# -*- coding: utf-8 -*-

"""
Contains global configuration options e.g. paths:

* general: several config definitions
* allyears: list with str for all years
* lumi: dict with luminosities for different epochs, keys are included in allyears and 'total'
"""

import os

version = '2022-11-09_v10'
storagepath = '/ceph/mlink/WbWbX/'

if os.getenv('HOSTNAME', None) == 'lxplus8s10.cern.ch':
    storagepath = '/scratch/jkiesele/WbWb/'

general = {
    'EnableImplicitMT': False, #this can be picked up wherever it makes sense
    'DataSetsPath': storagepath + version,
    'HistoPath': '/work/mlink/wb_scattering/extraction/output/Wbhistos/' + version + '/',
    'CardPath': './output/cards/',
    'FitPath': './output/fits/',
    'PlotPath': './output/plots/',
    'LogPath': './output/logs/',
    'Tree': 'Events',
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
