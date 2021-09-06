# -*- coding: utf-8 -*-

"""
key = Branchname (or nonexistent Branch if 'Expression' is used)

Title:      Title shown in plot
Xlabel:     x axis label shown in plot
Plot:       plotoptions (as list)
            'logX', 'logY',
            'nolegend'
            'nostack'
            'density'
            'step' or 'errorbar'
Branch:     TODO
Histogram:  binning of histogram e.g. {'nbins': 50, 'xmin': -300, 'xmax': 300}
Expression: (optional) expression to calculate values from other branches
Samples:    (optional) list of samples to limit histogram calculation to
"""

#TODO test varbins


from config.samples import background
background = list(background.keys())


plotoptions = ['nostack', 'density', 'step']
plotoptions = ['logY']


histograms = {

    #'Reco_Wb_on_offshell': {
        #'Branch': 'Reco_Wb3_mass',
        #'Histogram': {'nbins': 50, 'xmin': 0, 'xmax': 600},
        #'Samples': ['WbWbX_onshell', 'WbWbX_offshell'],
        #'Title': '',
        #'Xlabel': 'Reco_Wb_mass',
    #},

    #'Wb_diff': {
        #'Branch': 'Wb_diff',
        #'Expression': 'Reco_Wb_mass - Gen_Wb_mass',
        #'Histogram': {'nbins': 50, 'xmin': -300, 'xmax': 300},
        #'Samples': ['WbWbX_3'],
        #'Title': '',
        #'Xlabel': 'Reco_Wb - Gen_Wb in GeV',
    #},


    'Reco_Wb': {
        'Title': '',
        'Xlabel': 'Reco_Wb_mass',
        'Plot': plotoptions,
        'Branch': 'Reco_Wb_mass',
        'Histogram': {'nbins': 100, 'xmin': 0, 'xmax': 500},
    },

}


for i in range(9):
    histograms[f'Reco_Wb_{i}'] = {
        'Title': '',
        'Xlabel': 'Reco_Wb_mass',
        'Plot': plotoptions,
        'Branch': f'Reco_Wb{i}_mass',
        'Histogram': {'nbins': 100, 'xmin': 0, 'xmax': 500},
        'Samples': ['WbWbX_onshell', 'WbWbX_offshell'],
    }

    histograms[f'partonLevel_Wb_{i}'] = {
        'Title': '',
        'Xlabel': 'partonLevel_Wb_mass',
        'Plot': plotoptions,
        'Branch': f'partonLevel_Wb{i}_mass',
        'Histogram': {'nbins': 100, 'xmin': 0, 'xmax': 500},
        'Samples': ['WbWbX_onshell', 'WbWbX_offshell'],
    }

    histograms[f'particleLevel_Wb_{i}'] = {
        'Title': '',
        'Xlabel': 'particleLevel_Wb_mass',
        'Plot': plotoptions,
        'Branch': f'particleLevel_Wb{i}_mass',
        'Histogram': {'nbins': 100, 'xmin': 0, 'xmax': 500},
        'Samples': ['WbWbX_onshell', 'WbWbX_offshell'],

    }

    #histograms[f'particleLevel_MET_eta_{i}'] = {
    #'Title': '',
    #'Xlabel': 'particleLevel_MET_eta',
    #'Plot': [],
    #'Branch': f'particleLevel_MET_eta_{i}',
    #'Expression': f'particleLevel_W_met_eta[particleLevel_Wb{i}_W_idx]',
    #'Histogram': {'nbins': 100, 'xmin': -20, 'xmax': 20},
    #'Samples':  ['WbWbX_onshell', 'WbWbX_offshell'],
    #}

    histograms[f'comp_partonLevel_Wb_{i}'] = {
        'Title': '',
        'Xlabel': 'partonLevel_Wb_mass',
        'Plot': ['nostack', 'step', 'density'],
        'Branch': f'partonLevel_Wb{i}_mass',
        'Histogram': {'nbins': 100, 'xmin': 0, 'xmax': 500},
        'Samples': ['WbWbX_19', 'WbWbX_1'],
    }

    histograms[f'comp_particleLevel_Wb_{i}'] = {
        'Title': '',
        'Xlabel': 'particleLevel_Wb_mass',
        'Plot': ['nostack', 'step', 'density'],
        'Branch': f'particleLevel_Wb{i}_mass',
        'Histogram': {'nbins': 100, 'xmin': 0, 'xmax': 500},
        'Samples': ['WbWbX_19', 'WbWbX_1'],
    }

    histograms[f'comp_RecoLevel_Wb_{i}'] = {
        'Title': '',
        'Xlabel': 'Reco_Wb_mass',
        'Plot': ['nostack', 'step', 'density'],
        'Branch': f'Reco_Wb{i}_mass',
        'Histogram': {'nbins': 100, 'xmin': 0, 'xmax': 500},
        'Samples': ['WbWbX_19', 'WbWbX_1'],
    }
