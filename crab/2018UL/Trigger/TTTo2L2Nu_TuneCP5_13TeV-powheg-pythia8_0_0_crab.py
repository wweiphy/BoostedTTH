from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8_2018_ntuple_0_0_Trigger_3'
config.General.workArea = 'crab_ntuple'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/work/SM_TTHH/Summer20UL/EL8/Ntuple/CMSSW_10_6_29/src/BoostedTTH/BoostedAnalyzer/test/boostedAnalysis_ntuples-Legacy_2016_2017_2018_cfg_UL_Trigger.py'

# config.JobType.outputFiles = ["ntuples_nominal_Tree.root", "ntuples_nominal_Cutflow.txt"]

config.JobType.outputFiles = ["ntuples_nominal_Tree.root", "ntuples_nominal_Cutflow.txt"]

config.JobType.maxJobRuntimeMin = 2000
config.JobType.maxMemoryMB = 10000
config.JobType.numCores = 4
# config.JobType.maxMemoryMB = 4000


# config.JobType.pyCfgParams = ['isData=FALSE', 'maxEvents=99999999', 'outName=ntuples', 'dataEra=2017',
#                               'systematicVariations=nominal', 'weight=1.15E-05', 'ProduceMemNtuples=False', 'deterministicSeeds=False']

config.JobType.pyCfgParams = ['isData=FALSE', 'maxEvents=99999999', 'outName=ntuples', 'dataEra=2018',
                              'systematicVariations=nominal', 'weight=2.52E-05', 'ProduceMemNtuples=False', 'deterministicSeeds=False']
# config.JobType.sendPythonFolder=True
# config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v1/MINIAODSIM'

# config.Data.inputDBS = 'phys03'
config.Data.inputDBS = 'global'
# config.Data.splitting = 'EventAwareLumiBased'
# config.Data.unitsPerJob = 5000

# NJOB = 341 
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 4
# config.Data.totalUnits = config.Data.unitsPerJob * NJOB
# config.Data.splitting = 'Automatic'
config.Data.publication = False
config.Data.publishDBS = 'phys03'
config.Data.outputDatasetTag = 'sl_LEG_ntuple_2018'
config.Data.outLFNDirBase = '/store/group/lpctthrun2/wwei/UL/2018/ntuple'
# config.Data.outLFNDirBase = '/store/user/wwei/UL/2017/ntuple'


config.Site.storageSite = 'T3_US_FNALLPC'
# config.Site.blacklist = 'T1_US_FNAL'

