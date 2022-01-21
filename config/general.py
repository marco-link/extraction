# -*- coding: utf-8 -*-

"""
Contains global configuration options e.g. paths:

* general: several config definitions
* allyears: list with str for all years
* lumi: dict with luminosities for different epochs, keys are included in allyears and 'total'
"""



import os

general = {
    'MCPath': '/eos/cms/store/cmst3/group/top/WbWb/friends/testing/mc/',
    'DataPath': '/eos/cms/store/cmst3/group/top/WbWb/friends/testing/data/',
    'HistoPath': '/eos/cms/store/cmst3/group/top/WbWb/histos/testing/',
    'CardPath': './output/cards/',
    'FitPath': './output/fits/',
    'PlotPath': './output/plots/',
    'LogPath': './output/logs/',
    'Tree': 'Friends',
    'Histodir': 'Histograms',
    'GlobalDefaultValue': -999,
    'DeltaR': 0.4,
}

allyears = [
    #'2016_VFP',
    '2016',
    #'2017',
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



def samplepath(isMC, year, filename):
    """
    Generates path of the sample using the given parameters.

    :param isMC: set to True if the requested sample is MC
    :param year: year of the sample
    :param filename: filename of the sample
    :returns: path to data/MC sample
    :raises: Exception: samplepath not defined for data yet! (if isMC=False, data not implementded yet)
    """
    if isMC:
        return general['MCPath'] + year + '/' + filename + '.root'
    else:
        raise Exception('samplepath not defined for data yet!')
        #return general['DataPath'] + year + '/' + run + '/'


def histopath(isMC, year, filename, region, systematic):
    """
    Generates path of the histogram file using the given parameters.
    If the path doesn't exist it is generated.

    :param isMC: set to True if the requested histogram is from MC
    :param year: year of the histogram
    :param filename: filename of the histogram
    :param region: filename of the histogram
    :param systematic: systematic of the histogram
    :returns: path to root file for the histograms
    :raises: Exception: histopath not defined for data yet! (if isMC=False, data not implementded yet)
    """
    histodir = ''

    if isMC:
        histodir = general['HistoPath'] + '/mc/{year}/{region}/{systematic}/'.format(year=year, region=region, systematic=systematic)
    else:
        raise Exception('histopath not defined for data yet!')
        #return general['DataPath'] + year + '/' + run + '/'

    if not os.path.exists(histodir):
        os.makedirs(histodir)

    return histodir + filename + '.root'
