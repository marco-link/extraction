# -*- coding: utf-8 -*-

"""
Defines properties of systematics.




Defines the names and properties of systematics in the systematics dict of dicts:

* dict key:     systematic name in datacard
* ``type``:     systematics type ('shape' or 'lnN')
* ``years``:    list of years to apply this systematic to
* ``datasets``:  (optional) list of datasets to apply this systematic to

for shape systematics (extra histograms produced)

* ``Branch``:   (optional) branch suffixes as dictionary with 'UP' and 'DOWN' keys
* ``EventWeights``:(optional) systematic weights to apply as dictionary with 'UP' and 'DOWN' keys


for lnN systematics (only added to datacards)

* ``value``: single value or tuple e.g. (0.908, 1.058)

"""


from config.general import allyears


systematics = {

    # Nominal
    'nominal': {
        'type': 'shape',
        'years': allyears,
    },


    'CMS_PU': {
        'type': 'shape',
        'EventWeights': {'UP': ['puWeightUp/puWeight'],
                         'DOWN': ['puWeightDown/puWeight']},
        'years': allyears,
    },


    #MEweight_murDown_mufDown
    #MEweight_murDown_mufNominal
    #MEweight_murDown_mufUp
    #MEweight_murNominal_mufDown
    #MEweight_murNominal_mufNominal
    #MEweight_murNominal_mufUp
    #MEweight_murUp_mufDown
    #MEweight_murUp_mufNominal
    #MEweight_murUp_mufUp

    #PSweight_ISRUp_FSRNominal
    #PSweight_ISRNominal_FSRUp
    #PSweight_ISRDown_FSRNominal
    #PSweight_ISRNominal_FSRDown

    #fragEventWeight_fragCP5BLVsPt

    #fragEventWeight_fragCP5BLdownVsPt
    #fragEventWeight_fragCP5BLupVsPt

    #fragEventWeight_fragCP5PetersonVsPt
    #fragEventWeight_fragCP5PetersondownVsPt
    #fragEventWeight_fragCP5PetersonupVsPt


    #'CMS_fragEventWeight_semilepbr': {
        #'type': 'shape',
        #'EventWeights': {'UP': ['fragEventWeight_semilepbrup'],
                        #'DOWN': ['fragEventWeight_semilepbrdown']},
        #'years': allyears,
    #},


    # muon
    'CMS_Muon_id': {
        'type': 'shape',
        'EventWeights': {'UP': ['tightMuons_weight_id_up/tightMuons_weight_id_nominal'],
                         'DOWN': ['tightMuons_weight_id_down/tightMuons_weight_id_nominal']},
        'years': allyears,
    },

    'CMS_Muon_reco': {
        'type': 'shape',
        'EventWeights': {'UP': ['tightMuons_weight_reco_up/tightMuons_weight_reco_nominal'],
                         'DOWN': ['tightMuons_weight_reco_down/tightMuons_weight_reco_nominal']},
        'years': allyears,
    },

    'CMS_Muon_iso': {
        'type': 'shape',
        'EventWeights': {'UP': ['tightMuons_weight_iso_up/tightMuons_weight_iso_nominal'],
                         'DOWN': ['tightMuons_weight_iso_down/tightMuons_weight_iso_nominal']},
        'years': allyears,
    },

    'CMS_IsoMuTrigger_2017': {
        'type': 'shape',
        'EventWeights': {'UP': ['IsoMuTrigger_weight_trigger_2017_up/IsoMuTrigger_weight_trigger_2017_nominal'],
                         'DOWN': ['IsoMuTrigger_weight_trigger_2017_down/IsoMuTrigger_weight_trigger_2017_nominal']},
        'years': '2017',
    },


    # electron
    'CMS_Electron_reco': {
        'type': 'shape',
        'EventWeights': {'UP': ['tightElectrons_weight_reco_up/tightElectrons_weight_reco_nominal'],
                         'DOWN': ['tightElectrons_weight_reco_down/tightElectrons_weight_reco_nominal']},
        'years': allyears,
    },

    'CMS_Electron_iso': {
        'type': 'shape',
        'EventWeights': {'UP': ['tightElectrons_weight_id_up/tightElectrons_weight_id_nominal'],
                         'DOWN': ['tightElectrons_weight_id_down/tightElectrons_weight_id_nominal']},
        'years': allyears,
    },

    'CMS_IsoElectronTrigger_2017': {
        'type': 'shape',

        'EventWeights': {'UP': ['IsoElectronTrigger_weight_trigger_2017_up/IsoElectronTrigger_weight_trigger_2017_nominal'],
                         'DOWN': ['IsoElectronTrigger_weight_trigger_2017_down/IsoElectronTrigger_weight_trigger_2017_nominal']},
        'years': '2017',
    },





    # JES

    'CMS_jes': {
        'type': 'shape',

        'Branch': {'UP': 'jesTotalUp',
                   'DOWN': 'jesTotalDown'},
        'years': allyears,
    },

    #'CMS_jes_Absolute_2017': {
        #'type': 'shape',

        #'Branch': {'UP': 'jesAbsolute_2017Up',
                   #'DOWN': 'jesAbsolute_2017Down'},
        #'years': '2017',
    #},



    # JER
    'CMS_jer': {
        'type': 'shape',

        'Branch': {'UP': 'jerUp',
                   'DOWN': 'jerDown'},
        'years': allyears,
    },


    #'lumi_13TeV': {
        #'type': 'lnN',
        #'value': 1.01, #TODO
        #'years': allyears,
    #},


    #'QCDscale': {
        #'type': 'lnN',
        #'value': (0.908, 1.058), #TODO
        #'datasets': ['TT_Semileptonic'],
        #'years': allyears,
    #},


    # b-tagging

    'CMS_btag_lf': {
        'type': 'shape',
        'EventWeights': {'UP': ['btagEventWeight_deepjet_shape_lfUp/btagEventWeight_deepjet_shape_nominal'],
                         'DOWN': ['btagEventWeight_deepjet_shape_lfDown/btagEventWeight_deepjet_shape_nominal']},
        'years': allyears,
    },

    'CMS_btag_lfstats1_2017': {
        'type': 'shape',
        'EventWeights': {'UP': ['btagEventWeight_deepjet_shape_lfstats1_2017Up/btagEventWeight_deepjet_shape_nominal'],
                         'DOWN': ['btagEventWeight_deepjet_shape_lfstats1_2017Down/btagEventWeight_deepjet_shape_nominal']},
        'years': '2017',
    },

    'CMS_btag_lfstats2_2017': {
        'type': 'shape',
        'EventWeights': {'UP': ['btagEventWeight_deepjet_shape_lfstats2_2017Up/btagEventWeight_deepjet_shape_nominal'],
                         'DOWN': ['btagEventWeight_deepjet_shape_lfstats2_2017Down/btagEventWeight_deepjet_shape_nominal']},
        'years': '2017',
    },


    'CMS_btag_cferr1': {
        'type': 'shape',
        'EventWeights': {'UP': ['btagEventWeight_deepjet_shape_cferr1Up/btagEventWeight_deepjet_shape_nominal'],
                         'DOWN': ['btagEventWeight_deepjet_shape_cferr1Down/btagEventWeight_deepjet_shape_nominal']},
        'years': allyears,
    },

    'CMS_btag_cferr2': {
        'type': 'shape',
        'EventWeights': {'UP': ['btagEventWeight_deepjet_shape_cferr2Up/btagEventWeight_deepjet_shape_nominal'],
                         'DOWN': ['btagEventWeight_deepjet_shape_cferr2Down/btagEventWeight_deepjet_shape_nominal']},
        'years': allyears,
    },


    'CMS_btag_hf': {
        'type': 'shape',
        'EventWeights': {'UP': ['btagEventWeight_deepjet_shape_hfUp/btagEventWeight_deepjet_shape_nominal'],
                         'DOWN': ['btagEventWeight_deepjet_shape_hfDown/btagEventWeight_deepjet_shape_nominal']},
        'years': allyears,
    },

    'CMS_btag_hfstats1_2017': {
        'type': 'shape',
        'EventWeights': {'UP': ['btagEventWeight_deepjet_shape_hfstats1_2017Up/btagEventWeight_deepjet_shape_nominal'],
                         'DOWN': ['btagEventWeight_deepjet_shape_hfstats1_2017Down/btagEventWeight_deepjet_shape_nominal']},
        'years': '2017',
    },

    'CMS_btag_hfstats2_2017': {
        'type': 'shape',
        'EventWeights': {'UP': ['btagEventWeight_deepjet_shape_hfstats2_2017Up/btagEventWeight_deepjet_shape_nominal'],
                         'DOWN': ['btagEventWeight_deepjet_shape_hfstats2_2017Down/btagEventWeight_deepjet_shape_nominal']},
        'years': '2017',
    },

}


#L1PreFiringWeight_ECAL_Dn
#L1PreFiringWeight_ECAL_Nom
#L1PreFiringWeight_ECAL_Up
#L1PreFiringWeight_ECAL_Down
#L1PreFiringWeight_ECAL_Nominal


#L1PreFiringWeight_Muon_Nom
#L1PreFiringWeight_Muon_StatDn
#L1PreFiringWeight_Muon_StatUp
#L1PreFiringWeight_Muon_SystDn
#L1PreFiringWeight_Muon_SystUp
#L1PreFiringWeight_Muon_Nominal
#L1PreFiringWeight_Muon_StatDown
#L1PreFiringWeight_Muon_SystDown


#L1PreFiringWeight_Down
#L1PreFiringWeight_Nominal
#L1PreFiringWeight_Nom
#L1PreFiringWeight_Up
#L1PreFiringWeight_Dn



#PDFweight_0 - 100


#jesUncertaintyNames = ["Total","Absolute","EC2","BBEC1", "HF","RelativeBal","FlavorQCD" ]
#for jesUncertaintyExtra in ["RelativeSample","HF","Absolute","EC2","BBEC1"]:
#jesUncertaintyNames.append(jesUncertaintyExtra+"_"+args.year.replace("preVFP",""))
