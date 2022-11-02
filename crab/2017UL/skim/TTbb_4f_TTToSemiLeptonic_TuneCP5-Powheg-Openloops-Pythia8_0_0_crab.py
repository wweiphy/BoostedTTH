from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8_2017_skim_0_0'
config.General.workArea = 'crab_skims'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '/uscms/home/wwei/nobackup/SM_TTHH/Summer20UL/CMSSW_10_6_29/src/BoostedTTH/BoostedAnalyzer/test/skim.py'
config.JobType.outputFiles = ['Skim.root']
config.JobType.maxJobRuntimeMin = 2800
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 20000
config.JobType.pyCfgParams = ['isData=FALSE','maxEvents=99999999','dataEra=2017']
config.JobType.sendPythonFolder=True
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 2
config.Data.publication = True
config.Data.publishDBS = 'phys03'
config.Data.outputDatasetTag = 'sl_skims_MC_LEG_2017'
config.Data.outLFNDirBase = '/store/group/lpctthrun2/wwei/UL/2017/skim'

#config.User.voGroup = 'dcms'

config.Site.storageSite = 'T3_US_FNALLPC'
#config.Site.blacklist = ['T2_US_*']
#config.Site.whitelist = ['T2_DE_DESY']
