# -*- coding: utf-8 -*-

import os

general = {
    'MCPath': '/ceph/mlink/Wb/mc/',
    'DataPath': '/ceph/mlink/Wb/data/',
    'Suffix': '.root',
    'Tree': 'Friends',
    'Histodir': 'Histograms',
    'GlobalDefaultValue': -999,
    'Pi': 3.141,
    'DeltaR': 0.4,
    'Lumi': {
        '2016': 35.9,
        '2017': -1,
        '2018': -1,
    },
}

allyears = ['2016_VFP', '2016', '2017', '2018']


# taken from https://twiki.cern.ch/twiki/bin/view/CMS/PdmVRun2LegacyAnalysis (Oct 2021)
lumi = {
    '2016_VFP': 19.52,
    '2016': 16.81,
    '2017': 41.48,
    '2018': 59.83,
}



def samplepath(isMC, year=None, filename=None):
    if isMC:
        return general['MCPath'] + year + '/' + filename + general['Suffix']

    else:
        raise Exception('samplepath not defined for data yet!')
        #return general['DataPath'] + year + '/' + run + '/'


def histopath(isMC, year=None, filename=None, region=None, systematic=None):
    histodir = ''

    if isMC:
        histodir = general['MCPath'] + '/{year}/{region}/{systematic}/'.format(year=year, region=region, systematic=systematic)

    else:
        raise Exception('histopath not defined for data yet!')
        #return general['DataPath'] + year + '/' + run + '/'

    if not os.path.exists(histodir):
        os.makedirs(histodir)

    return histodir + filename + general['Suffix']
