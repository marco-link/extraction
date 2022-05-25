# -*- coding: utf-8 -*-

"""
Defines the names and properties of the MC datasets in signal, background and datasets dicts of dicts:

* dict key:         dataset name
* ``MC``:           bool, True for MC
* ``Signal``:       bool, True for signal
* ``FileName``:     root filename of dataset
* ``Label``:        plotlabel
* ``Color``:        plotcolor
* ``XS``:           cross section in pb
* ``XSUncertainty``: dict with ``Up`` and ``Down`` cross section uncertainty
* year name: dict containing year specific information:
    * ``KFactor``: correction factor
    * ``EventWeights``: event weights to apply for this dataset
"""

#cross section sources:
#[0] generator cross section: https://cms-gen-dev.cern.ch/xsdb/
#[1] ttbar NNLO: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO
#[2] WJets NNLO: https://indico.cern.ch/event/673253/contributions/2756806/attachments/1541203/2416962/20171016_VJetsXsecsUpdate_PH-GEN.pdf
#[3] DY + diboson: https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat13TeV
#[4] single top NLO: https://twiki.cern.ch/twiki/bin/view/LHCPhysics/SingleTopRefXsec
#[5] W boson BR: https://pdg.lbl.gov/2021/listings/rpp2021-list-w-boson.pdf



import os
import pandas


gen_json = pandas.read_json(os.path.abspath(os.path.dirname(__file__)) + '/xsecs.json')

gen_weights = ['genweight/genEventSumw', 'fragCP5BLVsPt']
me_weight = ['MEweight_murNominal_mufNominal']
pdf_weight = ['PDFweight_0']

weights_electron = ['tightElectrons_weight_reco_nominal', 'tightElectrons_weight_id_nominal']
weights_muon = ['tightMuons_weight_reco_nominal', 'tightMuons_weight_id_nominal', 'tightMuons_weight_iso_nominal']
weights_prefiring = ['L1PreFiringWeight_ECAL_Nom', 'L1PreFiringWeight_Muon_Nom']
weights_bjets = ['btagEventWeight_deepjet_shape_nominal']
weights_pileup = ['puWeight']

weights = weights_electron + weights_muon + weights_prefiring + weights_bjets + weights_pileup
weights_2016 = []
weights_2017 = ['IsoMuTrigger_weight_trigger_2017_nominal', 'IsoElectronTrigger_weight_trigger_2017_nominal']
weights_2018 = []


signal = {}
for index in gen_json.keys():
    signal['WbWbX_{}'.format(index)] = {
        'MC': True,
        'Signal': True,
        'Label': r'Wb x Wb',
        'FileName': 'WbjToLNu_4f_TuneCP5_13TeV-madgraph-pythia8',
        'Color': 'red',
        'XS': gen_json[index]['xsec'],
        'XSUncertainty': {
            'Up': 5, #TODO update
            'Down': 5, #TODO update
        },
        '2017': {
            'KFactor': 1.,
            'EventWeights': gen_weights + me_weight + pdf_weight + weights + weights_2017 + ['LHEWeights_width_{}'.format(index)],
        },
    }
# TODO cut option


background = {
    'ttbar_dilep': {
        'MC': True,
        'Signal': False,
        'FileName': 'TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8',
        'Label': r't$\bar{t}$ (dilep)',
        'Color': 'darkorange',
        'XS': 831.76 * (1 - 0.6741)**2, # [1]*[5]
        'XSUncertainty': {
            'Up': 50, #TODO update
            'Down': 50, #TODO update
        },
        '2017': {
            'KFactor': 1.,
            'EventWeights': gen_weights + me_weight + pdf_weight + weights + weights_2017,
        },
    },

    'ttbar_semilep': {
        'MC': True,
        'Signal': False,
        'FileName': 'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8',
        'Label': r't$\bar{t}$ (semilep)',
        'Color': 'gold',
        'XS': 831.76 * (0.6741 * (1 - 0.6741) * 2), # [1]*[5]
        'XSUncertainty': {
            'Up': 50, #TODO update
            'Down': 50, #TODO update
        },
        '2017': {
            'KFactor': 1.,
            'EventWeights': gen_weights + me_weight + pdf_weight + weights + weights_2017,
        },
    },

    'ttbar_had': {
        'MC': True,
        'Signal': False,
        'FileName': 'TTToHadronic_TuneCP5_13TeV-powheg-pythia8',
        'Label': r't$\bar{t}$ (had)',
        'Color': 'yellow',
        'XS': 831.76 * 0.6741**2, # [1]*[5]
        'XSUncertainty': {
            'Up': 50, #TODO update
            'Down': 50, #TODO update
        },
        '2017': {
            'KFactor': 1.,
            'EventWeights': gen_weights + me_weight + pdf_weight + weights + weights_2017,
        },
    },

    'WJets_0j': {
        'MC': True,
        'Signal': False,
        'FileName': 'WJetsToLNu_0J_TuneCP5_13TeV-amcatnloFXFX-pythia8',
        'Label': 'W+Jets (0j)',
        'Color': 'limegreen',
        'XS': 50131.98259, #[2]
        'XSUncertainty': {
            'Up': 50, #TODO update
            'Down': 50, #TODO update
        },
        '2017': {
            'KFactor': 1.,
            'EventWeights': gen_weights + me_weight + pdf_weight + weights + weights_2017,
        },
    },

    'WJets_1j': {
        'MC': True,
        'Signal': False,
        'FileName': 'WJetsToLNu_1J_TuneCP5_13TeV-amcatnloFXFX-pythia8',
        'Label': 'W+Jets (1j)',
        'Color': 'forestgreen',
        'XS': 8875.0, #[2]
        'XSUncertainty': {
            'Up': 50, #TODO update
            'Down': 50, #TODO update
        },
        '2017': {
            'KFactor': 1.,
            'EventWeights': gen_weights + me_weight + pdf_weight + weights + weights_2017,
        },
    },

    'WJets_2j': {
        'MC': True,
        'Signal': False,
        'FileName': 'WJetsToLNu_2J_TuneCP5_13TeV-amcatnloFXFX-pythia8',
        'Label': 'W+Jets (2j)',
        'Color': 'green',
        'XS': 3172.958208, #[2]
        'XSUncertainty': {
            'Up': 50, #TODO update
            'Down': 50, #TODO update
        },
        '2017': {
            'KFactor': 1.,
            'EventWeights': gen_weights + me_weight + pdf_weight + weights + weights_2017,
        },
    },

    'DY': {
        'MC': True,
        'Signal': False,
        'FileName': 'DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8',
        'Label': 'Drell Yan',
        'Color': 'aqua',
        'XS': 6529.0, #[0]
        'XSUncertainty': {
            'Up': 50, #TODO update
            'Down': 50, #TODO update
        },
        '2017': {
            'KFactor': 1.,
            'EventWeights': gen_weights + weights + weights_2017,
        },
    },

    'WW': {
        'MC': True,
        'Signal': False,
        'FileName': 'WW_TuneCP5_13TeV-pythia8',
        'Label': 'diboson (WW)',
        'Color': 'cornflowerblue',
        'XS': 75.8, #[0]
        'XSUncertainty': {
            'Up': 50, #TODO update
            'Down': 50, #TODO update
        },
        '2017': {
            'KFactor': 1.,
            'EventWeights': gen_weights + weights + weights_2017,
        },
    },

    'WZ': {
        'MC': True,
        'Signal': False,
        'Label': 'diboson (WZ)',
        'FileName': 'WZ_TuneCP5_13TeV-pythia8',
        'Color': 'royalblue',
        'XS': 27.6, #[0]
        'XSUncertainty': {
            'Up': 50, #TODO update
            'Down': 50, #TODO update
        },
        '2017': {
            'KFactor': 1.,
            'EventWeights': gen_weights + weights + weights_2017,
        },
    },

    'ZZ': {
        'MC': True,
        'Signal': False,
        'Label': 'diboson (ZZ)',
        'FileName': 'ZZ_TuneCP5_13TeV-pythia8',
        'Color': 'deepskyblue',
        'XS': 12.14, #[0]
        'XSUncertainty': {
            'Up': 50, #TODO update
            'Down': 50, #TODO update
        },
        '2017': {
            'KFactor': 1.,
            'EventWeights': gen_weights + weights + weights_2017,
        },
    },

    #TODO check included in signal
    #'ST_t_top': {
        #'MC': True,
        #'Signal': False,
        #'FileName': 'ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8',
        #'Label': 'WW',
        #'Color': 'indigo',
        #'XS': 136.02, #[4]
        #'XSUncertainty': {
            #'Up': 50, #TODO update
            #'Down': 50, #TODO update
        #},
        #'2017': {
            #'KFactor': 1.,
            #'EventWeights': gen_weights + me_weight + weights + weights_2017,
        #},
    #},

    #'ST_t_anti': {
        #'MC': True,
        #'Signal': False,
        #'FileName': 'ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8',
        #'Label': 'WW',
        #'Color': 'rebeccapurple',
        #'XS': 80.95, #[4]
        #'XSUncertainty': {
            #'Up': 50, #TODO update
            #'Down': 50, #TODO update
        #},
        #'2017': {
            #'KFactor': 1.,
            #'EventWeights': gen_weights + me_weight + weights + weights_2017,
        #},
    #},

    #'ST_tW_top': {
        #'MC': True,
        #'Signal': False,
        #'FileName': 'ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8',
        #'Label': 'WW',
        #'Color': 'darkorchid',
        #'XS': 71.7 * 0.5, #[4]
        #'XSUncertainty': {
            #'Up': 50, #TODO update
            #'Down': 50, #TODO update
        #},
        #'2017': {
            #'KFactor': 1.,
            #'EventWeights': gen_weights + me_weight + weights + weights_2017,
        #},
    #},

    #'ST_tW_antitop': {
        #'MC': True,
        #'Signal': False,
        #'FileName': 'ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8',
        #'Label': 'WW',
        #'Color': 'darkviolet',
        #'XS': 71.7 * 0.5, #[4]
        #'XSUncertainty': {
            #'Up': 50, #TODO update
            #'Down': 50, #TODO update
        #},
        #'2017': {
            #'KFactor': 1.,
            #'EventWeights': gen_weights + me_weight + weights + weights_2017,
        #},
    #},

    #'ST_s': {
        #'MC': True,
        #'Signal': False,
        #'FileName': 'ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8',
        #'Label': 'single t (s channel)',
        #'Color': 'purple',
        #'XS': 10.32 , #[4]
        #'XSUncertainty': {
            #'Up': 50, #TODO update
            #'Down': 50, #TODO update
        #},
        #'2017': {
            #'KFactor': 1.,
            #'EventWeights': gen_weights + me_weight + weights + weights_2017,
        #},
    #},

}


datasets = signal.copy()
datasets.update(background)
