from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'TTZZTo4b_5f_LO_TuneCP5_13TeV_madgraph_pythia8_2018_ntuple_0_0_7'
config.General.workArea = 'crab_ntuple'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/uscms/home/wwei/nobackup/SM_TTHH/Summer20UL/CMSSW_10_6_29/src/BoostedTTH/BoostedAnalyzer/test/boostedAnalysis_ntuples-Legacy_2016_2017_2018_cfg_UL.py'
config.JobType.outputFiles = ["ntuples_nominal_Tree.root", "ntuples_nominal_Cutflow.txt"]

# config.JobType.outputFiles = ["ntuples_nominal_Tree.root", "ntuples_nominal_Cutflow.txt", "ntuples_JESup_Tree.root", "ntuples_JESup_Cutflow.txt", "ntuples_JESdown_Tree.root", "ntuples_JESdown_Cutflow.txt", "ntuples_JERup_Tree.root", "ntuples_JERup_Cutflow.txt", "ntuples_JERdown_Tree.root", "ntuples_JERdown_Cutflow.txt", "ntuples_JESFlavorQCDup_Tree.root", "ntuples_JESFlavorQCDup_Cutflow.txt", "ntuples_JESFlavorQCDdown_Tree.root", "ntuples_JESFlavorQCDdown_Cutflow.txt", "ntuples_JESRelativeBalup_Tree.root", "ntuples_JESRelativeBalup_Cutflow.txt", "ntuples_JESRelativeBaldown_Tree.root", "ntuples_JESRelativeBaldown_Cutflow.txt", "ntuples_JESHFup_Tree.root", "ntuples_JESHFup_Cutflow.txt", "ntuples_JESHFdown_Tree.root", "ntuples_JESHFdown_Cutflow.txt", "ntuples_JESBBEC1up_Tree.root", "ntuples_JESBBEC1up_Cutflow.txt", "ntuples_JESBBEC1down_Tree.root", "ntuples_JESBBEC1down_Cutflow.txt", "ntuples_JESEC2up_Tree.root", "ntuples_JESEC2up_Cutflow.txt", "ntuples_JESEC2down_Tree.root", "ntuples_JESEC2down_Cutflow.txt", "ntuples_JESAbsoluteup_Tree.root", "ntuples_JESAbsoluteup_Cutflow.txt", "ntuples_JESAbsolutedown_Tree.root", "ntuples_JESAbsolutedown_Cutflow.txt", "ntuples_JESBBEC1yearup_Tree.root", "ntuples_JESBBEC1yearup_Cutflow.txt", "ntuples_JESBBEC1yeardown_Tree.root", "ntuples_JESBBEC1yeardown_Cutflow.txt", "ntuples_JESRelativeSampleyearup_Tree.root", "ntuples_JESRelativeSampleyearup_Cutflow.txt",
                            #   "ntuples_JESRelativeSampleyeardown_Tree.root", "ntuples_JESRelativeSampleyeardown_Cutflow.txt", "ntuples_JESEC2yearup_Tree.root", "ntuples_JESEC2yearup_Cutflow.txt", "ntuples_JESEC2yeardown_Tree.root", "ntuples_JESEC2yeardown_Cutflow.txt", "ntuples_JESHFyearup_Tree.root", "ntuples_JESHFyearup_Cutflow.txt", "ntuples_JESHFyeardown_Tree.root", "ntuples_JESHFyeardown_Cutflow.txt", "ntuples_JESAbsoluteyearup_Tree.root", "ntuples_JESAbsoluteyearup_Cutflow.txt", "ntuples_JESAbsoluteyeardown_Tree.root", "ntuples_JESAbsoluteyeardown_Cutflow.txt"]

config.JobType.maxJobRuntimeMin = 2750
config.JobType.maxMemoryMB = 10000
config.JobType.numCores = 4
# config.JobType.maxMemoryMB = 4000

config.JobType.pyCfgParams = ['isData=FALSE', 'maxEvents=999999999', 'outName=ntuples', 'dataEra=2018',
                              'systematicVariations=nominal', 'weight=4.56E-09', 'ProduceMemNtuples=False', 'deterministicSeeds=False']
# config.JobType.sendPythonFolder=True
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/TTZZTo4b_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18MiniAODv2-106X_upgrade2018_realistic_v16_L1v1-v2/MINIAODSIM'
config.Data.inputDBS = 'global'
# config.Data.unitsPerJob = 1000
# config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 3
config.Data.splitting = 'FileBased'
config.Data.publication = False
config.Data.publishDBS = 'phys03'
config.Data.outputDatasetTag = 'sl_LEG_ntuple_2018'
config.Data.outLFNDirBase = '/store/group/lpctthrun2/wwei/UL/2018/ntuple'
# config.Data.outLFNDirBase = '/store/user/wwei/UL/2017/ntuple'


config.Site.storageSite = 'T3_US_FNALLPC'

