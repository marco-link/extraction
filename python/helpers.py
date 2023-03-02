#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Defines some general helper functions
"""


import ROOT
import numpy
from config.datasets import all_samples
from config.systematics import systematics
from config.general import general, fnames
import json
import os


def getDataSetDir(year, setname):
    return general['DataSetsPath'] + '/' + year + '/' + setname


def getGridpaths(year, setname):
    """
    Reads paths to NanoAOD files on the grid from the config files.

    :param isMC: set to True if the requested dataset is MC
    :param year: year of the dataset
    :param setname: long name of the dataset
    :returns: paths to files as list
    """
    datasetdir = getDataSetDir(year, setname)
    fname = datasetdir + '/' + fnames['sample_merged_file_list']

    try:
        with open(fname, 'r') as f:
            files = json.load(f)
            return [datasetdir + '/' + r for r in files]

    except Exception as e:
        print('issue with ' + fname)
        raise e


def getSystsplit(systematic):
    """
    splits sytematic string into naem and variation direction.

    :param systematic: systematic sting constisting of systematic name and variation (``UP`` or ``DOWN``)
    :returns: systematic name, variation direction
    """
    sys_name = systematic.replace('UP', '').replace('DOWN', '')
    sys_name = sys_name.replace('Up', '').replace('Down', '')
    direction = systematic.replace(sys_name, '')
    direction = direction.upper()
    return sys_name, direction


def useSystematicBranch(expression, systematic, verbose=True):
    """
    modify expression to use special systematic branches

    :param expression: expression to modify
    :paramsystematic: systematic to switch expression to
    :returns: modified expression
    """
    systematic, direction = getSystsplit(systematic)

    if verbose:
        print('systematic: ' + systematic + ' ' + direction)
        print('old expression: ' + expression)

    if 'Branch' in systematics[systematic].keys():
        expression = expression.replace('nominal', systematics[systematic]['Branch'][direction])

    if verbose:
        print('new expression: ' + expression)

    return expression


def datasetKeysFromFileName(setfilename):
    """
    One file name can have multiple keys
    """
    out = []
    for k in all_samples.keys():
        if all_samples[k]['FileName'] == setfilename:
            out.append(k)
    return out


def datasetRegistered(setfilename):
    """
    Returns True if a dataset is registered
    """
    return len(datasetKeysFromFileName(setfilename)) > 0


def datasetIsMC(setdirname):
    """

    returns isMC for a dataset that is registered, raises exception otherwise
    """
    for k in all_samples.keys():
        if all_samples[k]['FileName'] == setdirname:
            return all_samples[k]['MC']

    raise ValueError('dataset ' + setdirname + 'not registered')



def _getDatasetInfo(paths, dset_key, verbose=False):
    """
    Reads dataset information from `Runs` Tree of all files in a dataset

    :param paths: a list of files associated to dataset
    :param dset_key: a key of the all_samples dictionary
    :returns: dict of entries
    """


    globalInfo = {
        'genEventCount': 0,
        'genEventSumw': 0,
        'genEventSumw2': 0,
        'LHEScaleSumw': None,
        'LHEPdfSumw': None,
    }

    MC = all_samples[dset_key]['MC']

    if 'WbjToLNu' in paths[0]:
        for i in range(105):
            globalInfo['LHESumw_width_{}'.format(i + 1)] = 0

    #this is slow in MT mode
    if ROOT.IsImplicitMTEnabled():
        ROOT.DisableImplicitMT()

    if MC:
        for path in paths:
            if verbose:
                print('Reading dataset info from {}:'.format(path))
            inFile = ROOT.TFile.Open(path, 'READ')
            tree = inFile.Get('Runs')

            # loop over entries
            for entry in tree:
                gensum = getattr(entry, 'genEventSumw')

                for label in globalInfo:
                    val = getattr(entry, label)

                    # sum up absolute weight sums
                    if hasattr(val, '__add__'):
                        if globalInfo[label] is None:
                            globalInfo[label] = 0

                        if 'genEvent' in label:
                            globalInfo[label] += val
                        else:
                            globalInfo[label] += val * gensum
                    else:
                        if globalInfo[label] is None:
                            globalInfo[label] = numpy.zeros(len(val))

                        # sum up over list
                        if len(globalInfo[label]) == len(val):
                            globalInfo[label] += numpy.array(val) * gensum
                        else:
                            raise(Exception('array length mismatch!'))

            inFile.Close()


    # flatten arrays in dictionary
    tmp = {}
    for label in globalInfo:
        if isinstance(globalInfo[label], numpy.ndarray):
            for i, val in enumerate(globalInfo[label]):
                tmp[label + '_{}'.format(i)] = val
    globalInfo.update(tmp)

    # remove arrays items
    globalInfo = {key: val for key, val in globalInfo.items() if not isinstance(val, numpy.ndarray)}

    if verbose:
        print('\n\n----- GlobalInfo -----')
    for label in globalInfo:
        # convert to relative weight
        if MC and 'genEvent' not in label:
            globalInfo[label] = globalInfo[label] / globalInfo['genEventSumw']

        if verbose:
            print(label + ': ' + globalInfo[label])
    if verbose:
        print('----------------------')

    # get back to previous configuration
    if general['EnableImplicitMT'] and not ROOT.IsImplicitMTEnabled():
        ROOT.EnableImplicitMT()

    return globalInfo


def writeDatasetInfo(year, dsetkey, verbose=False, inpaths=None, outdir=None):
    dset = all_samples[dsetkey]
    setname = dset['FileName']
    if inpaths is None:
        inpaths = getGridpaths(year=year, setname=setname)

    print('>>>>', inpaths, dsetkey)

    d = _getDatasetInfo(inpaths, dsetkey, verbose)
    if outdir is None:
        outdir = getDataSetDir(year, dset['FileName'])

    opath = outdir + '/' + dsetkey + '_preskimInfo.json'

    with open(opath, 'w') as f:
        return json.dump(d, f)


def getDatasetInfo(year, dsetkey, verbose=False):
    """
    Reads dataset information from cached file

    :param paths: a list of files associated to dataset
    :param dset: an entry of the dataset dictionary
    :returns: dict of entries
    """
    dset = all_samples[dsetkey]
    # see if there is a cached dataset info already
    path = getDataSetDir(year, dset['FileName']) + '/' + dsetkey + '_preskimInfo.json'
    with open(path, 'r') as f:
        return json.load(f)


def get_event_weigths(year, dataset, systematic, constants={}):
    """
    generates weightstring from dataset and systematic name

    :param year: year
    :param dataset: dataset name
    :param systematic: systematic sting (name and variation direction)
    :param constants: dict used to replace expressions in weight expression with constants TODO implementation
    :returns: weightstring
    """
    weightstring = '1'
    if systematic is None or systematic == 'None':
        return weightstring

    if all_samples[dataset]['MC']:
        if 'EventWeights' in all_samples[dataset][year].keys():
            for weight in all_samples[dataset][year]['EventWeights']:
                if not weight:
                    continue
                else:
                    weightstring += '*({})'.format(weight)



        sys_name, direction = getSystsplit(systematic)
        if sys_name in systematics.keys():
            if 'EventWeights' in systematics[sys_name].keys():
                for weight in systematics[sys_name]['EventWeights'][direction]:
                    if not weight:
                        continue
                    else:
                        weightstring += '*({})'.format(weight)


        # replace sum over all samples with actual value
        weightkeys = sorted(constants.keys(), key=lambda l: (len(l), l))
        weightkeys.reverse()
        for key in weightkeys:
            weightstring = weightstring.replace(key, '{:.6f}'.format(constants[key]))

    return weightstring


def histopath(year, region, dataset, number=None, create_dir=False):
    """
    Generates path of the histogram file using the given parameters.
    If the path doesn't exist it is generated.

    :param year: year of the histogram
    :param region: filename of the histogram
    :param dataset: dataset label of the histogram
    :param number: file number, `None` for merged file
    :param create_dir: create output directory
    :returns: path to root file for the histograms
    """

    histodir = general['HistoPath'] + '/mc/{year}/{region}/'.format(year=year, region=region)

    #not thread safe just go with sys call
    if create_dir:
        os.system('mkdir -p ' + histodir)
    #if not os.path.exists(histodir):
    #    os.makedirs(histodir)

    if number is None:
        return histodir + dataset + '.root'
    else:
        return histodir + dataset + '_{}'.format(number) + '.root'
