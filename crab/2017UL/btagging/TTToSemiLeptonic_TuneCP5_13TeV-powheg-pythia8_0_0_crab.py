from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_2017_ntuple_0_0'
config.General.workArea = 'crab_ntuple'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/uscms/home/wwei/nobackup/SM_TTHH/Summer20UL/CMSSW_10_6_29/src/BoostedTTH/BoostedAnalyzer/test/boostedAnalysis_ntuples-Legacy_2016_2017_2018_cfg_UL.py'
# config.JobType.outputFiles = ["ntuples_nominal_Tree.root", "ntuples_nominal_Cutflow.txt"]

config.JobType.outputFiles = ["ntuples_nominal_Tree.root", "ntuples_nominal_Cutflow.txt", "ntuples_JESup_Tree.root", "ntuples_JESup_Cutflow.txt", "ntuples_JESdown_Tree.root", "ntuples_JESdown_Cutflow.txt", "ntuples_JERup_Tree.root", "ntuples_JERup_Cutflow.txt", "ntuples_JERdown_Tree.root", "ntuples_JERdown_Cutflow.txt"]

config.JobType.maxJobRuntimeMin = 2750
config.JobType.maxMemoryMB = 20000
config.JobType.numCores = 8
# config.JobType.maxMemoryMB = 4000


config.JobType.pyCfgParams = ['isData=FALSE', 'maxEvents=99999999', 'outName=ntuples', 'dataEra=2017',
                              'systematicVariations=nominal,JES,JER', 'weight=3.42E-06', 'ProduceMemNtuples=False', 'deterministicSeeds=False']

# config.JobType.pyCfgParams = ['isData=FALSE', 'maxEvents=99999999', 'outName=ntuples', 'dataEra=2017',
#                               'systematicVariations=nominal,JES,JER,JESFlavorQCD,JESRelativeBal,JESHF,JESBBEC1,JESEC2,JESAbsolute,JESBBEC1year,JESRelativeSampleyear,JESEC2year,JESHFyear,JESAbsoluteyear', 'weight=3.42E-06', 'ProduceMemNtuples=False', 'deterministicSeeds=False']
# config.JobType.sendPythonFolder=True
config.JobType.allowUndistributedCMSSW = True

# config.Data.inputDataset = '/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/lpctthrun2-sl_skims_MC_LEG_2017-f7a1084d3f7c1cbe4d4074d5b1a88d52/USER'

config.Data.inputDataset = '/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM'

# config.Data.inputDBS = 'phys03'
config.Data.inputDBS = 'global'
# config.Data.splitting = 'EventAwareLumiBased'
# config.Data.unitsPerJob = 5000
# NJOB = 9000
# config.Data.totalUnits = config.Data.unitsPerJob * NJOB
NJOB = 50
config.Data.unitsPerJob = 1
config.Data.splitting = 'FileBased'
config.Data.totalUnits = config.Data.unitsPerJob * NJOB
# config.Data.splitting = 'Automatic'
config.Data.publication = False
config.Data.publishDBS = 'phys03'
config.Data.outputDatasetTag = 'sl_LEG_ntuple_2017'
config.Data.outLFNDirBase = '/store/group/lpctthrun2/wwei/UL/2017/ntuple'
# config.Data.outLFNDirBase = '/store/user/wwei/UL/2017/ntuple'


config.Site.storageSite = 'T3_US_FNALLPC'
# config.Site.blacklist = 'T1_US_FNAL'

