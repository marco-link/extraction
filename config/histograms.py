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
* ``Samples``:      (optional) list of samples to limit histogram calculation to
"""

# TODO test varbins


from config.samples import background
background = list(background.keys())


plotoptions = ['nostack', 'density', 'step']
plotoptions = ['logY']


histograms = {
    #'Wb_diff': {
        #'Branch': 'Wb_diff',
        #'Expression': 'Reco_Wb_mass - Gen_Wb_mass',
        #'Histogram': {'nbins': 50, 'xmin': -300, 'xmax': 300},
        #'Samples': ['WbWbX_19'],
        #'Title': '',
        #'Xlabel': 'Reco_Wb - Gen_Wb in GeV',
    #},

    #'Reco_Wb': {
        #'Title': '',
        #'Xlabel': 'Reco_Wb_mass',
        #'Plot': plotoptions,
        #'Branch': 'Reco_Wb_mass',
        #'Histogram': {'nbins': 100, 'xmin': 0, 'xmax': 500},
    #},

    'binCategory': {
        'Title': '',
        'Xlabel': 'Category',
        'Plot': plotoptions,
        'Branch': 'binCategory',
        'Histogram': {'nbins': 16, 'xmin': 0, 'xmax': 16},
        'Samples': ['WbWbX_19'] + background,
    },
}
