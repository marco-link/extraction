# -*- coding: utf-8 -*-

"""
Defines different analysis regions in ``regions`` dict of dicts:

* dict key: region name
* ``Name``:     long name of the region
* ``Filter``:   region defining filter
"""


# TODO btag regions
# 0: Bneg
# 1: B0bar
# 2: B0
# 3: Bpos


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
