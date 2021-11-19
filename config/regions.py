# -*- coding: utf-8 -*-

"""
Defines different analysis regions in ``regions`` dict of dicts:

* dict key: region name
* ``Name``:     long name of the region
* ``Filter``:   region defining filter
"""


regions = {
    'muon': {
        'Name': 'SingleMuon region',
        'Filter': 'ntightMuons == 1',
    },



    'electron': {
        'Name': 'SingleElectron region',
        'Filter': 'ntightElectrons == 1',
    },

}
