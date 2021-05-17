# -*- coding: utf-8 -*-

"""
key = Branchname (or nonexistent Branch if 'Expression' is used)

Title:      Title shown in plot
Xlabel:     x axis label shown in plot
Histogram:  binning of histogram e.g. {'nbins': 50, 'xmin': -300, 'xmax': 300}
Expression: (optional) expression to calculate values from other branches
Samples:    (optional) list of samples to limit histogram calculation to
"""

#TODO test varbins


histset = {
    'Gen_Wb_mass': {
        'Title': '',
        'Histogram': {'nbins': 50, 'xmin': 0, 'xmax': 600},
        'Samples': ['WbWbX'],
    },

    'Reco_Wb_mass': {
        'Title': '',
        'Histogram': {'nbins': 50, 'xmin': 0, 'xmax': 600},
    },

    'Wb_diff': {
        'Title': '',
        'Xlabel': 'Reco_Wb - Gen_Wb in GeV',
        'Ylabel': 'entries',
        'Expression': 'Reco_Wb_mass - Gen_Wb_mass',
        'Histogram': {'nbins': 50, 'xmin': -300, 'xmax': 300},
        'Samples': ['WbWbX'],
    },
}


for i in range(9):
    i = i + 1
    histset['Wb_diff_{}'.format(i)] = {
        'Title': '',
        'Xlabel': '$m^{Reco}_{Wb} - m^{gen}_{Wb}$ (GeV)',
        'Expression': 'reco_Wb{}_mass - Gen_Wb_mass'.format(i),
        'Histogram': {'nbins': 50, 'xmin': -300, 'xmax': 300},
        'Samples': ['WbWbX'],
    }
