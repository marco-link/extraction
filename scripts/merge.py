#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
merge output files from grid storage to single local file
usage: python merge.py <primary dataset name> <input path (nfs)> <output path (local storage)>
'''

import os
import datetime
import ROOT
from grid_tools import get_all_sample_files
import json
from helpers import datasetRegistered, datasetIsMC, writeDatasetInfo, datasetKeysFromFileName
from config.general import fnames, allyears
from grid_tools import _syscall
from multiprocessing import Pool
from argparse import ArgumentParser


def read_entries_local(filepath):
    n_i_selected = 0
    n_i_total = 0

    try:

        ifile = ROOT.TFile(filepath, 'READ')

        itree_evt = ifile.Get('Events')
        itree_run = ifile.Get('Runs')

        itree_run.GetEntry()

        # skip data
        if int(itree_run.run) != 1:
            return n_i_selected, n_i_total

        n_i_selected = int(itree_evt.GetEntries())
        n_i_total = int(itree_run.genEventCount)

        ifile.Close()

    except Exception as e:
        print(filepath, 'has encountered issue', e, 'will skip.')
        n_i_total = -1
        n_i_selected = -1

    return n_i_selected, n_i_total


# this is quite specitic now
def read_entries_xrootd(filepath):
    '''
    Returns entries in skimmed tree and entries before skim using xrootd.
    The workaround using system calls is needed on machines that use CC8,
    and does not hurt on CC7 machines, so I stuck to it.
    '''

    postskim, preskim = 0, 0

    rootscript = '''
    long long nentries = Events->GetEntries();
    long long npreentries = 0;
    Runs->SetBranchAddress(\\"genEventCount\\",&npreentries);
    Runs->GetEntry();
    cout << nentries << \\" \\" << npreentries << endl;
    '''

    try:
        call = "echo \"" + rootscript + "\" | root -l -b " + filepath + ' 2> /dev/null '
        r = _syscall(call)

        r = str(r, 'utf-8')
        r = r.split('\n')
        r = [e for e in r if e != '']
        r = r[-1].split(' ')

        preskim = int(r[1])
        postskim = int(r[0])

    except Exception as e:
        print(filepath, 'has encountered issue', e, 'will skip.')
        postskim, preskim = -1, -1

    # print('done')
    return postskim, preskim


def read_entries(filepath):

    post, pre = None, None
    if filepath[:5] == 'xroot':
        post, pre = read_entries_xrootd(filepath)
    else:
        post, pre = read_entries_local(filepath)

    return post, pre


def efficiency(filepath):

    n_i_selected, n_i_total = read_entries(filepath)

    if n_i_selected != n_i_total:
        print('--- selected events: {}, initial events: {} ---> preskim efficiency: {:.3f}'.format(n_i_selected,
                                                                                                   n_i_total,
                                                                                                   n_i_selected / n_i_total))
    return n_i_selected, n_i_total


def fill_userinfo(eff, filepath):
    f = ROOT.TFile(filepath, 'UPDATE')

    t = f.Get('Events')

    eff_string = 'efficiency:' + str(eff)

    t.GetUserInfo().Add(ROOT.TObjString(eff_string))

    f.Write('', ROOT.TObject.kOverwrite)

    f.Close()


def mergeFiles(args):
    '''
    This function is the actual function to merge a set of files to one output file.
    This could possibly also be run on the batch system.
    Inputs:
    - file list: which files to merge (absolute)
    - entries list: how many pre skim, post skim entries these files have (for later bookkeeping)
                    (one element of the output of events_per_file)
    - output path: full absolute output path including .root
    - index: the number of the file merge (only used for printouts)
    - skip_existing: skips existing merged files and returns immediately
    '''
    # opath with extension

    file_list, entries_list, opath, index, skip_existing = args

    bookfile = os.path.splitext(opath)[0]
    # this is just internal, no need to use imported names from general here
    summaryfile = bookfile + '_summary.txt'
    if skip_existing:
        if os.path.isfile(summaryfile):
            print('+++ ALREADY EXISTS! Skipping', index, opath, ' +++')
            return opath

    merger = ROOT.TFileMerger(False)
    merger.SetFastMethod(True)

    n_selected = 0
    n_total = 0

    t_start = datetime.datetime.now()

    print('outfile', opath)

    for i, F in enumerate(file_list):
        # F = F.replace('/storage/gridka-nrg/','root://cmsxrootd-redirectors.gridka.de//store/user/')
        # print('Adding ->' + F, i, '/', len(file_list))
        merger.AddFile(F)

        n_i_selected = 0
        n_i_total = 0

        n_i_selected, n_i_total = entries_list[i]
        n_selected += n_i_selected
        n_total += n_i_total

    # compression level is set to maximum (=209), same as input files
    # -> less space needed and faster merging - really faster merging???
    merger.OutputFile(opath, 'RECREATE', 209)
    merger.Merge()

    if n_selected != n_total:
        eff = n_selected / n_total
        print('\npreskim summary, filling userinfo with efficiency in output file:')
        print('--- selected events: {}, initial events: {} ---> preskim efficiency: {:.3f}'.format(n_selected, n_total, eff))
        fill_userinfo(eff, opath)

    # add bookkeeping into
    with open(summaryfile, 'w') as f:
        for fp in file_list:
            f.write(fp + '\n')

    t_run = datetime.datetime.now() - t_start
    print('+++ DONE! ', index, opath, ' +++', 'runtime: {}'.format(t_run))
    return opath


def eventsPerFiles(allfiles):
    from multiprocessing import Pool
    with Pool() as p:
        return p.map(read_entries, allfiles)


def cleanBrokenFiles(allfiles, evpf):
    oevpf = [e for e in evpf if e[0] >= 0]
    oallf = [allfiles[i] for i in range(len(allfiles)) if evpf[i][0] >= 0]
    return oallf, oevpf


def splitFileList(allfiles, opath, feventlist, eventsperfile=100000):

    ecounter = 0
    out = []
    temp = []
    tempentries = []

    for i, fpath in enumerate(allfiles):
        nentries, preskim = feventlist[i]
        tempentries.append((nentries, preskim))
        ecounter += nentries
        temp.append(fpath)
        if ecounter >= eventsperfile or i == len(allfiles) - 1:
            # dump
            out.append((opath + '/merged_' + str(len(out)) + '.root',
                        temp, tempentries))
            ecounter = 0
            temp = []
            tempentries = []

    # sanity check
    procfiles = []
    for e in out:
        procfiles.extend(e[1])
    assert procfiles == allfiles

    return out


def writeOutFileList(splitfilelist, opath):
    # for bookkeeping purposes
    pass


def clear_success_tag(opath):
    os.system('rm -f ' + opath + '/' + fnames['merge_success_tag'])


def add_success_tag(opath):
    os.system('touch ' + opath + '/' + fnames['merge_success_tag'])


def check_success_tag(opath):
    return os.path.isfile(opath + '/' + fnames['merge_success_tag'])


def createOrLoadMergeRules(ipath, opath, eventsperfile, maxfiles=-1, recreate=False, isMC=True, verbose=True):

    # if there is an issue, just redo
    try:
        if os.path.isfile(opath + '/' + fnames['sample_merge_rules']) and not recreate:
            with open(opath + '/' + fnames['sample_merge_rules'], 'r') as f:
                return json.load(f)
    finally:
        pass

    if verbose:
        print('getting files...')
    allfiles = get_all_sample_files(ipath)

    if maxfiles > 0:
        allfiles = allfiles[:args.maxfiles]  # DEBUG

    if len(allfiles) < 1:
        raise RuntimeError('No files selected in path ' + ipath)

    if verbose:
        print('reading events...')
    evpf = eventsPerFiles(allfiles)

    allfiles, evpfn = cleanBrokenFiles(allfiles, evpf)
    if isMC:
        print('Dataset is MC, some files broken; removed',
              (1. - len(evpfn) / len(evpf)) * 100., '% of files')
        evpf = evpfn
    elif evpf != evpfn:
        broken = []
        for f in evpf:
            if not f in evpfn:
                broken.append(f)
        raise RuntimeError(
            'Dataset is real data, and some files are broken. exiting. Broken: ' + str(broken))

    if verbose:
        print('creating splits...')
    m = splitFileList(allfiles, opath, evpf, eventsperfile)

    with open(opath + '/' + fnames['sample_merge_rules'], 'w') as f:
        json.dump(m, f)

    return m


def doMerge(ipath, opath, eventsperfile, maxfiles, overwrite, year, verbose=True):

    # check if it needs to run

    if not overwrite and check_success_tag(opath):
        print('merge already done, skipping', opath)
        exit()

    if overwrite and check_success_tag(opath):
        if verbose:
            print('overwriting', opath)
        clear_success_tag(opath)

    # check if dataset is registered

    datasetname = os.path.basename(os.path.normpath(opath))

    if not datasetRegistered(datasetname):
        raise ValueError(datasetname + ' error.\nDataset ' + datasetname + ' not registered. Choose an output path (last directory)\
 compatible with dataset names in configs/datasets.py or configs/data.py')

    # defines if broken files may be skipped or not
    isMC = datasetIsMC(datasetname)
    

    if isMC and verbose:
        print('dataset is MC')

    # create dir tree

    os.system('mkdir -p ' + opath)

    # create merge rules (which files go where)

    # for MC, remove broken files, for data fail if there are broken files

    m = createOrLoadMergeRules(ipath, opath, eventsperfile,
                               maxfiles=maxfiles,
                               recreate=overwrite,
                               isMC=isMC)

    # this part can also be run on batch with small modifications
    # since the merge rules have already been defined and saved above
    
    if verbose:
        print('perform merging...')

    pool_inputs = []
    for i, descr in enumerate(m):
        pool_inputs.append((descr[1], descr[2], descr[0], i, not overwrite))

    # this could be sent to batch
    with Pool(10) as p:
        mfiles = p.map(mergeFiles, pool_inputs)

    #then wait and continue here
    local_mfiles_paths = [os.path.basename(e) for e in mfiles]
    with open(opath + '/' + fnames['sample_merged_file_list'], 'w') as f:
        json.dump(local_mfiles_paths, f)

    datasetkeys = datasetKeysFromFileName(datasetname)
    #add dataset info
    for datasetkey in datasetkeys:
        writeDatasetInfo(year, datasetkey, inpaths=mfiles, outdir=opath)
    
    add_success_tag(opath)
    if verbose:
        print('done merging.')
        
        

############ call the script ###########



parser = ArgumentParser('merge root files')
parser.add_argument(
    'inputPath', help='root path of the sample, e.g. .../WbjToLNu_4f_TuneCP5_13TeV-madgraph-pythia8/WbNanoAODTools_2022-07-12_v7')
parser.add_argument(
    'outputPath', help='output path where the merged files will be stored. This needs to be a directoy that may or may not already exist.')
parser.add_argument(
    'year', help='Year')

# leave these hard coded, just for testing
# parser.add_argument('--eventsperfile', default=300000, help = 'maximum events per merged output file.', type=int)
# parser.add_argument('--maxfiles', default=-1, help = 'maximum files to consider (mostly for debugging)', type=int)

parser.add_argument('--overwrite', default=False,
                    help='Overwrite even if the merge has already been successful', action='store_true')
args = parser.parse_args()

if not args.year in allyears:
    raise ValueError(args.year + " unavailable as year. Available are "+str(allyears))

doMerge(args.inputPath, args.outputPath, 6000000, -1, args.overwrite, year=args.year)
