import CRABClient
from CRABClient.UserUtilities import config

config = config()

config.General.requestName = 'TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8_2017_ntuple_0_0'
config.General.workArea = 'crab_ntuple'
config.General.transferOutputs = True 

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'boostedAnalysis_ntuples-Legacy_2016_2017_2018_cfg_UL.py'
config.JobType.outputFiles = ["ntuples_nominal_Tree.root", "ntuples_nominal_Cutflow.txt"]
# config.JobType.maxJobRuntimeMin = 2800
# config.JobType.maxMemoryMB = 20000
# config.JobType.numCores = 8
# config.JobType.pyCfgParams = ['isData=FALSE','maxEvents=999999999','outName=ntuples', 'dataEra=2017','systematicVariations=nominal','weight=2.78E-05','ProduceMemNtuples=False', 'deterministicSeeds=False']
# config.JobType.sendPythonFolder=True
config.JobType.allowUndistributedCMSSW = True

config.Data.inputDataset = '/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17MiniAODv2-106X_mc2017_realistic_v9-v1/MINIAODSIM'
config.Data.inputDBS = 'global'
# config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 5
config.Data.splitting = 'FileBased'
config.Data.publication = False
config.Data.publishDBS = 'phys03'
config.Data.outputDatasetTag = 'sl_LEG_ntuple_2017'
config.Data.outLFNDirBase = '/store/group/lpctthrun2/wwei/UL/2017'


config.Site.storageSite = 'T3_US_FNALLPC'

