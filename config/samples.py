# -*- coding: utf-8 -*-

"""
Defines the names and properties of the MC samples in signal, background and samples dicts of dicts:

* dict key:         sample name
* ``MC``:           bool, True for MC
* ``Signal``:       bool, True for signal
* ``Label``:        plotlabel
* ``Color``:        plotcolor
* ``XS``:           cross section in pb
* ``XSUncertainty``: dict with ``Up`` and ``Down`` cross section uncertainty
* year name: dict containing year specific information:
    * ``KFactor``: correction factor
    * ``Entries``: number of simulated events
    * ``FileName``: root filename of sample
    * ``EventWeights``: event weights to apply in this sample
"""







import os
import pandas

#from config.data import data # TODO

gen_json = pandas.read_json(os.path.abspath(os.path.dirname(__file__)) + '/xsecs.json')
gen_weight = [] #TODO check width weight

weights_electron = []
weights_muon = ['tightMuons_weight_id_nominal', 'tightMuons_weight_iso_nominal']
weights_bjets = []

weights = weights_electron + weights_muon + weights_bjets
weights_2016 = []
weights_2017 = []
weights_2018 = []

weights = [] #TODO implement weights


signal = {}
for index in gen_json.keys():
    signal['WbWbX_{}'.format(index)] = {
        'MC': True,
        'Signal': True,
        'Label': r'Wb x Wb $m_t = {}$ GeV, $\Gamma_t = {}$ GeV'.format(gen_json[index]['mass'], gen_json[index]['width']),
        'Color': 'C1',
        'XS': gen_json[index]['xsec'],
        'XSUncertainty': {
            'Up': 5, #TODO update
            'Down': 5, #TODO update
        },
        '2016': {
            'KFactor': 1.,#TODO update
            'Entries': 1000, #TODO update
            'FileName': 'WbjToLNu_4f',
            'EventWeights': gen_weight + weights + weights_2016 + ['LHEWeights_width_{}'.format(index)],
        },
    }



background = {
    #'TT_Semileptonic': {
        #'MC': True,
        #'Signal': False,
        #'Label': 'tt',
        #'Color': 'C1',
        #'XS': 800, #TODO update
        #'XSUncertainty': {
            #'Up': 50, #TODO update
            #'Down': 50, #TODO update
        #},
        #'2016': {
            #'KFactor': 1.00764138624,#TODO update
            #'Entries': 106166400, #TODO update
            #'FileName': 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_WbWbX',
            #'EventWeights': gen_weight + weights + weights_2016,
        #},
    #},


    'testbg_1': {
        'MC': True,
        'Signal': False,
        'Label': 'test1',
        'Color': 'C1',
        'XS': 800, #TODO update
        'XSUncertainty': {
            'Up': 50, #TODO update
            'Down': 50, #TODO update
        },
        '2016': {
            'KFactor': 1.,#TODO update
            'Entries': 1000, #TODO update
            'FileName': 'DYJetsToLL_M-5',
            'EventWeights': gen_weight + weights + weights_2016,
        },
    },

    'testbg_2': {
        'MC': True,
        'Signal': False,
        'Label': 'test2',
        'Color': 'C2',
        'XS': 900, #TODO update
        'XSUncertainty': {
            'Up': 50, #TODO update
            'Down': 50, #TODO update
        },
        '2016': {
            'KFactor': 1.,#TODO update
            'Entries': 1000, #TODO update
            'FileName': 'DYJetsToLL_M-10to50',
            'EventWeights': gen_weight + weights + weights_2016,
        },
    },

}


samples = signal.copy()
samples.update(background)
