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


    #FIXME only test systematics!

    'jesAbsolute_2017': {
        'type': 'shape',

        'Branch': {'UP': 'jesAbsolute_2017Up',
                   'DOWN': 'jesAbsolute_2017Down'},
        'years': '2017',
    },

    #'CMS_Muon_id': {
        #'type': 'shape',

        #'EventWeights': {'UP': ['tightMuons_weight_id_up/tightMuons_weight_id_nominal'],
                         #'DOWN': ['tightMuons_weight_id_down/tightMuons_weight_id_nominal']},
        #'years': allyears,
    #},


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

}
