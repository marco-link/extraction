#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
merge output files from grid storage to single local file
usage: python merge.py <primary dataset name> <input path (nfs)> <output path (local storage)>
'''

from __future__ import division
import os
import sys
import datetime
import ROOT


def efficiency(filepath):
    n_i_selected = 0
    n_i_total = 0

    ifile = ROOT.TFile(filepath, 'READ')

    itree_evt = ifile.Get('Events')
    itree_run = ifile.Get('Runs')

    itree_run.GetEntry()

    # skip data
    if int(itree_run.run) != 1:
        return n_i_selected, n_i_total

    n_i_selected = int(itree_evt.GetEntries())
    n_i_total = int(itree_run.genEventCount)

    if n_i_selected != n_i_total:
        print('--- selected events: {}, initial events: {} ---> preskim efficiency: {:.3f}'.format(n_i_selected,
                                                                                                   n_i_total,
                                                                                                   n_i_selected / n_i_total))

    ifile.Close()

    return n_i_selected, n_i_total


def fill_userinfo(eff, filepath):
    f = ROOT.TFile(filepath, 'UPDATE')

    t = f.Get('Events')

    eff_string = 'efficiency:' + str(eff)

    t.GetUserInfo().Add(ROOT.TObjString(eff_string))

    f.Write('', ROOT.TObject.kOverwrite)

    f.Close()


ipath = sys.argv[2]
opath = sys.argv[3]

print('\nMerging ' + sys.argv[1])
print('Input from ' + sys.argv[2])
print('Output to ' + sys.argv[3])
t_start = datetime.datetime.now()
print('\nStarting time: {}'.format(t_start))

# default max tree size is 100 GB per file, so this is increased to prevent automatic file splitting
# in principle smaller files are better for parallel processing,
# but they shrink drastically in size after skimming thanks to dropping all non-relevant systematics
print('\nMax tree size {}'.format(ROOT.TTree.GetMaxTreeSize()))
ROOT.TTree.SetMaxTreeSize(10000000000000) # 10 TB
print('Updated tree size {}'.format(ROOT.TTree.GetMaxTreeSize()))

merger = ROOT.TFileMerger(False)
merger.SetFastMethod(True)


# support splitting if subdir is also given (e.g. different data runs)
file_list = []
for ipath, dirs, files in os.walk(ipath):
    for filename in files:
        if ('%s' % sys.argv[1]) in ipath:
            if 'nano_' in filename:
                file_list.append(ipath + '/' + filename)

file_list = sorted(file_list)

#print('\n\nInput file list: {}'.format(file_list))
print('Number of input files: {}'.format(len(file_list)))
print('Output file: ' + opath)
print('Replacing local nfs paths with xrootd ...')


n_selected = 0
n_total = 0

for F in file_list:
    #F = F.replace('/storage/gridka-nrg/','root://cmsxrootd-redirectors.gridka.de//store/user/')
    print('Adding ->' + F)
    merger.AddFile(F)

    n_i_selected = 0
    n_i_total = 0

    n_i_selected, n_i_total = efficiency(F)
    n_selected += n_i_selected
    n_total += n_i_total


# compression level is set to maximum (=209), same as input files
# -> less space needed and faster merging
merger.OutputFile(opath, 'RECREATE', 209)
merger.Merge()

t_end = datetime.datetime.now()
print('\nEnding time: {}'.format(t_end))
t_run = t_end - t_start
print('Total runtime: {}'.format(t_run))

if n_selected != n_total:
    eff = n_selected / n_total
    print('\npreskim summary, filling userinfo with efficiency in output file:')
    print('--- selected events: {}, initial events: {} ---> preskim efficiency: {:.3f}'.format(n_selected, n_total, eff))
    fill_userinfo(eff, opath)

print('+++ DONE! +++')
