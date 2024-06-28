from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8_2016preVFP_ntuple_0_0'
config.General.workArea = 'crab_ntuple'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/work/SM_TTHH/Summer20UL/EL8/Ntuple/CMSSW_10_6_29/src/BoostedTTH/BoostedAnalyzer/test/boostedAnalysis_ntuples-Legacy_2016_2017_2018_cfg_UL_btag.py'
# config.JobType.outputFiles = ["ntuples_nominal_Tree.root", "ntuples_nominal_Cutflow.txt"]

config.JobType.outputFiles = ["ntuples_nominal_Tree.root", "ntuples_nominal_Cutflow.txt", "ntuples_JESup_Tree.root", "ntuples_JESup_Cutflow.txt", "ntuples_JESdown_Tree.root", "ntuples_JESdown_Cutflow.txt", "ntuples_JERup_Tree.root", "ntuples_JERup_Cutflow.txt", "ntuples_JERdown_Tree.root", "ntuples_JERdown_Cutflow.txt"]

config.JobType.maxJobRuntimeMin = 2000
config.JobType.maxMemoryMB = 10000
config.JobType.numCores = 4
# config.JobType.maxMemoryMB = 4000
config.JobType.pyCfgParams = ['isData=FALSE', 'maxEvents=999999999', 'outName=ntuples', 'dataEra=2016preVFP',
                              'systematicVariations=nominal,JES,JER', 'weight=2.68E-08', 'ProduceMemNtuples=False', 'deterministicSeeds=False']
# config.JobType.sendPythonFolder=True
config.JobType.allowUndistributedCMSSW = True

# config.Data.userInputFiles = ['/store/group/lpctthrun2/wwei/TTZH_TuneCP5_13TeV-madgraph-pythia8/sl_skims_MC_94X_LEG_2017/220311_034726/0000/Skim_1.root',
#      '/store/group/lpctthrun2/wwei/TTZH_TuneCP5_13TeV-madgraph-pythia8/sl_skims_MC_94X_LEG_2017/220311_034726/0000/Skim_2.root',
#      '/store/group/lpctthrun2/wwei/TTZH_TuneCP5_13TeV-madgraph-pythia8/sl_skims_MC_94X_LEG_2017/220311_034726/0000/Skim_3.root']
     
config.Data.inputDataset = '/TTZHTo4b_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v2/MINIAODSIM'
config.Data.inputDBS = 'global'

# config.Data.unitsPerJob = 1000
# config.Data.splitting = 'EventAwareLumiBased'
NJOB = 50
config.Data.unitsPerJob = 1
config.Data.splitting = 'FileBased'
config.Data.totalUnits = config.Data.unitsPerJob * NJOB
config.Data.publication = False
config.Data.publishDBS = 'phys03'
config.Data.outputDatasetTag = 'sl_LEG_ntuple_2016preVFP'
config.Data.outLFNDirBase = '/store/group/lpctthrun2/wwei/UL/2016pre/ntuple'
# config.Data.outLFNDirBase = '/store/user/wwei/UL/2017/ntuple'

config.Site.storageSite = 'T3_US_FNALLPC'

