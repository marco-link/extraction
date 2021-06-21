# -*- coding: utf-8 -*-

#from config.data import data

gen_weight = ['genweight'] #TODO check width weight

weights_electron = []
weights_muon = ['tightMuons_weight_id_nominal', 'tightMuons_weight_iso_nominal']
weights_bjets = []

weights = weights_electron + weights_muon + weights_bjets
weights_2016 = []
weights_2017 = []
weights_2018 = []



signal = {

    #'data': data,

    'WbWbX_onshell': {
        'MC': True,
        'Signal': True,
        'Label': 'Wb x Wb onshell',
        'Color': 'C0',
        'XS': 51.7, #TODO update
        'XSUncertainty': {
            'Up': 5, #TODO update
            'Down': 5, #TODO update
        },
        'Efficiency': 0.43923, #TODO update
        '2016': {
            'KFactor': 1.00764138624,#TODO update
            'Entries': 106166400, #TODO update
            'FileName': 'ST_4f_w_lo_WbWbX',
            'EventWeights': gen_weight + weights + weights_2016 + ['LHEWeights_width_2', 'Reco_Wb_onshell'],
        },
    },

    'WbWbX_offshell': {
        'MC': True,
        'Signal': True,
        'Label': 'Wb x Wb offshell',
        'Color': 'C2',
        'XS': 51.7, #TODO update
        'XSUncertainty': {
            'Up': 5, #TODO update
            'Down': 5, #TODO update
        },
        'Efficiency': 0.43923, #TODO update
        '2016': {
            'KFactor': 1.00764138624,#TODO update
            'Entries': 106166400, #TODO update
            'FileName': 'ST_4f_w_lo_WbWbX',
            'EventWeights': gen_weight + weights + weights_2016 + ['LHEWeights_width_2', '(1-Reco_Wb_onshell)'],
        },
    },




    'WbWbX_2': {
        'MC': True,
        'Signal': True,
        'Label': 'Wb x Wb',
        'Color': 'C0',
        'XS': 51.7, #TODO update
        'XSUncertainty': {
            'Up': 5, #TODO update
            'Down': 5, #TODO update
        },
        'Efficiency': 0.43923, #TODO update
        '2016': {
            'KFactor': 1.00764138624,#TODO update
            'Entries': 106166400, #TODO update
            'FileName': 'ST_4f_w_lo_WbWbX',
            'EventWeights': gen_weight + weights + weights_2016 + ['LHEWeights_width_2'],
        },
    },

    'WbWbX_3': {
        'MC': True,
        'Signal': True,
        'Label': 'Wb x Wb',
        'Color': 'C0',
        'XS': 51.7, #TODO update
        'XSUncertainty': {
            'Up': 5, #TODO update
            'Down': 5, #TODO update
        },
        'Efficiency': 0.43923, #TODO update
        '2016': {
            'KFactor': 1.00764138624,#TODO update
            'Entries': 106166400, #TODO update
            'FileName': 'ST_4f_w_lo_WbWbX',
            'EventWeights': gen_weight + weights + weights_2016 + ['LHEWeights_width_3'],
        },
    },
}










background = {
    'TT_Semileptonic': {
        'MC': True,
        'Signal': False,
        'Label': 'tt',
        'Color': 'C1',
        'XS': 800, #TODO update
        'XSUncertainty': {
            'Up': 50, #TODO update
            'Down': 50, #TODO update
        },
        'Efficiency': 0.43923, #TODO update
        '2016': {
            'KFactor': 1.00764138624,#TODO update
            'Entries': 106166400, #TODO update
            'FileName': 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_WbWbX',
            'EventWeights': gen_weight + weights + weights_2016,
        },
    },













  #'TTToSemilepton': {
    #'MC': True,
    #'TT': True,
    #'Name': 'TT Semilep',
    #'Color': 'KITgreen100',
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets',  'muons', 'ttonly'],
    #'XS': 831.76,
    #'XSUncertainty': {
      #'Up': 40.24,
      #'Down': 45.62,
    #},
    #'Efficiency': 0.43923,
    #'2016': {
      #'KFactor': 1.00764138624,
      #'Entries': 106166400,
      #'FileName': 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8',
      #'GridPath': '/work/jrauser/frameworks/cmssw/napalm/CMSSW_10_6_2/src/napalm/trees/test/TTToSemilep16_NANOAOD_v7_Skim.root', # Testing
      ## 'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight, toppTWeight],
    #},
    #'2017': {
      #'KFactor': 1.00784894337,
      #'Entries': 109663792,
      #'FileName': 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8',
      #'GridPath': '/work/jrauser/frameworks/cmssw/napalm/CMSSW_10_6_2/src/napalm/trees/test/TTToSemilep17_NANOAOD_v7_Skim.root', # Testing
      ## 'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight, toppTWeight],
    #},
    #'2018': {
      #'KFactor': 1.00775806249,
      #'Entries': 300619998,
      #'FileName': 'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8',
      #'GridPath': '/work/jrauser/frameworks/cmssw/napalm/CMSSW_10_6_2/src/napalm/trees/test/TTToSemilep18_NANOAOD_v7_Skim.root', # Testing
      ## 'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, toppTWeight],
    #},
  #},
  #'TTToSemileptonBoosted': {
    #'MC': True,
    #'TT': True,
    #'Name': 'TT Semilep Boosted',
    #'Color': 'KITgreen100',
    #'XS': 831.76,
    #'XSUncertainty': {
      #'Up': 40.24,
      #'Down': 45.62,
    #},
    #'Efficiency': 0.43923,
    #'2016': {
      #'KFactor': 1.00764138624,
      #'Entries': 106166400,
      #'FileName': 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_boosted',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight, toppTWeight],
    #},
    #'2017': {
      #'KFactor': 1.00784894337,
      #'Entries': 109663792,
      #'FileName': 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_boosted',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.00775806249,
      #'Entries': 300619998,
      #'FileName': 'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_boosted',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight],
    #},
  #},
  #'TTToSemileptonResolved': {
    #'MC': True,
    #'TT': True,
    #'Name': '#splitline{TT Semilep }{Resolved}',
    #'Color': 'KITgreen100',
    #'XS': 831.76,
    #'XSUncertainty': {
      #'Up': 40.24,
      #'Down': 45.62,
    #},
    #'Efficiency': 0.43923,
    #'2016': {
      #'KFactor': 1.00764138624,
      #'Entries': 106166400,
      #'FileName': 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_resolved',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.00784894337,
      #'Entries': 109663792,
      #'FileName': 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_resolved',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.00775806249,
      #'Entries': 300619998,
      #'FileName': 'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_resolved',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight],
    #},
  #},
  #'TTToSemileptonCorrect': {
    #'MC': True,
    #'TT': True,
    #'Name': 'TT Semilep Correct',
    #'Color': 'KITgreen100',
    #'XS': 831.76,
    #'XSUncertainty': {
      #'Up': 40.24,
      #'Down': 45.62,
    #},
    #'Efficiency': 0.43923,
    #'2016': {
      #'KFactor': 1.00764138624,
      #'Entries': 106166400,
      #'FileName': 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_correct',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.00784894337,
      #'Entries': 109663792,
      #'FileName': 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_correct',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.00775806249,
      #'Entries': 300619998,
      #'FileName': 'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_correct',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight],
    #},
  #},
  #'TTToSemileptonWrong': {
    #'MC': True,
    #'TT': True,
    #'Name': 'TT Semilep Wrong',
    #'Color': 'KITgreen100',
    #'XS': 831.76,
    #'XSUncertainty': {
      #'Up': 40.24,
      #'Down': 45.62,
    #},
    #'Efficiency': 0.43923,
    #'2016': {
      #'KFactor': 1.00764138624,
      #'Entries': 106166400,
      #'FileName': 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_wrong',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.00784894337,
      #'Entries': 109663792,
      #'FileName': 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_wrong',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.00775806249,
      #'Entries': 300619998,
      #'FileName': 'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_wrong',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight],
    #},
  #},
  #'TTToSemileptonGenBoosted': {
    #'MC': True,
    #'TT': True,
    #'Name': 'TT Semilep Gen Boosted',
    #'Color': 'KITgreen100',
    #'XS': 831.76,
    #'XSUncertainty': {
      #'Up': 40.24,
      #'Down': 45.62,
    #},
    #'Efficiency': 0.43923,
    #'2016': {
      #'KFactor': 1.00764138624,
      #'Entries': 106166400,
      #'FileName': 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_genboosted',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.00784894337,
      #'Entries': 109663792,
      #'FileName': 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_genboosted',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.00775806249,
      #'Entries': 300619998,
      #'FileName': 'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_genboosted',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight],
    #},
  #},
  #'TTToSemileptonGenResolved': {
    #'MC': True,
    #'TT': True,
    #'Name': 'TT Semilep Gen Resolved',
    #'Color': 'KITgreen100',
    #'XS': 831.76,
    #'XSUncertainty': {
      #'Up': 40.24,
      #'Down': 45.62,
    #},
    #'Efficiency': 0.43923,
    #'2016': {
      #'KFactor': 1.00764138624,
      #'Entries': 106166400,
      #'FileName': 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_genresolved',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.00784894337,
      #'Entries': 109663792,
      #'FileName': 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_genresolved',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.00775806249,
      #'Entries': 300619998,
      #'FileName': 'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_genresolved',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight],
    #},
  #},
  #'TTToSemileptonGenPartonic': {
    #'MC': True,
    #'TT': True,
    #'Name': 'TT Semilep Gen Partonic',
    #'Color': 'KITgreen100',
    #'XS': 831.76,
    #'XSUncertainty': {
      #'Up': 40.24,
      #'Down': 45.62,
    #},
    #'Efficiency': 0.43923,
    #'2016': {
      #'KFactor': 1.00764138624,
      #'Entries': 106166400,
      #'FileName': 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_genpartonic',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.00784894337,
      #'Entries': 109663792,
      #'FileName': 'TTToSemiLeptonic_TuneCP5_PSweights_13TeV-powheg-pythia8_genpartonic',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.00775806249,
      #'Entries': 300619998,
      #'FileName': 'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_genpartonic',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight],
    #},
  #},
  #'TTToSemileptonHT250': {
    #'MC': True,
    #'TT': True,
    #'Name': 'TT Semilep HT 250',
    #'Color': 'KITblue100',
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets',  'muons', 'ttonly'],
    #'XS': 78.83,
    #'XSUncertainty': {
      #'Up': 3.81,
      #'Down': 4.32,
    #},
    #'Efficiency': 0.43923,
    #'2016': {
      #'KFactor': 1.01929625871,
      #'Entries': 28403407,
      #'FileName': 'TTToSemiLeptonic_AK8HT250_TuneCP5_PSweights_13TeV-powheg-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/TTToSemiLeptonic_AK8HT250_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight, toppTWeight],
    #},
    #'2017': {
      #'KFactor': 1.01937161286,
      #'Entries': 28357449,
      #'FileName': 'TTToSemiLeptonic_AK8HT250_TuneCP5_PSweights_13TeV-powheg-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/TTToSemiLeptonic_AK8HT250_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight, toppTWeight],
    #},
    #'2018': {
      #'KFactor': 1.01929038314,
      #'Entries': 22476261,
      #'FileName': 'TTToSemiLeptonic_AK8HT250_TuneCP5_13TeV-powheg-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/TTToSemiLeptonic_AK8HT250_TuneCP5_13TeV-powheg-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, toppTWeight],
    #},
  #},
  #'TTToSemileptonHT250Boosted': {
    #'MC': True,
    #'TT': True,
    #'Name': '#splitline{TT Semilep }{HT 250 Boosted}',
    #'Color': 'KITblue100',
    #'XS': 78.83,
    #'XSUncertainty': {
      #'Up': 3.81,
      #'Down': 4.32,
    #},
    #'Efficiency': 0.43923,
    #'2016': {
      #'KFactor': 1.01929625871,
      #'Entries': 28403407,
      #'FileName': 'TTToSemiLeptonic_AK8HT250_TuneCP5_PSweights_13TeV-powheg-pythia8_boosted',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.01937161286,
      #'Entries': 28357449,
      #'FileName': 'TTToSemiLeptonic_AK8HT250_TuneCP5_PSweights_13TeV-powheg-pythia8_boosted',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.01929038314,
      #'Entries': 22476261,
      #'FileName': 'TTToSemiLeptonic_AK8HT250_TuneCP5_13TeV-powheg-pythia8_boosted',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight],
    #},
  #},
  #'TTToSemileptonHT250Resolved': {
    #'MC': True,
    #'TT': True,
    #'Name': 'TT Semilep HT 250 Resolved',
    #'Color': 'KITblue100',
    #'XS': 78.83,
    #'XSUncertainty': {
      #'Up': 3.81,
      #'Down': 4.32,
    #},
    #'Efficiency': 0.43923,
    #'2016': {
      #'KFactor': 1.01929625871,
      #'Entries': 28403407,
      #'FileName': 'TTToSemiLeptonic_AK8HT250_TuneCP5_PSweights_13TeV-powheg-pythia8_resolved',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.01937161286,
      #'Entries': 28357449,
      #'FileName': 'TTToSemiLeptonic_AK8HT250_TuneCP5_PSweights_13TeV-powheg-pythia8_resolved',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.01929038314,
      #'Entries': 22476261,
      #'FileName': 'TTToSemiLeptonic_AK8HT250_TuneCP5_13TeV-powheg-pythia8_resolved',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight],
    #},
  #},
  #'TTToSemileptonHT250Correct': {
    #'MC': True,
    #'TT': True,
    #'Name': 'TT Semilep HT 250 Correct',
    #'Color': 'KITblue100',
    #'XS': 78.83,
    #'XSUncertainty': {
      #'Up': 3.81,
      #'Down': 4.32,
    #},
    #'Efficiency': 0.43923,
    #'2016': {
      #'KFactor': 1.01929625871,
      #'Entries': 28403407,
      #'FileName': 'TTToSemiLeptonic_AK8HT250_TuneCP5_PSweights_13TeV-powheg-pythia8_correct',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.01937161286,
      #'Entries': 28357449,
      #'FileName': 'TTToSemiLeptonic_AK8HT250_TuneCP5_PSweights_13TeV-powheg-pythia8_correct',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.01929038314,
      #'Entries': 22476261,
      #'FileName': 'TTToSemiLeptonic_AK8HT250_TuneCP5_13TeV-powheg-pythia8_correct',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight],
    #},
  #},
  #'TTToSemileptonHT250Wrong': {
    #'MC': True,
    #'TT': True,
    #'Name': 'TT Semilep HT 250 Wrong',
    #'Color': 'KITblue100',
    #'XS': 78.83,
    #'XSUncertainty': {
      #'Up': 3.81,
      #'Down': 4.32,
    #},
    #'Efficiency': 0.43923,
    #'2016': {
      #'KFactor': 1.01929625871,
      #'Entries': 28403407,
      #'FileName': 'TTToSemiLeptonic_AK8HT250_TuneCP5_PSweights_13TeV-powheg-pythia8_wrong',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.01937161286,
      #'Entries': 28357449,
      #'FileName': 'TTToSemiLeptonic_AK8HT250_TuneCP5_PSweights_13TeV-powheg-pythia8_wrong',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.01929038314,
      #'Entries': 22476261,
      #'FileName': 'TTToSemiLeptonic_AK8HT250_TuneCP5_13TeV-powheg-pythia8_wrong',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight],
    #},
  #},
  #'TTToSemileptonHT250GenBoosted': {
    #'MC': True,
    #'TT': True,
    #'Name': 'TT Semilep HT 250 Gen Boosted',
    #'Color': 'KITblue100',
    #'XS': 78.83,
    #'XSUncertainty': {
      #'Up': 3.81,
      #'Down': 4.32,
    #},
    #'Efficiency': 0.43923,
    #'2016': {
      #'KFactor': 1.01929625871,
      #'Entries': 28403407,
      #'FileName': 'TTToSemiLeptonic_AK8HT250_TuneCP5_PSweights_13TeV-powheg-pythia8_genboosted',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.01937161286,
      #'Entries': 28357449,
      #'FileName': 'TTToSemiLeptonic_AK8HT250_TuneCP5_PSweights_13TeV-powheg-pythia8_genboosted',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.01929038314,
      #'Entries': 22476261,
      #'FileName': 'TTToSemiLeptonic_AK8HT250_TuneCP5_13TeV-powheg-pythia8_genboosted',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight],
    #},
  #},
  #'TTToSemileptonHT250GenResolved': {
    #'MC': True,
    #'TT': True,
    #'Name': 'TT Semilep HT 250 Gen Resolved',
    #'Color': 'KITblue100',
    #'XS': 78.83,
    #'XSUncertainty': {
      #'Up': 3.81,
      #'Down': 4.32,
    #},
    #'Efficiency': 0.43923,
    #'2016': {
      #'KFactor': 1.01929625871,
      #'Entries': 28403407,
      #'FileName': 'TTToSemiLeptonic_AK8HT250_TuneCP5_PSweights_13TeV-powheg-pythia8_genresolved',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.01937161286,
      #'Entries': 28357449,
      #'FileName': 'TTToSemiLeptonic_AK8HT250_TuneCP5_PSweights_13TeV-powheg-pythia8_genresolved',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.01929038314,
      #'Entries': 22476261,
      #'FileName': 'TTToSemiLeptonic_AK8HT250_TuneCP5_13TeV-powheg-pythia8_genresolved',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight],
    #},
  #},
  #'TTToSemileptonHT250GenPartonic': {
    #'MC': True,
    #'TT': True,
    #'Name': 'TT Semilep HT 250 Gen Partonic',
    #'Color': 'KITblue100',
    #'XS': 78.83,
    #'XSUncertainty': {
      #'Up': 3.81,
      #'Down': 4.32,
    #},
    #'Efficiency': 0.43923,
    #'2016': {
      #'KFactor': 1.01929625871,
      #'Entries': 28403407,
      #'FileName': 'TTToSemiLeptonic_AK8HT250_TuneCP5_PSweights_13TeV-powheg-pythia8_genpartonic',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.01937161286,
      #'Entries': 28357449,
      #'FileName': 'TTToSemiLeptonic_AK8HT250_TuneCP5_PSweights_13TeV-powheg-pythia8_genpartonic',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.01929038314,
      #'Entries': 22476261,
      #'FileName': 'TTToSemiLeptonic_AK8HT250_TuneCP5_13TeV-powheg-pythia8_genpartonic',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight],
    #},
  #},
  #'TTToSemileptonHT250NoGen': {
    #'MC': True,
    #'TT': True,
    #'Name': 'TT Semilep HT 250 No Gen',
    #'Color': 'KITblue100',
    #'XS': 78.83,
    #'XSUncertainty': {
      #'Up': 3.81,
      #'Down': 4.32,
    #},
    #'Efficiency': 0.43923,
    #'2016': {
      #'KFactor': 1.01929625871,
      #'Entries': 28403407,
      #'FileName': 'TTToSemiLeptonic_AK8HT250_TuneCP5_PSweights_13TeV-powheg-pythia8_nogen',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.01937161286,
      #'Entries': 28357449,
      #'FileName': 'TTToSemiLeptonic_AK8HT250_TuneCP5_PSweights_13TeV-powheg-pythia8_nogen',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.01929038314,
      #'Entries': 22476261,
      #'FileName': 'TTToSemiLeptonic_AK8HT250_TuneCP5_13TeV-powheg-pythia8_nogen',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toppTWeight, toptagWeight],
    #},
  #},
  #'TTToHadronic': {
    #'MC': True,
    #'TT': False,
    #'Name': 'TT Hadronic',
    #'Color': 850,
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets', 'muons', 'ttonly'],
    #'XS': 831.76,
    #'XSUncertainty': {
      #'Up': 40.24,
      #'Down': 45.62,
    #},
    #'Efficiency': 0.45469,
    #'2016': {
      #'KFactor': 1.00975884395,
      #'Entries': 68302800,
      #'FileName': 'TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight, toppTWeight],
    #},
    #'2017': {
      #'KFactor': 1.0094795342,
      #'Entries': 128829950,
      #'FileName': 'TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/TTToHadronic_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight, toppTWeight],
    #},
    #'2018': {
      #'KFactor': 1.00898229037,
      #'Entries': 327396000,
      #'FileName': 'TTToHadronic_TuneCP5_13TeV-powheg-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/TTToHadronic_TuneCP5_13TeV-powheg-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, toppTWeight],
    #},
  #},
  #'TTTo2L2Nu': {
    #'MC': True,
    #'TT': False,
    #'Name': 'TT Dilep',
    #'Color': 860,
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets', 'muons', 'ttonly'],
    #'XS': 831.76,
    #'XSUncertainty': {
      #'Up': 40.24,
      #'Down': 45.62,
    #},
    #'Efficiency': 0.10608,
    #'2016': {
      #'KFactor': 1.00764633228,
      #'Entries': 67860400,
      #'FileName': 'TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight, toppTWeight],
    #},
    #'2017': {
      #'KFactor': 1.00783277091,
      #'Entries': 68812194,
      #'FileName': 'TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/TTTo2L2Nu_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight, toppTWeight],
    #},
    #'2018': {
      #'KFactor': 1.00774763338,
      #'Entries': 44645000,
      #'FileName': 'TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, toppTWeight],
    #},
  #},
  #'ST_t-channel_antitop': {
    #'MC': True,
    #'TT': False,
    #'Name': 'Single Top (Antitop)',
    #'Color': 633,
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets', 'muons'],
    #'XS': 80.95,
    #'XSUncertainty': {
      #'Up': 4.06,
      #'Down': 3.61,
    #},
    #'Efficiency': 1.0,
    #'2016': {
      #'KFactor': 1.0,
      #'Entries': 17780700,
      #'FileName': 'ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.0,
      #'Entries': 64761200,
      #'FileName': 'ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.0,
      #'Entries': 79090800,
      #'FileName': 'ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight],
    #},
  #},
  #'ST_t-channel_top': {
    #'MC': True,
    #'TT': False,
    #'Name': 'Single Top (Top)',
    #'Color': 634,
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets', 'muons'],
    #'XS': 136.02,
    #'XSUncertainty': {
      #'Up': 5.40,
      #'Down': 4.57,
    #},
    #'Efficiency': 1.0,
    #'2016': {
      #'KFactor': 1.0,
      #'Entries': 31848000,
      #'FileName': 'ST_t-channel_top_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.0,
      #'Entries': 122688200,
      #'FileName': 'ST_t-channel_top_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.0,
      #'Entries': 154307600,
      #'FileName': 'ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight],
    #},
  #},
  #'ST_tW_antitop': {
    #'MC': True,
    #'TT': False,
    #'Name': 'Single Top (Antitop)',
    #'Color': 635,
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets', 'muons'],
    #'XS': 35.85,
    #'XSUncertainty': {
      #'Up': 3.84,
      #'Down': 3.84,
    #},
    #'Efficiency': 0.5454,
    #'2016': {
      #'KFactor': 1.0,
      #'Entries': 2712006,
      #'FileName': 'ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV_PSweights-powheg-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/ST_tW_antitop_5f_NoFullyHadronicDecays_13TeV_PSweights-powheg-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.00802066335,
      #'Entries': 5577319,
      #'FileName': 'ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_PSweights_13TeV-powheg-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.00478540486,
      #'Entries': 5823328,
      #'FileName': 'ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/ST_tW_antitop_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight],
    #},
  #},
  #'ST_tW_top': {
    #'MC': True,
    #'TT': False,
    #'Name': 'Single Top (Top)',
    #'Color': 636,
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets', 'muons'],
    #'XS': 35.85,
    #'XSUncertainty': {
      #'Up': 3.84,
      #'Down': 3.84,
    #},
    #'Efficiency': 0.5454,
    #'2016': {
      #'KFactor': 1.0,
      #'Entries': 3214709,
      #'FileName': 'ST_tW_top_5f_NoFullyHadronicDecays_13TeV_PSweights-powheg-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/ST_tW_top_5f_NoFullyHadronicDecays_13TeV_PSweights-powheg-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.00809136151,
      #'Entries': 5103599,
      #'FileName': 'ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_PSweights_13TeV-powheg-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_PSweights_13TeV-powheg-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.00464255946,
      #'Entries': 7636887,
      #'FileName': 'ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/ST_tW_top_5f_NoFullyHadronicDecays_TuneCP5_13TeV-powheg-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight],
    #},
  #},
  #'DYJetsToLL': {
    #'MC': True,
    #'TT': False,
    #'Name': 'DY Jets',
    #'Color': 413,
    #'PlotGroup': 'dyjets',
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets', 'muons'],
    #'XS': 5765.4,
    #'XSUncertainty': {
      #'Up': 288.27, # estimated 5%
      #'Down': 288.27, # estimated 5%
    #},
    #'Efficiency': 1.0,
    #'2016': {
      #'KFactor': 1.51339731918,
      #'Entries': 120777245,
      #'FileName': 'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.85906139218,
      #'Entries': 5189271,
      #'FileName': 'DYJetsToLL_M-50_VBFFilter_TuneCP5_PSweights_13TeV-amcatnloFXFX-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/DYJetsToLL_M-50_VBFFilter_TuneCP5_PSweights_13TeV-amcatnloFXFX-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.49595318288,
      #'Entries': 997561, #FIXME Why so few events?
      #'FileName': 'DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight],
    #},
    ## '2018': {
    ##   'KFactor': 1.47559,
    ##   'Entries': 193094040,
    ##   'FileName': 'DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8',
    ##   'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8.root',
    ##   'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight],
    ## },
  #},
  #'WToLNu_50To100': {
    #'MC': True,
    #'TT': False,
    #'Name': 'W Jets 50-100',
    #'Color': 400,
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets', 'muons'],
    #'XS': 3298.373338,
    #'XSUncertainty': {
      #'Up': 164.91, # estimated 5%
      #'Down': 164.91, # estimated 5%
    #},
    #'Efficiency': 1.0,
    #'2016': {
      #'KFactor': 0.000001, #TODO 2016
      #'Entries': 18242254, #TODO 2016
      #'FileName': 'WJetsToLNu_Pt-50To100_TuneCP5_13TeV-amcatnloFXFX-pythia8',#TODO 2016
      #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/WJetsToLNu_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root',#TODO 2016
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 2.61464511324,
      #'Entries': 18184612,
      #'FileName': 'WJetsToLNu_Pt-50To100_TuneCP5_13TeV-amcatnloFXFX-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/WJetsToLNu_Pt-50To100_TuneCP5_13TeV-amcatnloFXFX-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 2.61950344449,
      #'Entries': 19671032,
      #'FileName': 'WJetsToLNu_Pt-50To100_TuneCP5_13TeV-amcatnloFXFX-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/WJetsToLNu_Pt-50To100_TuneCP5_13TeV-amcatnloFXFX-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight],
    #},
  #},
  #'WToLNu_100To250': {
    #'MC': True,
    #'TT': False,
    #'Name': 'W Jets 100-250',
    #'Color': 401,
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets', 'muons'],
    #'XS': 689.749632,
    #'XSUncertainty': {
      #'Up': 34.48, # estimated 5%
      #'Down': 34.48, # estimated 5%
    #},
    #'Efficiency': 1.0,
    #'2016': {
      #'KFactor': 2.69295049675,
      #'Entries': 110844684,
      #'FileName': 'WJetsToLNu_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/WJetsToLNu_Pt-100To250_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 2.634303072,
      #'Entries': 97109738,
      #'FileName': 'WJetsToLNu_Pt-100To250_TuneCP5_13TeV-amcatnloFXFX-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/WJetsToLNu_Pt-100To250_TuneCP5_13TeV-amcatnloFXFX-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 2.63702026559,
      #'Entries': 96540150,
      #'FileName': 'WJetsToLNu_Pt-100To250_TuneCP5_13TeV-amcatnloFXFX-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/WJetsToLNu_Pt-100To250_TuneCP5_13TeV-amcatnloFXFX-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight],
    #},
  #},
  #'WToLNu_250To400': {
    #'MC': True,
    #'TT': False,
    #'Name': 'W Jets 250-400',
    #'Color': 402,
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets', 'muons'],
    #'XS': 24.5069015,
    #'XSUncertainty': {
      #'Up': 1.22, # estimated 5%
      #'Down': 1.22, # estimated 5%
    #},
    #'Efficiency': 1.0,
    #'2016': {
      #'KFactor': 2.67901769448,
      #'Entries': 12022587,
      #'FileName': 'WJetsToLNu_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/WJetsToLNu_Pt-250To400_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 2.54884763327,
      #'Entries': 9488289,
      #'FileName': 'WJetsToLNu_Pt-250To400_TuneCP5_13TeV-amcatnloFXFX-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/WJetsToLNu_Pt-250To400_TuneCP5_13TeV-amcatnloFXFX-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 2.5515690335,
      #'Entries': 8216981,
      #'FileName': 'WJetsToLNu_Pt-250To400_TuneCP5_13TeV-amcatnloFXFX-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/WJetsToLNu_Pt-250To400_TuneCP5_13TeV-amcatnloFXFX-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight],
    #},
  #},
  #'WToLNu_400To600': {
    #'MC': True,
    #'TT': False,
    #'Name': 'W Jets 400-600',
    #'Color': 403,
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets', 'muons'],
    #'XS': 3.110130566,
    #'XSUncertainty': {
      #'Up': 0.155, # estimated 5%
      #'Down': 0.155, # estimated 5%
    #},
    #'Efficiency': 1.0,
    #'2016': {
      #'KFactor': 2.59847093474,
      #'Entries': 1939947,
      #'FileName': 'WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/WJetsToLNu_Pt-400To600_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 2.3960195288,
      #'Entries': 1948286,
      #'FileName': 'WJetsToLNu_Pt-400To600_TuneCP5_13TeV-amcatnloFXFX-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/WJetsToLNu_Pt-400To600_TuneCP5_13TeV-amcatnloFXFX-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 2.40205238298,
      #'Entries': 1967802,
      #'FileName': 'WJetsToLNu_Pt-400To600_TuneCP5_13TeV-amcatnloFXFX-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/WJetsToLNu_Pt-400To600_TuneCP5_13TeV-amcatnloFXFX-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight],
    #},
  #},
  #'WToLNu_600ToInf': {
    #'MC': True,
    #'TT': False,
    #'Name': 'W Jets 600-Inf',
    #'Color': 404,
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets', 'muons'],
    #'XS': 0.4683178368,
    #'XSUncertainty': {
      #'Up': 0.0234, # estimated 5%
      #'Down': 0.0234, # estimated 5%
    #},
    #'Efficiency': 1.0,
    #'2016': {
      #'KFactor': 2.46996699808,
      #'Entries': 1974609,
      #'FileName': 'WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/WJetsToLNu_Pt-600ToInf_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 2.41529405422,
      #'Entries': 1989303,
      #'FileName': 'WJetsToLNu_Pt-600ToInf_TuneCP5_13TeV-amcatnloFXFX-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/WJetsToLNu_Pt-600ToInf_TuneCP5_13TeV-amcatnloFXFX-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 2.4159835611,
      #'Entries': 1950016,
      #'FileName': 'WJetsToLNu_Pt-600ToInf_TuneCP5_13TeV-amcatnloFXFX-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/WJetsToLNu_Pt-600ToInf_TuneCP5_13TeV-amcatnloFXFX-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight],
    #},
  #},
  #'QCD': {
    #'MC': True,
    #'TT': False,
    #'Name': 'QCD Data Driven',
    #'Color': 404,
    #'XS': 1.0,
    #'XSUncertainty': {
      #'Up': 0.5,
      #'Down': 0.5,
    #},
    #'Efficiency': 1.0,
    #'2016': {
      #'KFactor': 1.0,
      #'Entries': 35867.060, #Correct Lumi
      #'FileName': 'QCD_DataDriven',
      #'EventWeights': [],
    #},
    #'2017': {
      #'KFactor': 1.0,
      #'Entries': 41529.0, #Correct Lumi
      #'FileName': 'QCD_DataDriven',
      #'EventWeights': [],
    #},
    #'2018': {
      #'KFactor': 1.0,
      #'Entries': 59740.0, #Correct Lumi
      #'FileName': 'QCD_DataDriven',
      #'EventWeights': [],
    #},
  #},
  #'QCD_200To300': {
    #'MC': True,
    #'TT': False,
    #'Name': 'QCD 200-300',
    #'Color': 404,
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets', 'muons'],
    #'XS': 1556000.0,
    #'Efficiency': 1.0,
    #'2016': {
      #'KFactor': 1.0,
      #'Entries': 57580393,
      #'FileName': 'QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.00072395569,
      #'Entries': 59197363,
      #'FileName': 'QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/QCD_HT200to300_TuneCP5_13TeV-madgraph-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.00058548009,
      #'Entries': 54289442,
      #'FileName': 'QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/QCD_HT200to300_TuneCP5_13TeV-madgraphMLM-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight],
    #},
  #},
  #'QCD_300To500': {
    #'MC': True,
    #'TT': False,
    #'Name': 'QCD 300-500',
    #'Color': 404,
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets', 'muons'],
    #'XS': 323600.0,
    #'Efficiency': 1.0,
    #'2016': {
      #'KFactor': 1.0,
      #'Entries': 54552852,
      #'FileName': 'QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.00108139992,
      #'Entries': 59569132,
      #'FileName': 'QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/QCD_HT300to500_TuneCP5_13TeV-madgraph-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.00155480694,
      #'Entries': 54661579,
      #'FileName': 'QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/QCD_HT300to500_TuneCP5_13TeV-madgraphMLM-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight],
    #},
  #},
  #'QCD_500To700': {
    #'MC': True,
    #'TT': False,
    #'Name': 'QCD 500-700',
    #'Color': 404,
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets', 'muons'],
    #'XS': 29990.0,
    #'Efficiency': 1.0,
    #'2016': {
      #'KFactor': 1.0,
      #'Entries': 62622029,
      #'FileName': 'QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.00236119061,
      #'Entries': 56207744,
      #'FileName': 'QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/QCD_HT500to700_TuneCP5_13TeV-madgraph-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.00107550011,
      #'Entries': 55152960,
      #'FileName': 'QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/QCD_HT500to700_TuneCP5_13TeV-madgraphMLM-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight],
    #},
  #},
  #'QCD_700To1000': {
    #'MC': True,
    #'TT': False,
    #'Name': 'QCD 700-1000',
    #'Color': 404,
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets', 'muons'],
    #'XS': 6351.0,
    #'Efficiency': 1.0,
    #'2016': {
      #'KFactor': 1.0,
      #'Entries': 37233786,
      #'FileName': 'QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.00356529777,
      #'Entries': 46840955,
      #'FileName': 'QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/QCD_HT700to1000_TuneCP5_13TeV-madgraph-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.00240368999,
      #'Entries': 48158738,
      #'FileName': 'QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/QCD_HT700to1000_TuneCP5_13TeV-madgraphMLM-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight],
    #},
  #},
  #'QCD_1000To1500': {
    #'MC': True,
    #'TT': False,
    #'Name': 'QCD 1000-1500',
    #'Color': 404,
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets', 'muons'],
    #'XS': 1039.0,
    #'Efficiency': 1.0,
    #'2016': {
      #'KFactor': 1.0,
      #'Entries': 15210939,
      #'FileName': 'QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.0061702426,
      #'Entries': 16824762,
      #'FileName': 'QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/QCD_HT1000to1500_TuneCP5_13TeV-madgraph-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.00433875678,
      #'Entries': 15466225,
      #'FileName': 'QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight],
    #},
  #},
  #'QCD_1500To2000': {
    #'MC': True,
    #'TT': False,
    #'Name': 'QCD 1500-2000',
    #'Color': 404,
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets', 'muons'],
    #'XS': 99.01,
    #'Efficiency': 1.0,
    #'2016': {
      #'KFactor': 1.0,
      #'Entries': 11839357,
      #'FileName': 'QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.0091416176,
      #'Entries': 11634434,
      #'FileName': 'QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/QCD_HT1500to2000_TuneCP5_13TeV-madgraph-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.00990295108,
      #'Entries': 10955087,
      #'FileName': 'QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/QCD_HT1500to2000_TuneCP5_13TeV-madgraphMLM-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight],
    #},
  #},
  #'QCD_2000ToInf': {
    #'MC': True,
    #'TT': False,
    #'Name': 'QCD 2000-Inf',
    #'Color': 404,
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets', 'muons'],
    #'XS': 20.23,
    #'Efficiency': 1.0,
    #'2016': {
      #'KFactor': 1.0,
      #'Entries': 5804179,
      #'FileName': 'QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.01987938352,
      #'Entries': 5941306,
      #'FileName': 'QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/QCD_HT2000toInf_TuneCP5_13TeV-madgraph-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.01601423488,
      #'Entries': 5475677,
      #'FileName': 'QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/QCD_HT2000toInf_TuneCP5_13TeV-madgraphMLM-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight],
    #},
  #},
  #'TTWJetsToLNu': {
    #'MC': True,
    #'TT': False,
    #'Name': 'TTWJets to LNu',
    #'Color': 404,
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets', 'muons'],
    #'XS': 0.55,
    #'Efficiency': 0.3259,
    #'2016': {
      #'KFactor': 1.92186488942,
      #'Entries': 5280565,
      #'FileName': 'TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.8083414,
      #'Entries': 4908905,
      #'FileName': 'TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/TTWJetsToLNu_TuneCP5_PSweights_13TeV-amcatnloFXFX-madspin-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.8072015554,
      #'Entries': 4911941,
      #'FileName': 'TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight],
    #},
  #},
  #'TTWJetsToQQ': {
    #'MC': True,
    #'TT': False,
    #'Name': 'TTWJets to QQ',
    #'Color': 404,
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets', 'muons'],
    #'XS': 0.55,
    #'Efficiency': 0.6741,
    #'2016': {
      #'KFactor': 1.93925574801,
      #'Entries': 833298,
      #'FileName': 'TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.8315353,
      #'Entries': 811306,
      #'FileName': 'TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.8203853325,
      #'Entries': 835296,
      #'FileName': 'TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight],
    #},
  #},
  #'TTZToLLNuNu': {
    #'MC': True,
    #'TT': False,
    #'Name': 'TTZ to LLNuNu',
    #'Color': 404,
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets', 'muons'],
    #'XS': 0.86,
    #'Efficiency': 0.301,
    #'2016': {
      #'KFactor': 2.13901593969,
      #'Entries': 13692628,
      #'FileName': 'TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 2.11410316935,
      #'Entries': 11035000,
      #'FileName': 'TTZToLLNuNu_M-10_TuneCP5_PSweights_13TeV-amcatnlo-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/TTZToLLNuNu_M-10_TuneCP5_PSweights_13TeV-amcatnlo-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 2.10886527608,
      #'Entries': 13280000,
      #'FileName': 'TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight],
    #},
  #},
  #'TTZToQQ': {
    #'MC': True,
    #'TT': False,
    #'Name': 'TTZ to QQ',
    #'Color': 404,
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets', 'muons'],
    #'XS': 0.86,
    #'Efficiency': 0.699,
    #'2016': {
      #'KFactor': 2.11408013765,
      #'Entries': 749400,
      #'FileName': 'TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 2.08591286209,
      #'Entries': 9690000,
      #'FileName': 'TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 2.08780389194,
      #'Entries': 9572000,
      #'FileName': 'TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/TTZToQQ_TuneCP5_13TeV-amcatnlo-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight],
    #},
  #},
  #'WW': {
    #'MC': True,
    #'TT': False,
    #'Name': 'WW',
    #'Color': 404,
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets', 'muons'],
    #'XS': 118.7,
    #'Efficiency': 1.0,
    #'2016': {
      #'KFactor': 1.0,
      #'Entries': 7982180,
      #'FileName': 'WW_TuneCUETP8M1_13TeV-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/WW_TuneCUETP8M1_13TeV-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.0,
      #'Entries': 7765828,
      #'FileName': 'WW_TuneCP5_13TeV-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/WW_TuneCP5_13TeV-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.0,
      #'Entries': 7958000,
      #'FileName': 'WW_TuneCP5_PSweights_13TeV-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/WW_TuneCP5_PSweights_13TeV-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight],
    #},
  #},
  #'WZ': {
    #'MC': True,
    #'TT': False,
    #'Name': 'WZ',
    #'Color': 404,
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets', 'muons'],
    #'XS': 65.5443,
    #'Efficiency': 1.0,
    #'2016': {
      #'KFactor': 1.0,
      #'Entries': 6995142,
      #'FileName': 'WZ_TuneCUETP8M1_13TeV-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/WZ_TuneCUETP8M1_13TeV-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.0,
      #'Entries': 3928630,
      #'FileName': 'WZ_TuneCP5_13TeV-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/WZ_TuneCP5_13TeV-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.0,
      #'Entries': 3893000,
      #'FileName': 'WZ_TuneCP5_PSweights_13TeV-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/WZ_TuneCP5_PSweights_13TeV-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight],
    #},
  #},
  #'ZZ': {
    #'MC': True,
    #'TT': False,
    #'Name': 'ZZ',
    #'Color': 404,
    #'BranchGroups': ['mconly', 'electrons', 'event', 'jets', 'muons'],
    #'XS': 15.8274,
    #'Efficiency': 1.0,
    #'2016': {
      #'KFactor': 1.0,
      #'Entries': 1988098,
      #'FileName': 'ZZ_TuneCUETP8M1_13TeV-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/ZZ_TuneCUETP8M1_13TeV-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2017': {
      #'KFactor': 1.0,
      #'Entries': 1949768,
      #'FileName': 'ZZ_TuneCP5_13TeV-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/ZZ_TuneCP5_13TeV-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight, L1PreFiringWeight],
    #},
    #'2018': {
      #'KFactor': 1.0,
      #'Entries': 1979000,
      #'FileName': 'ZZ_TuneCP5_13TeV-pythia8',
      #'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/ZZ_TuneCP5_13TeV-pythia8.root',
      #'EventWeights': [genWeightSign, puWeight, btagWeight, leptonWeight, toptagWeight],
    #},
  #},

}

samples = {**signal, **background}
