# -*- coding: utf-8 -*-

"""
data currently not implemented
"""

#data = {
#'MC': False,
#'TT': False,
## 'BranchGroups': ['electrons', 'event', 'jets', 'dataonly', 'muons','triggers'],
#'BranchGroups': ['electrons', 'event', 'jets', 'dataonly', 'muons'],
#'Name': 'Data',
#'2016': {
#'runB1':{
#'SingleElectron': {
#'Entries': 240044046,
#'FileName': 'SingleElectron',
#'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/SingleElectron_2016B.root',
#'Regions' : ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'Trigger':'HLT_Ele32_eta2p1_WPTight_Gsf && !('
#'HLT_IsoMu24 || '
#'HLT_IsoTkMu24)',
#},
#},
#},
#'SingleMuon': {
#'Entries': 154054252,
#'FileName': 'SingleMuon',
#'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/SingleMuon_2016B.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'Trigger': 'HLT_IsoMu24 || HLT_IsoTkMu24',
#},
#},
#},
#},
#'runC': {
#'SingleElectron': {
#'Entries': 93326652,
#'FileName': 'SingleElectron',
#'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/SingleElectron_2016C.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'Trigger': 'HLT_Ele32_eta2p1_WPTight_Gsf && !('
#'HLT_IsoMu24 || '
#'HLT_IsoTkMu24)',
#},
#},
#},
#'SingleMuon': {
#'Entries': 64718679,
#'FileName': 'SingleMuon',
## 'GridPath': '/work/jrauser/frameworks/cmssw/napalm/CMSSW_10_6_2/src/napalm/trees/test/\
#SingleMuon_Run2016C-02Apr2020-v1_NANOAOD_v7_Skim.root', # Testing
#'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/SingleMuon_2016C.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'Trigger': 'HLT_IsoMu24 || HLT_IsoTkMu24',
#},
#},
#},
#},
#'runD': {
#'SingleElectron': {
#'Entries': 146495223,
#'FileName': 'SingleElectron',
#'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/SingleElectron_2016D.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'Trigger': 'HLT_Ele32_eta2p1_WPTight_Gsf && !('
#'HLT_IsoMu24 || '
#'HLT_IsoTkMu24)',
#},
#},
#},
#'SingleMuon': {
#'Entries': 96657799,
#'FileName': 'SingleMuon',
#'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/SingleMuon_2016D.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'Trigger': 'HLT_IsoMu24 || HLT_IsoTkMu24',
#},
#},
#},
#},
#'runE': {
#'SingleElectron': {
#'Entries': 113169852,
#'FileName': 'SingleElectron',
#'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/SingleElectron_2016E.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'Trigger': 'HLT_Ele32_eta2p1_WPTight_Gsf && !('
#'HLT_IsoMu24 || '
#'HLT_IsoTkMu24)',
#},
#},
#},
#'SingleMuon': {
#'Entries': 87378748,
#'FileName': 'SingleMuon',
#'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/SingleMuon_2016E.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'Trigger': 'HLT_IsoMu24 || HLT_IsoTkMu24',
#},
#},
#},
#},
#'runF': {
#'SingleElectron': {
#'Entries': 70143321,
#'FileName': 'SingleElectron',
#'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/SingleElectron_2016F.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'Trigger': 'HLT_Ele32_eta2p1_WPTight_Gsf && !('
#'HLT_IsoMu24 || '
#'HLT_IsoTkMu24)',
#},
#},
#},
#'SingleMuon': {
#'Entries': 65047318,
#'FileName': 'SingleMuon',
#'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/SingleMuon_2016F.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'Trigger': 'HLT_IsoMu24 || HLT_IsoTkMu24',
#},
#},
#},
#},
#'runG': {
#'SingleElectron': {
#'Entries': 152098617,
#'FileName': 'SingleElectron',
#'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/SingleElectron_2016G.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'Trigger': 'HLT_Ele32_eta2p1_WPTight_Gsf && !('
#'HLT_IsoMu24 || '
#'HLT_IsoTkMu24)',
#},
#},
#},
#'SingleMuon': {
#'Entries': 147941144,
#'FileName': 'SingleMuon',
#'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/SingleMuon_2016G.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'Trigger': 'HLT_IsoMu24 || HLT_IsoTkMu24',
#},
#},
#},
#},
#'runH': {
#'SingleElectron': {
#'Entries': 128854598,
#'FileName': 'SingleElectron',
#'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/SingleElectron_2016H.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'Trigger': 'HLT_Ele32_eta2p1_WPTight_Gsf && !('
#'HLT_IsoMu24 || '
#'HLT_IsoTkMu24)',
#},
#},
#},
#'SingleMuon': {
#'Entries': 174035164,
#'FileName': 'SingleMuon',
#'GridPath': '/ceph/jrauser/nanoaod2/2016/merge/SingleMuon_2016H.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'Trigger': 'HLT_IsoMu24 || HLT_IsoTkMu24',
#},
#},
#},
#},
#},
#'2017':{
#'runB': {
#'SingleElectron': {
#'Entries': 56501676,
#'FileName': 'SingleElectron',
#'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/SingleElectron_2017B.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'Trigger': '(HLT_Ele35_WPTight_Gsf || HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned) && !HLT_IsoMu27',
#},
#},
#},
#'SingleMuon': {
#'Entries': 128496874,
#'FileName': 'SingleMuon',
## 'GridPath': '/work/jrauser/frameworks/cmssw/napalm/CMSSW_10_6_2/src/napalm/trees/test/\
#SingleMuon_Run2017B-02Apr2020-v1_NANOAOD_v7_Skim.root', # Testing
#'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/SingleMuon_2017B.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'Trigger': 'HLT_IsoMu27',
#},
#},
#},
#},
#'runC': {
#'SingleElectron': {
#'Entries': 127361546,
#'FileName': 'SingleElectron',
#'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/SingleElectron_2017C.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'Trigger': '(HLT_Ele35_WPTight_Gsf || HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned) && !HLT_IsoMu27',
#},
#},
#},
#'SingleMuon': {
#'Entries': 154633551,
#'FileName': 'SingleMuon',
#'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/SingleMuon_2017C.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'Trigger': 'HLT_IsoMu27',
#},
#},
#},
#},
#'runD': {
#'SingleElectron': {
#'Entries': 50610320,
#'FileName': 'SingleElectron',
#'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/SingleElectron_2017D.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'Trigger': '(HLT_Ele35_WPTight_Gsf || HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned) && !HLT_IsoMu27',
#},
#},
#},
#'SingleMuon': {
#'Entries': 69031074,
#'FileName': 'SingleMuon',
#'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/SingleMuon_2017D.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'Trigger': 'HLT_IsoMu27',
#},
#},
#},
#},
#'runE': {
#'SingleElectron': {
#'Entries': 100205122,
#'FileName': 'SingleElectron',
#'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/SingleElectron_2017E.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'Trigger': '(HLT_Ele35_WPTight_Gsf || HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned) && !HLT_IsoMu27',
#},
#},
#},
#'SingleMuon': {
#'Entries': 151713898,
#'FileName': 'SingleMuon',
#'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/SingleMuon_2017E.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'Trigger': 'HLT_IsoMu27',
#},
#},
#},
#},
#'runF': {
#'SingleElectron': {
#'Entries': 126061224,
#'FileName': 'SingleElectron',
#'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/SingleElectron_2017F.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'Trigger': '(HLT_Ele35_WPTight_Gsf || HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned) && !HLT_IsoMu27',
#},
#},
#},
#'SingleMuon': {
#'Entries': 235939903,
#'FileName': 'SingleMuon',
#'GridPath': '/ceph/jrauser/nanoaod2/2017/merge/SingleMuon_2017F.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'Trigger': 'HLT_IsoMu27',
#},
#},
#},
#},
#},
#'2018': {
#'runA': {
#'SingleElectron': {
#'Entries': 308668555,
#'FileName': 'SingleElectron',
#'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/EGamma_2018A.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'Trigger': '(HLT_Ele32_WPTight_Gsf || HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned) && !HLT_IsoMu24',
#},
#},
#},
#'SingleMuon': {
#'Entries': 227489240,
#'FileName': 'SingleMuon',
## 'GridPath': '/work/jrauser/frameworks/cmssw/napalm/CMSSW_10_6_2/src/napalm/trees/test/\
#SingleMuon_Run2018A-02Apr2020-v1_NANOAOD_v7_Skim.root', # Testing
#'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/SingleMuon_2018A.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'Trigger': 'HLT_IsoMu24',
#},
#},
#},
#},
#'runB': {
#'SingleElectron': {
#'Entries': 139144140,
#'FileName': 'SingleElectron',
#'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/EGamma_2018B.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'Trigger': '(HLT_Ele32_WPTight_Gsf || HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned) && !HLT_IsoMu24',
#},
#},
#},
#'SingleMuon': {
#'Entries': 110446445,
#'FileName': 'SingleMuon',
#'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/SingleMuon_2018B.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'Trigger': 'HLT_IsoMu24',
#},
#},
#},
#},
#'runC': {
#'SingleElectron': {
#'Entries': 143697310,
#'FileName': 'SingleElectron',
#'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/EGamma_2018C.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'Trigger': '(HLT_Ele32_WPTight_Gsf || HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned) && !HLT_IsoMu24',
#},
#},
#},
#'SingleMuon': {
#'Entries': 107972995,
#'FileName': 'SingleMuon',
#'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/SingleMuon_2018C.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'Trigger': 'HLT_IsoMu24',
#},
#},
#},
#},
#'runD': {
#'SingleElectron': {
#'Entries': 704810729,
#'FileName': 'SingleElectron',
#'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/EGamma_2018D.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdelectron'],
#'Trigger': '(HLT_Ele32_WPTight_Gsf || HLT_Ele30_eta2p1_WPTight_Gsf_CentralPFJet35_EleCleaned) && !HLT_IsoMu24',
#},
#},
#},
#'SingleMuon': {
#'Entries': 492637435,
#'FileName': 'SingleMuon',
#'GridPath': '/ceph/jrauser/nanoaod2/2018/merge/SingleMuon_2018D.root',
#'Regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'HLT': {
#'semilep':{
#'regions': ['semilepcombined', 'semilepcontrol', 'control', 'abcdmuon'],
#'Trigger': 'HLT_IsoMu24',
#},
#},
#},
#},
#},
#}
