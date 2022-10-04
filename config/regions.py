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
        'Name': 'WJets control region (muon)',
        'Filter': '(nselectedJets_nominal == 2 && nselectedBJets_nominal == 0 && ntightMuons == 1)',
    },
    'WJets_electron': {
        'Name': 'WJets control region (electron)',
        'Filter': '(nselectedJets_nominal == 2 && nselectedBJets_nominal == 0 && ntightElectrons == 1)',
    },


    # 2j1t
    'signal_muon': {
        'Name': 'signal region (muon)',
        'Filter': '(nselectedJets_nominal == 2 && nselectedBJets_nominal == 1 && ntightMuons == 1)',
    },
    'signal_electron': {
        'Name': 'signal region (electron)',
        'Filter': '(nselectedJets_nominal == 2 && nselectedBJets_nominal == 1 && ntightElectrons == 1)',
    },


    # 3j1t
    'ttbar_3j1t_muon': {
        'Name': 'ttbar 1 tag control region (muon)',
        'Filter': '(nselectedJets_nominal == 3 && nselectedBJets_nominal == 1 && ntightMuons == 1)',
    },
    'ttbar_3j1t_electron': {
        'Name': 'ttbar 1 tag control region (electron)',
        'Filter': '(nselectedJets_nominal == 3 && nselectedBJets_nominal == 1 && ntightElectrons == 1)',
    },

    # 3j2t
    'ttbar_3j2t_muon': {
        'Name': 'ttbar 2 tag control region (muon)',
        'Filter': '(nselectedJets_nominal == 3 && nselectedBJets_nominal == 2 && ntightMuons == 1)',
    },
    'ttbar_3j2t_electron': {
        'Name': 'ttbar 2 tag control region (electron)',
        'Filter': '(nselectedJets_nominal == 3 && nselectedBJets_nominal == 2 && ntightElectrons == 1 )',
    },
}

regions = {
    
    'ttbar_muon': {
        'Name': 'ttbar muon+jets',
        'Filter': '(ntightMuons == 1  && nselectedJets_nominal >= 4 && nselectedBJets_nominal == 2)',
    },
    #
    #'inclusive_electron': {
    #    'Name': 'inclusive one electron',
    #    'Filter': '(ntightElectrons == 1)',
    #},
    # 2j1t
    'signal_muonBpos': {
        'Name': 'signal region (muon) Bpos',
        'Filter': '(nselectedJets_nominal == 2 && nselectedBJets_nominal == 1 && ntightMuons == 1 && top_bjet_bChargeTag_highestScoreIndex_nominal == 3)',
    },
    'signal_muon': {
        'Name': 'signal region (muon)',
        'Filter': '(nselectedJets_nominal == 2 && nselectedBJets_nominal == 1 && ntightMuons == 1)',
    },
    
    #'signal_electron': {
    #    'Name': 'signal region (electron)',
    #    'Filter': '(nselectedJets_nominal == 2 && nselectedBJets_nominal == 1 && ntightElectrons == 1)',
    #},
    
    
}
#for category in bChargeCategories:
#    for region in templateRegions:
#        regions[region + '_' + category[0]] = {
#            'Name': templateRegions[region]['Name'] + ' ' + category[0],
#            'Filter': templateRegions[region]['Filter'] + ' && ' + category[1],
#        }
#