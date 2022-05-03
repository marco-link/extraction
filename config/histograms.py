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
    #'parton_top_mass': {
        #'Branch': 'partonLevel_top_mass',
        #'Histogram': {'nbins': 35, 'xmin': 0, 'xmax': 350},
        #'datasets': signal,
        #'Title': '',
        #'Xlabel': 'partonLevel top mass',
    #},

    ##'Reco_Wb': {
        ##'Title': '',
        ##'Xlabel': 'Reco_Wb_mass',
        ##'Plot': plotoptions,
        ##'Branch': 'Reco_Wb_mass',
        ##'Histogram': {'nbins': 100, 'xmin': 0, 'xmax': 500},
    ##},

    #'top_mass': {
        #'Title': '',
        #'Xlabel': 'm_{t}',
        #'Plot': plotoptions,
        #'Branch': 'top_mass_nominal',
        #'Histogram': {'nbins': 100, 'xmin': 0, 'xmax': 1000},
    #},

    #'met': {
        #'Title': '',
        #'Xlabel': 'MET',
        #'Plot': plotoptions,
        #'Branch': 'met_nominal',
        #'Histogram': {'nbins': 100, 'xmin': 0, 'xmax': 1000},
    #},

    'fitcategories': {
        'Branch': 'fit_category',
        'Expression': 'int x = 1; if(std::fabs(top_mass_nominal-172.5)<25.) {x++;} \
            if(ntightMuons==1) {return x * tightMuons_charge[0];} else {return x * tightElectrons_charge[0];}',
        'Histogram': {'nbins': 5, 'xmin': -2.5, 'xmax': 2.5},
        'Title': 'Fit categories',
        'Xlabel': 'category',
        'Plot': plotoptions,
    },
}
