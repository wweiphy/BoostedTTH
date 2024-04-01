from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'TTbb_4f_TTTo2L2Nu_TuneCP5-Powheg-Openloops-Pythia8_2016preVFP_ntuple_0_0'
config.General.workArea = 'crab_ntuple'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/uscms/home/wwei/nobackup/SM_TTHH/Summer20UL/CMSSW_10_6_29/src/BoostedTTH/BoostedAnalyzer/test/boostedAnalysis_ntuples-Legacy_2016_2017_2018_cfg_UL_btag.py'
# config.JobType.outputFiles = ["ntuples_nominal_Tree.root", "ntuples_nominal_Cutflow.txt"]

config.JobType.outputFiles = ["ntuples_nominal_Tree.root", "ntuples_nominal_Cutflow.txt", "ntuples_JESup_Tree.root", "ntuples_JESup_Cutflow.txt", "ntuples_JESdown_Tree.root", "ntuples_JESdown_Cutflow.txt", "ntuples_JERup_Tree.root", "ntuples_JERup_Cutflow.txt", "ntuples_JERdown_Tree.root", "ntuples_JERdown_Cutflow.txt"]
                              
config.JobType.maxJobRuntimeMin = 2750
config.JobType.maxMemoryMB = 20000
config.JobType.numCores = 8
# config.JobType.maxMemoryMB = 4000
# config.JobType.pyCfgParams = ['isData=FALSE', 'maxEvents=999999999', 'outName=ntuples', 'dataEra=2018',
#                               'systematicVariations=nominal', 'weight=3.60E-06', 'ProduceMemNtuples=False', 'deterministicSeeds=False']

config.JobType.pyCfgParams = ['isData=FALSE', 'maxEvents=999999999', 'outName=ntuples', 'dataEra=2016preVFP',
                              'systematicVariations=nominal,JES,JER', 'weight=9.18E-05', 'ProduceMemNtuples=False', 'deterministicSeeds=False']

# config.JobType.sendPythonFolder=True
config.JobType.allowUndistributedCMSSW = True

# config.Data.inputDataset = '/TTbb_4f_TTTo2L2Nu_TuneCP5-Powheg-Openloops-Pythia8/lpctthrun2-sl_skims_MC_LEG_2017-f7a1084d3f7c1cbe4d4074d5b1a88d52/USER'

config.Data.inputDataset = '/TTbb_4f_TTTo2L2Nu_TuneCP5-Powheg-Openloops-Pythia8/RunIISummer20UL16MiniAODAPVv2-106X_mcRun2_asymptotic_preVFP_v11-v1/MINIAODSIM'

# config.Data.inputDBS = 'phys03'
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

