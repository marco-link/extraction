# -*- coding: utf-8 -*-

"""

Defines properties of histograms to produce in the ``histograms`` dict of dicts:

* dict key:         histogram name
* ``Branch``:       name of the branch (use ``Expression`` to definen non-existent branches)
* ``Title``:        Title shown in plot
* ``Xlabel``:       x axis label shown in plot
* ``Plot``:         list of plotoptions (available options: 'logX', 'logY', 'nolegend' 'nostack' 'density' 'step'/'errorbar')
* ``Histogram``:    binning of histogram e.g. {'nbins': 50, 'xmin': -300, 'xmax': 300}
                    or in binedges e.g. {'varbins': [1, 2, 3, 4, 5]}
* ``Expression``:   (optional) expression to calculate values from other branches
* ``datasets``:      (optional) list of datasets to limit histogram calculation to
"""


import numpy

from config.datasets import signal, background
signal = list(signal.keys())
background = list(background.keys())


plotoptions = ['nostack', 'density', 'step']
plotoptions = ['logY']
plotoptions = []


histograms = {

    # lepton
    'lepton_pt': {
        'Title': '',
        'Xlabel': 'Lepton pt',
        'Plot': plotoptions + ['logX'],
        'Branch': 'lepton_pt',
        'Expression': 'if(ntightMuons==1) {return tightMuons_pt[0];} else {return tightElectrons_pt[0];}',
        'Histogram': {'varbins': numpy.geomspace(20, 400, 31)},
    },

    'lepton_eta': {
        'Title': '',
        'Xlabel': 'Lepton eta',
        'Plot': plotoptions,
        'Branch': 'lepton_eta',
        'Expression': 'if(ntightMuons==1) {return tightMuons_eta[0];} else {return tightElectrons_eta[0];}',
        'Histogram': {'nbins': 30, 'xmin': -3, 'xmax': 3},
    },

    # TODO add to NanoAODTools output
    #'lepton_phi': {
        #'Title': '',
        #'Xlabel': 'Lepton phi',
        #'Plot': plotoptions,
        #'Branch': 'lepton_phi',
        #'Expression': 'if(ntightMuons==1) {return tightMuons_phi[0];} else {return tightElectrons_phi[0];}',
        #'Histogram': {'nbins': 30, 'xmin': -numpy.pi, 'xmax': -numpy.pi},
    #},

    'lepton_iso': {
        'Title': '',
        'Xlabel': 'lepton rel. iso.',
        'Plot': plotoptions + ['logX'],
        'Branch': 'lepton_iso',
        'Expression': 'float x = -9; if(ntightMuons==1) {return tightMuons_pfRelIso04_all[0];} else {return x;}',
        'Histogram': {'varbins': numpy.geomspace(1e-4, 1, 31)},
    },

    'lepton_iso_cut': {
        'Title': '',
        'Xlabel': 'lepton rel. iso. (mtw>50 GeV)',
        'Plot': plotoptions + ['logX'],
        'Branch': 'lepton_iso_cut',
        'Expression': 'float x = -9; if(mtw_nominal>50 && ntightMuons==1) {return tightMuons_pfRelIso04_all[0];} else {return x;}',
        'Histogram': {'varbins': numpy.geomspace(1e-4, 1, 31)},
    },


    # Jets
    'n_jets': {
        'Title': '',
        'Xlabel': 'N_{jets}',
        'Plot': plotoptions,
        'Branch': 'nselectedJets_nominal',
        'Histogram': {'nbins': 7, 'xmin': 0, 'xmax': 7},
    },

    'jet_pt': {
        'Title': '',
        'Xlabel': 'selected Jet pt',
        'Plot': plotoptions + ['logX'],
        'Branch': 'selectedJets_nominal_pt',
        'Histogram': {'varbins': numpy.geomspace(20, 400, 31)},
    },

    'jet_eta': {
        'Title': '',
        'Xlabel': 'selected Jet eta',
        'Plot': plotoptions,
        'Branch': 'selectedJets_nominal_eta',
        'Histogram': {'nbins': 30, 'xmin': -4, 'xmax': 4},
    },

    # TODO add to NanoAODTools output
    #'jet_phi': {
        #'Title': '',
        #'Xlabel': 'selected Jet phi',
        #'Plot': plotoptions,
        #'Branch': 'selectedJets_nominal_phi',
        #'Histogram': {'nbins': 30, 'xmin': -numpy.pi, 'xmax': -numpy.pi},
    #},

     'n_bjets': {
        'Title': '',
        'Xlabel': 'N_{b-jets}',
        'Plot': plotoptions,
        'Branch': 'nselectedBJets_nominal',
        'Histogram': {'nbins': 4, 'xmin': 0, 'xmax': 4},
    },

    # b-Jets
    'bjet_pt': {
        'Title': '',
        'Xlabel': 'selected b-Jet pt',
        'Plot': plotoptions + ['logX'],
        'Branch': 'selectedBJets_nominal_pt',
        'Histogram': {'varbins': numpy.geomspace(20, 400, 31)},
    },

    'bjet_eta': {
        'Title': '',
        'Xlabel': 'selected b-Jet eta',
        'Plot': plotoptions,
        'Branch': 'selectedBJets_nominal_eta',
        'Histogram': {'nbins': 30, 'xmin': -3, 'xmax': 3},
    },

    # TODO add to NanoAODTools output
    #'bjet_phi': {
        #'Title': '',
        #'Xlabel': 'selected b-Jet phi',
        #'Plot': plotoptions,
        #'Branch': 'selectedBJets_nominal_phi',
        #'Histogram': {'nbins': 30, 'xmin': -numpy.pi, 'xmax': -numpy.pi},
    #},

    # 'n_muons': {
    #    'Title': '',
    #    'Xlabel': 'N_{b-jets}',
    #    'Plot': plotoptions,
    #    'Branch': 'ntightMuons',
    #    #'Expression': 'if(ntightMuons==1) {return tightMuons_pt[0];} else {return tightElectrons_pt[0];}',
    #    'Histogram': {'nbins': 4, 'xmin': 0, 'xmax': 4},
    #},

    # 'n_bjets_ttbar': {
    #    'Title': '',
    #    'Xlabel': 'N_{b-jets}',
    #    'Plot': plotoptions,
    #    'Branch': 'nselectedBJets_nominal',
    #    'Filter': '(nselectedBJets_nominal == 2 && nselectedJets_nominal >= 3 && ntightMuons == 1)',
    #    'Histogram': {'nbins': 4, 'xmin': 0, 'xmax': 4},
    #},



    'top_mass': {
        'Title': '',
        'Xlabel': '$m_{t}$',
        'Plot': plotoptions,
        'Branch': 'top_mass_nominal',
        'Histogram': {'nbins': 100, 'xmin': 0, 'xmax': 800},
    },
    #
    #'top_pt': {
    #    'Title': '',
    #    'Xlabel': 'top pt',
    #    'Plot': plotoptions,
    #    'Branch': 'top_pt_nominal',
    #    'Histogram': {'nbins': 100, 'xmin': 0, 'xmax': 400},
    #},

    'met': {
        'Title': '',
        'Xlabel': 'MET',
        'Plot': plotoptions,
        'Branch': 'met_nominal',
        'Histogram': {'nbins': 30, 'xmin': 0, 'xmax': 250},
    },

    'mtw': {
        'Title': '',
        'Xlabel': 'MTW',
        'Plot': plotoptions,
        'Branch': 'mtw_nominal',
        'Histogram': {'nbins': 30, 'xmin': 0, 'xmax': 250},
    },


    'fitbins': {
        'Branch': 'fitBins',
        'Expression': 'int x = 0; \
            if(std::fabs(top_mass_nominal-172.5)<25.) x++; \
            if(ntightMuons==1) { if(tightMuons_charge[0]>0) x += 2; } else { if(tightElectrons_charge[0]>0) x += 2; } \
            return x;',
        'Histogram': {'nbins': 4, 'xmin': -0.5, 'xmax': 3.5},
        'Title': 'Fit bins',
        'Xlabel': 'category',
        'Plot': plotoptions,
    },
}
