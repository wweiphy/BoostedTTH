from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'TTHHTo4b_5f_LO_TuneCP5_13TeV_madgraph_pythia8_2017_ntuple_0_0'
config.General.workArea = 'crab_ntuple'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/uscms/home/wwei/nobackup/SM_TTHH/Summer20UL/CMSSW_10_6_29/src/BoostedTTH/BoostedAnalyzer/test/boostedAnalysis_ntuples-Legacy_2016_2017_2018_cfg_UL.py'
config.JobType.outputFiles = ["ntuples_nominal_Tree.root", "ntuples_nominal_Cutflow.txt"]
# config.JobType.maxJobRuntimeMin = 2800
config.JobType.maxMemoryMB = 5000
# config.JobType.numCores = 8

config.JobType.pyCfgParams = ['isData=FALSE','maxEvents=999999999','outName=ntuples', 'dataEra=2017','systematicVariations=nominal','weight=2.67E-08','ProduceMemNtuples=False', 'deterministicSeeds=False']
config.JobType.sendPythonFolder=True
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/lpctthrun2-sl_skims_MC_LEG_2017-f7a1084d3f7c1cbe4d4074d5b1a88d52/USER'
config.Data.inputDBS = 'phys03'
# config.Data.unitsPerJob = 5
# config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 1
config.Data.splitting = 'FileBased'
#config.Data.unitsPerJob = 720
# config.Data.splitting = 'Automatic'
config.Data.publication = False
config.Data.publishDBS = 'phys03'
config.Data.outputDatasetTag = 'sl_LEG_ntuple_2017'
config.Data.outLFNDirBase = '/store/group/lpctthrun2/wwei/UL/2017/ntuple'


config.Site.storageSite = 'T3_US_FNALLPC'

