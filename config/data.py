# -*- coding: utf-8 -*-

"""
Defines the names and properties of the datasets from real data in a data dict of dicts:

* dict key:         dataset name
* ``MC``:           bool, True for MC
* ``FileName``:     root filename of dataset
* ``Label``:        plotlabel
* ``Color``:        plotcolor
"""


data = {
    'SingleMuon': {
        'MC': False,
        'FileName': 'SingleMuon',
        'Label': r'data (muon)',
        'Group': 'data',
    },

    'SingleElectron': {
        'MC': False,
        'FileName': 'SingleElectron',
        'Label': r'data (electron)',
        'Group': 'data',
    },
}
