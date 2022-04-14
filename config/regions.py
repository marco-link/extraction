# -*- coding: utf-8 -*-

"""
Defines different analysis regions in ``regions`` dict of dicts:

* dict key: region name
* ``Name``:     long name of the region
* ``Filter``:   region defining filter
"""


bChargeCategories = [
    ['Bneg', 'top_bjet_bChargeTag_highestScoreIndex_nominal == 0'],
    ['B0bar', 'top_bjet_bChargeTag_highestScoreIndex_nominal == 1'],
    ['B0', 'top_bjet_bChargeTag_highestScoreIndex_nominal == 2'],
    ['Bpos', 'top_bjet_bChargeTag_highestScoreIndex_nominal == 3'],
]

templateRegions = {
    # signal regions
    'signal_muon': {
        'Name': 'SingleMuon region',
        'Filter': '(ntightMuons == 1 && nselectedBJets_nominal == 1)',
    },

    'signal_electron': {
        'Name': 'SingleElectron region',
        'Filter': '(ntightElectrons == 1 && nselectedBJets_nominal == 1)',
    },

    # ttbar regions

    # QCD region

}

regions = {}
for category in bChargeCategories:
    for region in templateRegions:
        regions[region + '_' + category[0]] = {
            'Name': templateRegions[region]['Name'] + ' ' + category[0],
            'Filter': templateRegions[region]['Filter'] + ' && ' + category[1],
        }
