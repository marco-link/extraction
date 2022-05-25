# -*- coding: utf-8 -*-

"""

Defines properties of histograms to produce in the ``histograms`` dict of dicts:

* dict key:         histogram name
* ``Branch``:       name of the branch (use ``Expression`` to definen non-existent branches)
* ``Title``:        Title shown in plot
* ``Xlabel``:       x axis label shown in plot
* ``Plot``:         list of plotoptions (available options: 'logX', 'logY', 'nolegend' 'nostack' 'density' 'step'/'errorbar')
* ``Histogram``:    binning of histogram e.g. {'nbins': 50, 'xmin': -300, 'xmax': 300}
* ``Expression``:   (optional) expression to calculate values from other branches
* ``datasets``:      (optional) list of datasets to limit histogram calculation to
"""

# TODO test varbins


from config.datasets import signal, background
signal = list(signal.keys())
background = list(background.keys())


plotoptions = ['nostack', 'density', 'step']
plotoptions = ['logY']
plotoptions = []


histograms = {
    'lepton_pt': {
        'Title': '',
        'Xlabel': 'lepton pt',
        'Plot': plotoptions,
        'Branch': 'lepton_pt',
        'Expression': 'if(ntightMuons==1) {return tightMuons_pt[0];} else {return tightElectrons_pt[0];}',
        'Histogram': {'nbins': 100, 'xmin': 0, 'xmax': 400},
    },

    'top_mass': {
        'Title': '',
        'Xlabel': 'm_{t}',
        'Plot': plotoptions,
        'Branch': 'top_mass_nominal',
        'Histogram': {'nbins': 100, 'xmin': 0, 'xmax': 800},
    },

    'top_pt': {
        'Title': '',
        'Xlabel': 'top pt',
        'Plot': plotoptions,
        'Branch': 'top_pt_nominal',
        'Histogram': {'nbins': 100, 'xmin': 0, 'xmax': 400},
    },

    'met': {
        'Title': '',
        'Xlabel': 'MET',
        'Plot': plotoptions,
        'Branch': 'met_nominal',
        'Histogram': {'nbins': 100, 'xmin': 0, 'xmax': 1000},
    },

    'mtw': {
        'Title': '',
        'Xlabel': 'MET',
        'Plot': plotoptions,
        'Branch': 'mtw_nominal',
        'Histogram': {'nbins': 100, 'xmin': 0, 'xmax': 300},
    },

    'fitbins': {
        'Branch': 'fitBins',
        'Expression': 'int x = 0; \
            if(std::fabs(top_mass_nominal-172.5)<25.) x++; \
            if(ntightMuons==1) { if(tightMuons_charge[0]>0) x += 2; } else {  if(tightElectrons_charge[0]>0) x += 2; } \
            return x;',
        'Histogram': {'nbins': 4, 'xmin': -0.5, 'xmax': 3.5},
        'Title': 'Fit bins',
        'Xlabel': 'category',
        'Plot': plotoptions,
    },
}
