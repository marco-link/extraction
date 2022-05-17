# -*- coding: utf-8 -*-

"""
Contains global configuration options e.g. paths:

* general: several config definitions
* allyears: list with str for all years
* lumi: dict with luminosities for different epochs, keys are included in allyears and 'total'
"""



import os

general = {
    'MCPath': './config/mc/',
    'DataPath': './config/data/',
    'HistoPath': '/eos/cms/store/cmst3/group/top/WbWb/histos/2022-05-17_v1/',
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


def getGridpaths(isMC, year, filename):
    """
    Reads paths to NanoAOD files on the grid from the config files.

    :param isMC: set to True if the requested dataset is MC
    :param year: year of the dataset
    :param filename: filename of the dataset
    :returns: paths to files as list
    """
    filepath = ''
    if isMC:
        filepath = general['MCPath'] + year + '/' + filename + '.txt'
    else:
        filepath = general['DataPath'] + year + '/' + filename + '.txt'

    filelist = []
    with open(filepath, 'r') as files:
        for f in files:
            filelist.append(f.strip())

    return filelist



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
