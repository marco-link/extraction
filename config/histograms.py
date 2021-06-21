# -*- coding: utf-8 -*-

"""
key = Branchname (or nonexistent Branch if 'Expression' is used)

Title:      Title shown in plot
Xlabel:     x axis label shown in plot
Histogram:  binning of histogram e.g. {'nbins': 50, 'xmin': -300, 'xmax': 300}
Branch: TODO
Expression: (optional) expression to calculate values from other branches
Samples:    (optional) list of samples to limit histogram calculation to
"""

#TODO test varbins


from config.samples import background
background = list(background.keys())




histograms = {
    'Gen_Wb_mass': {
        'Branch': 'Reco_Wb_mass',
        'Histogram': {'nbins': 50, 'xmin': 0, 'xmax': 600},
        'Samples': ['WbWbX_3'],
        'Title': '',
    },

    'Reco_Wb_mass': {
        'Title': '',
        'Branch': 'Reco_Wb_mass',
        'Histogram': {'nbins': 50, 'xmin': 0, 'xmax': 600},
        'Samples': ['WbWbX_3'] + background,
    },

    'Reco_Wb_on_offshell': {
        'Branch': 'Reco_Wb_mass',
        'Histogram': {'nbins': 50, 'xmin': 0, 'xmax': 600},
        'Samples': ['WbWbX_onshell', 'WbWbX_offshell'],
        'Title': '',
        'Xlabel': 'Reco_Wb_mass',
    },

    'Wb_diff': {
        'Branch': 'Wb_diff',
        'Expression': 'Reco_Wb_mass - Gen_Wb_mass',
        'Histogram': {'nbins': 50, 'xmin': -300, 'xmax': 300},
        'Samples': ['WbWbX_3'],
        'Title': '',
        'Xlabel': 'Reco_Wb - Gen_Wb in GeV',
        'Ylabel': 'entries',
    },
}
