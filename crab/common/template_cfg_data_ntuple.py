from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'THEREQUESTNAME'
config.General.workArea = 'WORKAREA'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'CMSSWPATH/RUNCONFIG'
config.JobType.outputFiles = OUTPUTFILES
config.JobType.maxJobRuntimeMin = 2750
config.JobType.maxMemoryMB = 10000 
config.JobType.numCores = 4
config.JobType.pyCfgParams = ['isData=ISDATA','maxEvents=999999999','outName=OUTNAME', 'dataEra=DATAERA','systematicVariations=SYSTEMATICVARIATIONS','weight=WEIGHT','ProduceMemNtuples=False', 'deterministicSeeds=False']
# config.JobType.sendPythonFolder=True

config.Data.inputDataset = 'THEINPUTDATASET'
config.Data.lumiMask = 'LUMIMASK'
config.Data.inputDBS = 'DBSINSTANCE'
# config.Data.splitting = 'EventAwareLumiBased'
config.Data.unitsPerJob = 3200000
config.Data.splitting = 'SPLITTING'
config.Data.publication = False
config.Data.publishDBS = 'phys03'
config.Data.outputDatasetTag = 'sl_LEG_NTUPLETAG_DATAERA'

config.Data.outLFNDirBase = '/store/group/lpctthrun2/wwei/UL/DATAERA/ntuple'

config.Site.storageSite = 'T3_US_FNALLPC'
# config.Site.blacklist = ['T2_CH_CERN','T2_US_Wisconsin','T2_US_Purdue','T2_US_Nebraska']


