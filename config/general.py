# -*- coding: utf-8 -*-

"""
Contains global configuration options e.g. paths:

* general: several config definitions
* allyears: list with str for all years
* lumi: dict with luminosities for different epochs, keys are included in allyears and 'total'
"""



import os
import json

general = {
    'DataSetsPath': '/eos/cms/store/cmst3/group/top/WbWb/nano/2022-07-12_v7',
    'HistoPath': '/eos/cms/store/cmst3/group/top/WbWb/histos/2022-07-12_v7/' + os.getenv('USER') + '/',
    'CardPath': './output/cards/',
    'FitPath': './output/fits/',
    'PlotPath': './output/plots/',
    'LogPath': './output/logs/',
    'Tree': 'Events',
    'Histodir': 'Histograms',
    'GlobalDefaultValue': -999,
    'DeltaR': 0.4,
}

allyears = [
    #'2016_VFP',
    #'2016',
    '2017',
    #'2018',
]


# taken from https://twiki.cern.ch/twiki/bin/view/CMS/PdmVRun2LegacyAnalysis (Oct 2021)
lumi = {
    '2016_VFP': 19.52,
    '2016': 16.81,
    '2017': 41.48,
    '2018': 59.83,
    'total': 137.64, # sum of the above
}


# some general path globals

fnames = {
    'sample_merge_rules': 'sample_merges.json',
    'merge_success_tag': 'succ',
    'sample_merged_file_list': 'merged_files.json'
}



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
