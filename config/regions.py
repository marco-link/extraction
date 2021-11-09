# -*- coding: utf-8 -*-


regions = {
    'muon': {
        'Name': 'SingleMuon region',
        'Label': {
            'X': 0.2,
            'Y': 0.83,
            'Font': 42,
            'Size': 0.05,
            'Text': 'region'
        },
        'Filter': 'ntightMuons == 1',
    },



    'electron': {
        'Name': 'SingleElectron region',
        'Label': {
            'X': 0.2,
            'Y': 0.83,
            'Font': 42,
            'Size': 0.05,
            'Text': 'region'
        },
        'Filter': 'ntightElectrons == 1',
    },

}
