#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Defines some general helper functions
"""


import ROOT
import numpy
from config.datasets import datasets
from config.systematics import systematics
from config.data import data as realdatadict
from config.general import general, fnames
import json
import os


def getGridpaths(year, setname):
    """
    Reads paths to NanoAOD files on the grid from the config files.

    :param isMC: set to True if the requested dataset is MC
    :param year: year of the dataset
    :param setname: long name of the dataset
    :returns: paths to files as list
    """
    datasetdir = general['DataSetsPath'] + '/' + year + '/' + setname

    with open(datasetdir + '/' + fnames['sample_merged_file_list'], 'r') as f:
        files = json.load(f)
        return [datasetdir + '/' + r for r in files]


def getSystsplit(systematic):
    """
    splits sytematic string into naem and variation direction.

    :param systematic: systematic sting constisting of systematic name and variation (``UP`` or ``DOWN``)
    :returns: systematic name, variation direction
    """
    sys_name = systematic.replace('UP', '').replace('DOWN', '')
    direction = systematic.replace(sys_name, '')

    return sys_name, direction


def datasetRegistered(setfilename: str):
    """
    Returns True if a dataset is registered
    """
    alldsets = datasets.copy()
    alldsets.update(realdatadict)
    for k in alldsets.keys():
        if datasets[k]['FileName'] == setfilename:
            return True
    return False


def datasetIsMC(setdirname: str):
    """

    returns isMC for a dataset that is registered, raises exception otherwise
    """
    alldsets = datasets.copy()
    alldsets.update(realdatadict)
    for k in alldsets.keys():
        if datasets[k]['FileName'] == setdirname:
            return datasets[k]['MC']

    raise ValueError('dataset ' + setdirname + 'not registered')


def getDatasetInfo(paths, dset):
    """
    Reads dataset information from `Runs` Tree of all files in a dataset

    :param paths: a list of files associated to dataset
    :param dset: an entry of the dataset dictionary
    :returns: dict of entries
    """
    globalInfo = {
        'genEventCount': 0,
        'genEventSumw': 0,
        'genEventSumw2': 0,
        'LHEScaleSumw': None,
        'LHEPdfSumw': None,
    }

    MC = dset['MC']

    if 'WbjToLNu' in paths[0]:
        for i in range(105):
            globalInfo['LHESumw_width_{}'.format(i + 1)] = 0

    #this is slow in MT mode
    ROOT.DisableImplicitMT()

    if MC:
        for path in paths:
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

    print('\n\n----- GlobalInfo -----')
    for label in globalInfo:
        # convert to relative weight
        if 'genEvent' not in label:
            globalInfo[label] = globalInfo[label] / globalInfo['genEventSumw']

        print(f'{label}: {globalInfo[label]}')
    print('----------------------')

    # get back to previous configuration
    if general['EnableImplicitMT']:
        ROOT.EnableImplicitMT()

    return globalInfo


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

    if datasets[dataset]['MC']:
        if 'EventWeights' in datasets[dataset][year].keys():
            for weight in datasets[dataset][year]['EventWeights']:
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


def histopath(year, region, dataset, systematic=None, number=None):
    """
    Generates path of the histogram file using the given parameters.
    If the path doesn't exist it is generated.

    :param year: year of the histogram
    :param region: filename of the histogram
    :param dataset: dataset label of the histogram
    :param systematic: systematic of the histogram
    :param number: file number, `None` for merged file
    :returns: path to root file for the histograms
    """
    histodir = ''

    if systematic is None or systematic == 'None':
        histodir = general['HistoPath'] + '/data/{year}/{region}/'.format(year=year, region=region)
    else:
        histodir = general['HistoPath'] + '/mc/{year}/{region}/{systematic}/'.format(year=year, region=region, systematic=systematic)

    if not os.path.exists(histodir):
        os.makedirs(histodir)

    if number is None:
        return histodir + dataset + '.root'
    else:
        return histodir + dataset + '_{}'.format(number) + '.root'
