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
    # 2j0t
    'WJets_muon': {
        'Name': r'$1\mu$ WJets CR (2j0t)',
        'Filter': '(nselectedJets_nominal == 2 && nselectedBJets_nominal == 0 && ntightMuons == 1)',
    },
    'WJets_electron': {
        'Name': r'$1e$ WJets CR (2j0t)',
        'Filter': '(nselectedJets_nominal == 2 && nselectedBJets_nominal == 0 && ntightElectrons == 1)',
    },

    # 2j1t
    'signal_muon': {
        'Name': r'$1\mu$ signal region (2j1t)',
        'Filter': '(nselectedJets_nominal == 2 && nselectedBJets_nominal == 1 && ntightMuons == 1)',
    },
    'signal_electron': {
        'Name': r'$1e$ signal region (2j1t)',
        'Filter': '(nselectedJets_nominal == 2 && nselectedBJets_nominal == 1 && ntightElectrons == 1)',
    },


    # 3j1t
    'ttbar_3j1t_muon': {
        'Name': r'$1\mu$ ttbar CR (3j1t)',
        'Filter': '(nselectedJets_nominal == 3 && nselectedBJets_nominal == 1 && ntightMuons == 1)',
    },
    'ttbar_3j1t_electron': {
        'Name': r'$1e$ ttbar CR (3j1t)',
        'Filter': '(nselectedJets_nominal == 3 && nselectedBJets_nominal == 1 && ntightElectrons == 1)',
    },

    # 3j2t
    'ttbar_3j2t_muon': {
        'Name': r'$1\mu$ ttbar CR (3j2t)',
        'Filter': '(nselectedJets_nominal == 3 && nselectedBJets_nominal == 2 && ntightMuons == 1)',
    },
    'ttbar_3j2t_electron': {
        'Name': r'$1e$ ttbar CR (3j2t)',
        'Filter': '(nselectedJets_nominal == 3 && nselectedBJets_nominal == 2 && ntightElectrons == 1 )',
    },
}


regions = templateRegions



#for category in bChargeCategories:
#    for region in templateRegions:
#        regions[region + '_' + category[0]] = {
#            'Name': templateRegions[region]['Name'] + ' ' + category[0],
#            'Filter': templateRegions[region]['Filter'] + ' && ' + category[1],
#        }
#
