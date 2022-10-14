import FWCore.ParameterSet.Config as cms
import sys
import os

# lack CombineHarvester, RecoBTag


# To execute test, run

# python boostedAnalysis_ntuples-Legacy_2016_2017_2018_cfg_UL.py isData=False outputFile=test maxEvents=10 systematicVariations=nominal dataEra=2017 ProduceMemNtuples=False deterministicSeeds=False inputFiles=/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2560000/05CB1A7E-2A10-514E-8E1F-76E9749EE10D.root

# cmsRun boostedAnalysis_ntuples-Legacy_2016_2017_2018_cfg_UL.py isData=False outputFile=test maxEvents=10 systematicVariations=nominal dataEra=2017 ProduceMemNtuples=False deterministicSeeds=False inputFiles=/store/mc/RunIISummer20UL17MiniAODv2/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v1/00000/005708B7-331C-904E-88B9-189011E6C9DD.root

# cmsRun boostedAnalysis_ntuples-Legacy_2016_2017_2018_cfg_UL.py isData=False outputFile=test maxEvents=10 systematicVariations=nominal dataEra=2018 ProduceMemNtuples=False deterministicSeeds=False inputFiles=/store/mc/RunIISummer20UL18MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2430000/31C4D752-4BB3-324A-BE81-A24F0B1037D5.root


# cmsRun boostedAnalysis_ntuples-Legacy_2016_2017_2018_cfg.py isData=False outputFile=test maxEvents=100 systematicVariations=nominal,JES,JER,JESFlavorQCD,JESRelativeBal,JESHF,JESBBEC1,JESEC2,JESAbsolute,JESBBEC1year,JESRelativeSampleyear,JESEC2year,JESHFyear,JESAbsoluteyear,JEReta0,JEReta1,JERpt0eta2,JERpt1eta2,JERpt0eta3,JERpt1eta3 dataEra=2017 ProduceMemNtuples=False deterministicSeeds=False inputFiles=/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2560000/05CB1A7E-2A10-514E-8E1F-76E9749EE10D.root

# cmsRun boostedAnalysis_ntuples-Legacy_2016_2017_2018_cfg.py isData=False outputFile=test maxEvents=100 systematicVariations=nominal,JES,JER,JESFlavorQCD,JESRelativeBal,JESHF,JESBBEC1,JESEC2,JESAbsolute,JESBBEC1year,JESRelativeSampleyear,JESEC2year,JESHFyear,JESAbsoluteyear,JERpt0eta0 dataEra=2017 ProduceMemNtuples=False deterministicSeeds=False inputFiles=/store/mc/RunIISummer20UL17MiniAODv2/TTHHTo4b_TuneCP5_13TeV-madgraph-pythia8/MINIAODSIM/106X_mc2017_realistic_v9-v2/2560000/05CB1A7E-2A10-514E-8E1F-76E9749EE10D.root
 
# parse command-line arguments
# https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideCommandLineParsing
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('analysis')
# The following variables are already defined in VarParsing class:
# maxEvents: singleton, int; default = -1
# inputFiles: (comma separated, no spaces!) list, string: default empty
options.register( "outName", "testrun", VarParsing.multiplicity.singleton, VarParsing.varType.string, "name and path of the output files (without extension)" )
options.register( "weight", 0.01, VarParsing.multiplicity.singleton, VarParsing.varType.float, "xs*lumi/(nPosEvents-nNegEvents)" )
options.register( "skipEvents", 0, VarParsing.multiplicity.singleton, VarParsing.varType.int, "Number of events to skip" )
options.register( "isData", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "is it data or MC?" )
options.register( "isBoostedMiniAOD", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "has the file been prepared with the BoostedProducer ('custom' MiniAOD)?" )
options.register( "generatorName", "MadGraph", VarParsing.multiplicity.singleton, VarParsing.varType.string, "'POWHEG','aMC', 'MadGraph' or 'pythia8'" )
options.register("globalTag", "106X_mc2017_realistic_v9",
                 VarParsing.multiplicity.singleton, VarParsing.varType.string, "global tag")
options.register( "useJson",True, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "apply the json filter (on the grid there are better ways to do this)" )
options.register( "additionalSelection","NONE", VarParsing.multiplicity.singleton, VarParsing.varType.string, "addition Selection to use for this sample" )
datasets=['NA','mu','el','elel','elmu','mumu']
options.register( "dataset", "NA", VarParsing.multiplicity.singleton, VarParsing.varType.string, "flag to identify which dataset is used, can be "+','.join(datasets))
# options.register( "calcBJetness",False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "Calculate BJetness variables" )
options.register( "dumpSyncExe", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "Dump textfiles for sync exe?" )
options.register( "systematicVariations","nominal", VarParsing.multiplicity.list, VarParsing.varType.string, "comma-separated list of systematic variations ('nominal' or systematics base name, up/down will be added)" )
options.register( "deterministicSeeds",False,VarParsing.multiplicity.singleton,VarParsing.varType.bool,"create collections with deterministic seeds")
# options.register( "electronRegression","",VarParsing.multiplicity.singleton,VarParsing.varType.string,"'GT' or an absolute path to a sqlite file for electron energy regression")
# options.register( "electronSmearing","",VarParsing.multiplicity.singleton,VarParsing.varType.string,"correction type for electron energy smearing")
options.register( "useMuonRC", True, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "use Rochester Correction for muons" )
options.register( "dataEra",     "2017",     VarParsing.multiplicity.singleton,     VarParsing.varType.string,     "the era of the data taking period or mc campaign, e.g. '2016B' or '2017'" )
# options.register( "updatePUJetId",     False,     VarParsing.multiplicity.singleton,     VarParsing.varType.bool,     "update the PUJetId values" )
options.register( "ProduceMemNtuples", False, VarParsing.multiplicity.singleton, VarParsing.varType.bool, "do you want to produce slimmed ntuples as input to mem code?" )

options.parseArguments()

# re-set some defaults
if options.maxEvents is -1: # maxEvents is set in VarParsing class by default to -1
    options.maxEvents = 1000 # reset for testing

if options.isData:
    if "2016" in options.dataEra:
        options.globalTag="106X_dataRun2_v35"
    elif "2017" in options.dataEra:
        options.globalTag="106X_dataRun2_v35"
    elif "2018" in options.dataEra:
        options.globalTag="106X_dataRun2_v35"
    else:
        raise Exception( "dataEra "+options.dataEra+" not supported for this config: USE dataEra=2016/2017")
elif not options.isData:
    if "2016preVFP" in options.dataEra:
        options.globalTag = "106X_mcRun2_asymptotic_preVFP_v11"
    elif "2016postVFP" in options.dataEra:
        options.globalTag = "106X_mcRun2_asymptotic_v17"
    elif "2017" in options.dataEra:
        options.globalTag = "106X_mc2017_realistic_v9"
    elif "2018" in options.dataEra:
        options.globalTag = "106X_upgrade2018_realistic_v16_L1v1"
    else:
        raise Exception( "dataEra "+options.dataEra+" not supported for this config: USE dataEra=2016/2017")
else:
    raise Exception("Problem with isData option! This should never happen!")


# this is needed when using crab 
# when crab imports the configuration file it will test run it and if no inputfiles are preset the program will terminate because L#110
if not options.inputFiles:
    if not options.isData:
        if "2016" in options.dataEra:
            options.inputFiles=['file:///pnfs/desy.de/cms/tier2/store/user/vanderli/ttH_4f_ctcvcp_TuneCP5_13TeV_madgraph_pythia8/KIT_tthbb_sl_skims_MC_94X_LEG_2016/191218_102941/0000/Skim_1.root']
        elif "2017" in options.dataEra: 
           options.inputFiles=['file:///pnfs/desy.de/cms/tier2/store/user/vanderli/TTH_4f_ctcvcp_TuneCP5_13TeV_madgraph_pythia8/KIT_tthbb_sl_skims_MC_94X_LEG_2017/191218_102702/0000/Skim_1.root']
      
        elif "2018" in options.dataEra:
            
            options.inputFiles=['file:///pnfs/desy.de/cms/tier2/store/user/vanderli/TTH_4f_ctcvcp_TuneCP5_13TeV_madgraph_pythia8/KIT_tthbb_sl_skims_MC_102X_LEG_2018/191218_103017/0000/Skim_1.root']
            
    else:
        if "2016" in options.dataEra: # CAREFUL: NO 2016 Data Skims ready yet
        	options.inputFiles=['file:///pnfs/desy.de/cms/tier2/store/user/pkeicher/SingleElectron/KIT_tthbb_sl_skims_DATA_94X_Run2017B/180617_220344/0000/Skim_1.root']
        elif "2017" in options.dataEra:
            options.inputFiles=['file:///pnfs/desy.de/cms/tier2//store/user/vanderli/SingleElectron/KIT_tthbb_sl_skims_DATA_94X_LEG_2017B/190607_140551/0000/Skim_526.root']
        elif "2018" in options.dataEra:
        	options.inputFiles=['file:///pnfs/desy.de/cms/tier2/store/user/mschrode/SingleMuon/KIT_tthbb_skims_DATA_94X_LEG_2018A/190406_082949/0000/Skim_1.root']
    
 

# checks for correct values and consistency
if "data" in options.globalTag.lower() and not options.isData:
    print "\n\nConfig ERROR: GT contains seems to be for data but isData==False\n\n"
    sys.exit()
if "mc" in options.globalTag.lower() and options.isData:
    print "\n\nConfig ERROR: GT contains seems to be for MC but isData==True\n\n"
    sys.exit()
if not options.inputFiles:
    print "\n\nConfig ERROR: no inputFiles specified\n\n"
    sys.exit()
if not options.dataset in datasets:
    print options.dataset,'not an allowed dataset, options are',datasets
    sys.exit()

# print settings
print "\n\n***** JOB SETUP *************************"
for key in options._register:
    # do not print unused default options
    if key not in ["secondaryInputFiles","section","tag","totalSections","outputFile","secondaryOutputFile","filePrepend"]:
        print str(key)+" : "+str( options.__getattr__(key) )
print "*****************************************\n\n"

writeNominal=False
systsJES=[] 
systsJER=[]
if options.systematicVariations:
    for var in options.systematicVariations:
        if var == '':
            continue
        if var.lower() == "nominal":
            writeNominal=True
        elif var.startswith("JES"):
            systsJES.append( var+"up" )
            systsJES.append( var+"down")
        elif var.startswith("JER"):
            systsJER.append( var+"up" )
            systsJER.append( var+"down")
        else:
            print "ERROR: unknown variation '"+var+"'"
            sys.exit()
systs=systsJER+systsJES

if options.isData:
    systsJER=[]
    systsJES=[]
    systs=[]
    writeNominal=True

process = cms.Process("boostedAnalysis")

# cmssw options
process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10000
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = options.globalTag
process.load("CondCore.CondDB.CondDB_cfi")
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.options.allowUnscheduled = cms.untracked.bool(False)

# process.options.numberOfThreads=cms.untracked.uint32(8)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(int(options.maxEvents)))
process.source = cms.Source(  "PoolSource",
                              fileNames = cms.untracked.vstring(options.inputFiles),
                              skipEvents=cms.untracked.uint32(int(options.skipEvents)),
)
process.load('Configuration.Geometry.GeometryRecoDB_cff')
process.load("Configuration.StandardSequences.MagneticField_38T_cff")

# ------------------------------------------------------------------------------------------------------------------------------------------------- #

# Add producer calculating the L1 prefire weights
# https://twiki.cern.ch/twiki/bin/view/CMS/L1PrefiringWeightRecipe#Call_the_producer_in_your_config

process.load("PhysicsTools.PatUtils.L1PrefiringWeightProducer_cff")
from PhysicsTools.PatUtils.l1PrefiringWeightProducer_cfi import l1PrefiringWeightProducer

if "2016preVFP" in options.dataEra:

   process.prefiringweight = l1PrefiringWeightProducer.clone(
        TheJets=cms.InputTag("CorrectedJetProducerAK4:correctedJetsAK4"),
        # TheJets = cms.InputTag("updatedPatJetsUpdatedJEC"), #this should be the slimmedJets collection with up to date JECs !
        DataEraECAL = cms.string("UL2016preVFP"),
        DataEraMuon = cms.string("2016preVFP"),
        UseJetEMPt = cms.bool(False),
        PrefiringRateSystematicUnctyECAL = cms.double(0.2),
        PrefiringRateSystematicUnctyMuon = cms.double(0.2)
        )

elif "2016postVFP" in options.dataEra:
   
   process.prefiringweight = l1PrefiringWeightProducer.clone(
        TheJets=cms.InputTag("CorrectedJetProducerAK4:correctedJetsAK4"),
        # TheJets = cms.InputTag("updatedPatJetsUpdatedJEC"), #this should be the slimmedJets collection with up to date JECs !
        DataEraECAL = cms.string("UL2016postVFP"),
        DataEraMuon = cms.string("2016postVFP"),
        UseJetEMPt = cms.bool(False),
        PrefiringRateSystematicUnctyECAL = cms.double(0.2),
        PrefiringRateSystematicUnctyMuon = cms.double(0.2)
        )

elif "2017" in options.dataEra:
   
   process.prefiringweight = l1PrefiringWeightProducer.clone(
        TheJets=cms.InputTag("CorrectedJetProducerAK4:correctedJetsAK4"),
        # TheJets = cms.InputTag("updatedPatJetsUpdatedJEC"), #this should be the slimmedJets collection with up to date JECs !
        DataEraECAL = cms.string("UL2017BtoF"),
        DataEraMuon = cms.string("20172018"),
        UseJetEMPt = cms.bool(False),
        PrefiringRateSystematicUnctyECAL = cms.double(0.2),
        PrefiringRateSystematicUnctyMuon = cms.double(0.2)
        )
elif "2018" in options.dataEra:

    process.prefiringweight = l1PrefiringWeightProducer.clone(
        TheJets=cms.InputTag("CorrectedJetProducerAK4:correctedJetsAK4"),
        # TheJets = cms.InputTag("updatedPatJetsUpdatedJEC"), #this should be the slimmedJets collection with up to date JECs !
        DataEraECAL = cms.string("None"),
        DataEraMuon = cms.string("20172018"),
        UseJetEMPt = cms.bool(False),
        PrefiringRateSystematicUnctyECAL = cms.double(0.2),
        PrefiringRateSystematicUnctyMuon = cms.double(0.2)
        )




# ReRun DeepJet
# from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection
# updateJetCollection(
#    process,
#    jetSource = cms.InputTag('slimmedJets'),
#    pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
#    svSource = cms.InputTag('slimmedSecondaryVertices'),
#    jetCorrections = ('AK4PFchs', cms.vstring(['L1FastJet', 'L2Relative', 'L3Absolute']), 'None'),
#    btagDiscriminators = [
#       'pfDeepFlavourJetTags:probb',
#       'pfDeepFlavourJetTags:probbb',
#       'pfDeepFlavourJetTags:problepb',
#       'pfDeepFlavourJetTags:probc',
#       'pfDeepFlavourJetTags:probuds',
#       'pfDeepFlavourJetTags:probg'
#       ],
#    postfix='NewDFTraining'
# )

# process.updateJets = cms.Task(
#                     process.patJetCorrFactorsNewDFTraining,
#                     process.patJetCorrFactorsTransientCorrectedNewDFTraining,
#                     process.pfDeepCSVTagInfosNewDFTraining, 
#                     process.pfDeepFlavourJetTagsNewDFTraining,
#                     process.pfDeepFlavourTagInfosNewDFTraining,
#                     process.pfImpactParameterTagInfosNewDFTraining,
#                     process.pfInclusiveSecondaryVertexFinderTagInfosNewDFTraining,
#                     process.selectedUpdatedPatJetsNewDFTraining,
#                     process.updatedPatJetsNewDFTraining,
#                     process.updatedPatJetsTransientCorrectedNewDFTraining)

# ------------------------------------------------------------------------------------------------------------------------------------------------- #

# Set up JetCorrections chain to be used in MiniAODHelper
# Note: name is hard-coded to ak4PFchsL1L2L3 and does not
# necessarily reflect actual corrections level
# TODO - figure out the funtion of following :
#
from JetMETCorrections.Configuration.JetCorrectionServices_cff import *
process.ak4PFCHSL1Fastjet = cms.ESProducer(
  'L1FastjetCorrectionESProducer',
  level = cms.string('L1FastJet'),
  algorithm = cms.string('AK4PFchs'),
  srcRho = cms.InputTag( 'fixedGridRhoFastjetAll' )
  )
process.ak4PFchsL2Relative = ak4CaloL2Relative.clone( algorithm = 'AK4PFchs' )
process.ak4PFchsL3Absolute = ak4CaloL3Absolute.clone( algorithm = 'AK4PFchs' )
process.ak4PFchsResidual = ak4CaloResidual.clone( algorithm = 'AK4PFchs' )
process.ak4PFchsL1L2L3 = cms.ESProducer("JetCorrectionESChain",
  correctors = cms.vstring(
    'ak4PFCHSL1Fastjet',
    'ak4PFchsL2Relative',
    'ak4PFchsL3Absolute')
)

if options.isData:
  process.ak4PFchsL1L2L3.correctors.append('ak4PFchsResidual') # add residual JEC for data

process.ak8PFCHSL1Fastjet = cms.ESProducer(
  'L1FastjetCorrectionESProducer',
  level = cms.string('L1FastJet'),
  algorithm = cms.string('AK8PFchs'),
  srcRho = cms.InputTag( 'fixedGridRhoFastjetAll' )
  )
process.ak8PFchsL2Relative = ak4CaloL2Relative.clone( algorithm = 'AK8PFchs' )
process.ak8PFchsL3Absolute = ak4CaloL3Absolute.clone( algorithm = 'AK8PFchs' )
process.ak8PFchsResidual = ak4CaloResidual.clone( algorithm = 'AK8PFchs' )
process.ak8PFchsL1L2L3 = cms.ESProducer("JetCorrectionESChain",
  correctors = cms.vstring(
    'ak8PFCHSL1Fastjet',
    'ak8PFchsL2Relative',
    'ak8PFchsL3Absolute')
)

if options.isData:
  process.ak8PFchsL1L2L3.correctors.append('ak8PFchsResidual') # add residual JEC for data


# ------------------------------------------------------------------------------------------------------------------------------------------------- #
  
# if options.recorrectMET:
    # This is EE noise in JET, not needed in UL
    # https://twiki.cern.ch/twiki/bin/view/CMS/MissingETUncertaintyPrescription#Instructions_for_2017_data_with
    # https://twiki.cern.ch/twiki/bin/view/CMS/JetMET#Quick_links_to_current_recommend
   
    # from PhysicsTools.PatUtils.tools.runMETCorrectionsAndUncertainties import runMetCorAndUncFromMiniAOD
    # runMetCorAndUncFromMiniAOD(process,
    #                            isData=options.isData,
    #                            fixEE2017 = True if "2017" in options.dataEra else False,
    #                            fixEE2017Params = {'userawPt': True, 'ptThreshold':50.0, 'minEtaThreshold':2.65, 'maxEtaThreshold': 3.139} 
    #                            )
#METCollection      = cms.InputTag("slimmedMETs", "", process.name_())

# ------------------------------------------------------------------------------------------------------------------------------------------------- #

# run ecalBadCalibReducedMINIAODFilter for 2017 data
# not neede in UL
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2#2018_2017_data_and_MC_UL
# if "2017" or "2018" in options.dataEra:
#     process.load('RecoMET.METFilters.ecalBadCalibFilter_cfi')

#     baddetEcallist = cms.vuint32(
#         [872439604,872422825,872420274,872423218,
#         872423215,872416066,872435036,872439336,
#         872420273,872436907,872420147,872439731,
#         872436657,872420397,872439732,872439339,
#         872439603,872422436,872439861,872437051,
#         872437052,872420649,872422436,872421950,
#         872437185,872422564,872421566,872421695,
#         872421955,872421567,872437184,872421951,
#         872421694,872437056,872437057,872437313])


#     process.ecalBadCalibReducedMINIAODFilter = cms.EDFilter(
#         "EcalBadCalibFilter",
#         EcalRecHitSource = cms.InputTag("reducedEgamma:reducedEERecHits"),
#         ecalMinEt        = cms.double(50.),
#         baddetEcal    = baddetEcallist, 
#         taggingMode = cms.bool(True),
#         debug = cms.bool(False)
#         )
    
# ------------------------------------------------------------------------------------------------------------------------------------------------- #

### E/Gamma recommendations ###  

### Electron scale and smearing corrections ### 
# 2017UL and 2018UL already have the corrections ()
# But scale systematics are applied to data and not to MC
# If you are not using the samples above, or you prefer (as we recommend) to apply the scale systematics to the MC, please check the steps below for including the scale and smearing corrections on the fly in your analysis ("Recipe for running scales and smearings using EgammaPostRecoTools ").
# https://twiki.cern.ch/twiki/bin/view/CMS/EgammaUL2016To2018#Recipe_for_running_scales_and_sm
from RecoEgamma.EgammaTools.EgammaPostRecoTools import setupEgammaPostRecoSeq
EG_era = None
EG_corrections = None
EG_vid = None
if "2016preVFP" in options.dataEra:
    EG_era = '2016preVFP-UL'
    EG_corrections = True
    EG_vid = False
elif "2016postVFP" in options.dataEra:
    EG_era = '2016postVFP-UL'
    EG_corrections = True
    EG_vid = False
elif "2017" in options.dataEra:
    EG_era = '2017-UL'
    EG_corrections = True
    EG_vid = False
    # EG_corrections = False
    # EG_vid = False
elif "2018" in options.dataEra:
    EG_era = '2018-UL'
    EG_corrections = True
    EG_vid = False
else:
    raise Exception( "dataEra "+options.dataEra+" not supported for Egamma tools: USE dataEra=2016/2017/2018")

setupEgammaPostRecoSeq(process,
                       runVID=EG_vid,
                       runEnergyCorrections=EG_corrections,
                       era=EG_era
                       )
# a sequence egammaPostRecoSeq has now been created and should be added to your path, eg process.p=cms.Path(process.egammaPostRecoSeq)

# ------------------------------------------------------------------------------------------------------------------------------------------------- #


### some standard collections ####
#if not options.isData:
electronCollection = cms.InputTag("slimmedElectrons")
photonCollection   = cms.InputTag("slimmedPhotons")
muonCollection     = cms.InputTag("slimmedMuons")
tauCollection      = cms.InputTag("slimmedTaus")
METCollection      = cms.InputTag("slimmedMETs")
jetCollection      = cms.InputTag("slimmedJets")
# AK8jetCollection   = cms.InputTag("slimmedJetsAK8","","PAT")


###### deterministic seed producer ######

if options.deterministicSeeds:
    process.load("PhysicsTools.PatUtils.deterministicSeeds_cfi")
    process.deterministicSeeds.produceCollections = cms.bool(True)
    process.deterministicSeeds.produceValueMaps   = cms.bool(False)
    process.deterministicSeeds.electronCollection = electronCollection
    process.deterministicSeeds.muonCollection     = muonCollection
    process.deterministicSeeds.tauCollection      = tauCollection
    process.deterministicSeeds.photonCollection   = photonCollection
    process.deterministicSeeds.jetCollection      = jetCollection
    process.deterministicSeeds.METCollection      = METCollection
    #process.deterministicSeeds.AK8jetCollection   = AK8jetCollection

    # overwrite output collections
    electronCollection = cms.InputTag("deterministicSeeds", "electronsWithSeed", process.name_())
    muonCollection     = cms.InputTag("deterministicSeeds", "muonsWithSeed", process.name_())
    tauCollection      = cms.InputTag("deterministicSeeds", "tausWithSeed", process.name_())
    photonCollection   = cms.InputTag("deterministicSeeds", "photonsWithSeed", process.name_())
    jetCollection      = cms.InputTag("deterministicSeeds", "jetsWithSeed", process.name_())
    METCollection      = cms.InputTag("deterministicSeeds", "METsWithSeed", process.name_())
    #AK8jetCollection   = cms.InputTag("deterministicSeeds", "AK8jetsWithSeed", process.name_())

# ------------------------------------------------------------------------------------------------------------------------------------------------- #
# lepton selection
#process.load('BoostedTTH.Producers.SelectedLeptonProducers_cfi')
from BoostedTTH.Producers.SelectedLeptonProducers_cfi import *
if "2016preVFP" in options.dataEra:
    process.SelectedElectronProducer = SelectedElectronProducer2016preVFP
    process.SelectedElectronProducer.ptMins=[15.,15.,29.]
    ###
    process.SelectedMuonProducer = SelectedMuonProducer2016preVFP
    process.SelectedMuonProducer.ptMins=[15.,15.,26.]
elif "2016postVFP" in options.dataEra:
    process.SelectedElectronProducer = SelectedElectronProducer2016postVFP
    process.SelectedElectronProducer.ptMins=[15.,15.,29.]
    ###
    process.SelectedMuonProducer = SelectedMuonProducer2016postVFP
    process.SelectedMuonProducer.ptMins=[15.,15.,26.]
elif "2017" in options.dataEra:
    process.SelectedElectronProducer = SelectedElectronProducer2017
    process.SelectedElectronProducer.ptMins=[15.,15.,30.]
    ###
    process.SelectedMuonProducer = SelectedMuonProducer2017
    process.SelectedMuonProducer.ptMins=[15.,15.,29.]
elif "2018" in options.dataEra:
    process.SelectedElectronProducer = SelectedElectronProducer2018
    process.SelectedElectronProducer.ptMins=[15.,15.,30.]
    ###
    process.SelectedMuonProducer = SelectedMuonProducer2018
    process.SelectedMuonProducer.ptMins=[15.,15.,26.]
    

process.SelectedElectronProducer.leptons=electronCollection
process.SelectedElectronProducer.etaMaxs=[2.4,2.4,2.4]
process.SelectedElectronProducer.leptonIDs=["tight","tight","tight"]
process.SelectedElectronProducer.isoConeSizes=[""]*3
process.SelectedElectronProducer.isoCorrTypes=["rhoEA"]*3
process.SelectedElectronProducer.collectionNames=["selectedElectronsLoose","selectedElectronsDL","selectedElectrons"]
process.SelectedElectronProducer.isData=options.isData
process.SelectedElectronProducer.era=options.dataEra


process.SelectedMuonProducer.leptons=muonCollection
process.SelectedMuonProducer.etaMaxs=[2.4,2.4,2.4]
process.SelectedMuonProducer.leptonIDs=["tight","tight","tight"]
# change the muon isolation cut to miniPF relative isolation 
process.SelectedMuonProducer.isoConeSizes=[""]*3
process.SelectedMuonProducer.isoCorrTypes=["rhoEA"]*3
# muon iso change to miniPF isolation miniPFRelIso_all < 0.2, corresponds to medium WP
# see https://github.com/cms-sw/cmssw/blob/master/DataFormats/MuonReco/interface/Muon.h
process.SelectedMuonProducer.muonIsoTypes = ["loose", "loose", "medium"]
process.SelectedMuonProducer.collectionNames=["selectedMuonsLoose","selectedMuonsDL","selectedMuons"]
process.SelectedMuonProducer.useMuonRC=options.useMuonRC
process.SelectedMuonProducer.useDeterministicSeeds=options.deterministicSeeds
process.SelectedMuonProducer.isData=options.isData
process.SelectedMuonProducer.era=options.dataEra

# ------------------------------------------------------------------------------------------------------------------------------------------------- #

# jet selection
process.load("BoostedTTH.Producers.SelectedJetProducer_cfi")
process.SelectedJetProducerAK4=process.SelectedJetProducer.clone()
# selection of corrected and smeared jets -- one producer for every jet systematic that selects two collections (regular and loose jets) each
# selection of the nominal jets
process.SelectedJetProducerAK4.jets=cms.InputTag('patSmearedJetsAK4',"",process.name_())
process.SelectedJetProducerAK4.applyCorrection=False
process.SelectedJetProducerAK4.ptMins=[20,30] # original [30, 30]
if options.ProduceMemNtuples==True:
    process.SelectedJetProducerAK4.ptMins=[10,30]
process.SelectedJetProducerAK4.etaMaxs=[4.0,2.4] # original [4.7,2.4]
process.SelectedJetProducerAK4.collectionNames=["selectedJetsLooseAK4","selectedJetsAK4"]
process.SelectedJetProducerAK4.systematics=[""]
process.SelectedJetProducerAK4.PUJetIDMins=["loose","loose"]
process.SelectedJetProducerAK4.JetID=["none","none"]
process.SelectedJetProducerAK4.era= options.dataEra
process.SelectedJetProducerAK4.isData= options.isData
# selection of the systematically shifted jets
for syst in systs:
    setattr(process,'SelectedJetProducerAK4'+syst,process.SelectedJetProducerAK4.clone(jets='patSmearedJetsAK4'+syst,collectionNames=[n+syst for n in list(process.SelectedJetProducerAK4.collectionNames)]))

# correction of  miniAOD jets -- one producer creates a jet collection for nominal JES and every JES systematic
process.CorrectedJetProducerAK4=process.SelectedJetProducerAK4.clone(jets=jetCollection, 
                                                               ptMins=[-1.],
                                                               etaMaxs=[999.],
                                                               collectionNames=["correctedJetsAK4"],
                                                               applyCorrection=True,
                                                               systematics=[""]+systsJES,
                                                               JetID=["tightlepveto"],
                                                               PUJetIDMins=["none"])

# Rerun pileupJetID for 2016 and 2017 UL after JEC correction above
# https://twiki.cern.ch/twiki/bin/view/CMS/PileupJetIDUL#Data_MC_Efficiency_Scale_Factors

process.load("RecoJets.JetProducers.PileupJetID_cfi")
if "2016postVFP" in options.dataEra:
    from RecoJets.JetProducers.PileupJetID_cfi import _chsalgos_106X_UL16
    process.pileupJetIdUpdated = process.pileupJetId.clone(
        jets=cms.InputTag("CorrectedJetProducerAK4:correctedJetsAK4"),
        inputIsCorrected=True,
        applyJec=False,
        vertexes=cms.InputTag("offlineSlimmedPrimaryVertices"),
        algos=cms.VPSet(_chsalgos_106X_UL16),
    )

elif "2016preVFP" in options.dataEra:
    from RecoJets.JetProducers.PileupJetID_cfi import _chsalgos_106X_UL16APV
    process.pileupJetIdUpdated = process.pileupJetId.clone(
        jets=cms.InputTag("CorrectedJetProducerAK4:correctedJetsAK4"),
        inputIsCorrected=True,
        applyJec=False,
        vertexes=cms.InputTag("offlineSlimmedPrimaryVertices"),
        algos=cms.VPSet(_chsalgos_106X_UL16APV),
    )

elif "2018" in options.dataEra:
    from RecoJets.JetProducers.PileupJetID_cfi import _chsalgos_106X_UL18
    process.pileupJetIdUpdated = process.pileupJetId.clone(
        jets=cms.InputTag("CorrectedJetProducerAK4:correctedJetsAK4"),
        inputIsCorrected=True,
        applyJec=False,
        vertexes=cms.InputTag("offlineSlimmedPrimaryVertices"),
        algos=cms.VPSet(_chsalgos_106X_UL18),
    )

# smearing of corrected jets -- producers that create the nominal and up/down JER correction
# jer shift of nominal sample
# no files for Summer20UL campaign 
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetResolution#Smearing_procedures
# https://github.com/cms-jet/JRDatabase/tree/master/textFiles
if "2016preVFP" in options.dataEra:
    jerResFileAK4 = "Summer20UL16APV_JRV3_MC_PtResolution_AK4PFchs.txt"
    # jerEtaFileAK4 = "Summer20UL16APV_JRV3_MC_EtaResolution_AK4PFchs.txt"
    # jerPhiFileAK4 = "Summer20UL16APV_JRV3_MC_PhiResolution_AK4PFchs.txt"
    # jerResFileAK8 = "Summer16_25nsV1_MC_PtResolution_AK8PFchs.txt"
    jerSFFileAK4 = "Summer20UL16APV_JRV3_MC_SF_AK4PFchs.txt"
    # jerSFFileAK8 = "Summer16_25nsV1_MC_SF_AK8PFchs.txt"
elif "2016postVFP" in options.dataEra:
    jerResFileAK4 = "Summer20UL16_JRV3_MC_PtResolution_AK4PFchs.txt"
    # jerEtaFileAK4 = "Summer20UL16_JRV3_MC_EtaResolution_AK4PFchs.txt"
    # jerPhiFileAK4 = "Summer20UL16_JRV3_MC_PhiResolution_AK4PFchs.txt"
    # jerResFileAK8 = "Summer16_25nsV1_MC_PtResolution_AK8PFchs.txt"
    jerSFFileAK4 = "Summer20UL16_JRV3_MC_SF_AK4PFchs.txt"
    # jerSFFileAK8 = "Summer16_25nsV1_MC_SF_AK8PFchs.txt"
elif "2017" in options.dataEra:
    jerResFileAK4 = "Summer19UL17_JRV2_MC_PtResolution_AK4PFchs.txt"
    # jerResFileAK8 = "Fall17_V3_MC_PtResolution_AK8PFchs.txt"
    jerSFFileAK4 = "Summer19UL17_JRV2_MC_SF_AK4PFchs.txt"
    # jerSFFileAK8 = "Fall17_V3_MC_SF_AK8PFchs.txt"
elif "2018" in options.dataEra:
    jerResFileAK4 = "Summer19UL18_JRV2_MC_PtResolution_AK4PFchs.txt"
    # jerEtaFileAK4 = "Summer19UL18_JRV2_MC_EtaResolution_AK4PFchs.txt"
    # jerPhiFileAK4 = "Summer19UL18_JRV2_MC_PhiResolution_AK4PFchs.txt"
    # jerResFileAK8 = "Summer16_25nsV1_MC_PtResolution_AK8PFchs.txt"
    jerSFFileAK4 = "Summer19UL18_JRV2_MC_SF_AK4PFchs.txt"
    # jerSFFileAK8 = "Summer16_25nsV1_MC_SF_AK8PFchs.txt"
else:
    raise Exception("NO JER FILES SPECIFIED: USE dataEra=2016/2017/2018")

process.patSmearedJetsAK4 = cms.EDProducer("SmearedPATJetProducer",
    src = cms.InputTag("CorrectedJetProducerAK4:correctedJetsAK4"),
    enabled = cms.bool(True),  # If False, no smearing is performed
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    skipGenMatching = cms.bool(False),  # If True, always skip gen jet matching and smear jet with a random gaussian
    #algopt = cms.string('AK4PFchs_pt'),
    #algo = cms.string('AK4PFchs'),
    genJets = cms.InputTag("slimmedGenJets","","PAT"),
    dRMax = cms.double(0.2),  # = cone size (0.4) / 2
    dPtMaxFactor = cms.double(3),  # dPt < 3 * resolution
    variation = cms.int32(0),  # systematic +1 0 -1 sigma
    debug = cms.untracked.bool(False),
    useDeterministicSeed=cms.bool(False),# default deterministic seeds not used, but our own
    resolutionFile = cms.FileInPath("BoostedTTH/BoostedAnalyzer/data/jerfiles/" + jerResFileAK4),
    scaleFactorFile = cms.FileInPath("BoostedTTH/BoostedAnalyzer/data/jerfiles/" + jerSFFileAK4),
)



for s in systsJER:
    v=0
    if s=='JERup': v=+1
    # https://github.com/cms-sw/cmssw/blob/CMSSW_10_6_X/PhysicsTools/PatUtils/interface/SmearedJetProducerT.h
    # default producer does not have separate JER variaitons
    # git cms-merge-topic sebwieland:CMSSW_10_2_X_SmearedJetProducer
    # elif s=='JEReta0up': v=+2
    # elif s=='JEReta1up': v=+3
    # elif s=='JERpt0eta2up': v=+4
    # elif s=='JERpt1eta2up': v=+5
    # elif s=='JERpt0eta3up': v=+6
    # elif s=='JERpt1eta3up': v=+7

    if s=='JERdown': v=-1
    # elif s=='JEReta0down': v=-2
    # elif s=='JEReta1down': v=-3
    # elif s=='JERpt0eta2down': v=-4
    # elif s=='JERpt1eta2down': v=-5
    # elif s=='JERpt0eta3down': v=-6
    # elif s=='JERpt1eta3down': v=-7
    
    setattr(process,'patSmearedJetsAK4'+s,process.patSmearedJetsAK4.clone(variation=v,src=cms.InputTag("CorrectedJetProducerAK4:correctedJetsAK4")))
    # setattr(process,'patSmearedJetsAK8'+s,process.patSmearedJetsAK8.clone(variation=v,src=cms.InputTag("CorrectedJetProducerAK8:correctedJetsAK8")))
for s in systsJES:
    setattr(process,'patSmearedJetsAK4'+s,process.patSmearedJetsAK4.clone(variation=0,src=cms.InputTag("CorrectedJetProducerAK4:correctedJetsAK4"+s)))
    # setattr(process,'patSmearedJetsAK8'+s,process.patSmearedJetsAK8.clone(variation=0,src=cms.InputTag("CorrectedJetProducerAK8:correctedJetsAK8"+s)))


# ------------------------------------------------------------------------------------------------------------------------------------------------- #

# load and run the boosted analyzer
if options.isData:
    from BoostedTTH.BoostedAnalyzer.BoostedAnalyzer_data_cfi import *
    if "2016" in options.dataEra:
        process.BoostedAnalyzer = BoostedAnalyzer2016
    elif "2017" in options.dataEra:
        process.BoostedAnalyzer = BoostedAnalyzer2017
    elif "2018" in options.dataEra:
        process.BoostedAnalyzer = BoostedAnalyzer2018
    
    process.BoostedAnalyzer.filterBits=cms.InputTag("TriggerResults::RECO")
    process.BoostedAnalyzer.dataEra=options.dataEra

else:
    from BoostedTTH.BoostedAnalyzer.BoostedAnalyzer_cfi import *
    if "2016preVFP" in options.dataEra:
        process.BoostedAnalyzer = BoostedAnalyzer2016preVFP
    if "2016postVFP" in options.dataEra:
        process.BoostedAnalyzer = BoostedAnalyzer2016postVFP
    elif "2017" in options.dataEra:
        process.BoostedAnalyzer = BoostedAnalyzer2017
    elif "2018" in options.dataEra:
        process.BoostedAnalyzer = BoostedAnalyzer2018
    
    process.BoostedAnalyzer.dataEra=options.dataEra

    if not options.isBoostedMiniAOD:
        # Supplies PDG ID to real name resolution of MC particles
        process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
        # Needed to determine tt+x category -- is usually run when producing boosted jets in miniAOD
        process.load("BoostedTTH.Producers.genHadronMatching_cfi")

# which systematic variations to store in the ntuple?
variations = systs
if writeNominal:
    variations.insert(0,"") # also store nominal case
process.BoostedAnalyzer.selectedJets=[cms.InputTag("SelectedJetProducerAK4"+s+":selectedJetsAK4"+s) for s in variations]
process.BoostedAnalyzer.selectedJetsLoose=[cms.InputTag("SelectedJetProducerAK4"+s+":selectedJetsLooseAK4"+s) for s in variations]
process.BoostedAnalyzer.AK8Jets=[cms.InputTag("slimmedJets") for s in variations]
process.BoostedAnalyzer.correctedMETs=[METCollection]*(len(variations))

if options.isBoostedMiniAOD:
    process.BoostedAnalyzer.useFatJets=True
else:
    process.BoostedAnalyzer.useFatJets=False

process.BoostedAnalyzer.outfileName=options.outName
if not options.isData:
    process.BoostedAnalyzer.eventWeight = options.weight

process.BoostedAnalyzer.systematics=variations
process.BoostedAnalyzer.generatorName=options.generatorName

if options.isData and options.useJson:
    # TODO - change the lumi files when data is included
    # https://twiki.cern.ch/twiki/bin/view/CMS/LumiRecommendationsRun2#2018
    import FWCore.PythonUtilities.LumiList as LumiList
    if "2016" in options.dataEra:
        process.source.lumisToProcess = LumiList.LumiList(filename = os.getenv('CMSSW_BASE')+"/src/BoostedTTH/BoostedAnalyzer/data/lumi_jsons/Cert_271036-284044_13TeV_ReReco_07Aug2017_Collisions16_JSON.txt").getVLuminosityBlockRange()
    elif "2017" in options.dataEra:
        process.source.lumisToProcess = LumiList.LumiList(filename = os.getenv('CMSSW_BASE')+"/src/BoostedTTH/BoostedAnalyzer/data/lumi_jsons/Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON_v1.txt").getVLuminosityBlockRange()
    elif "2018" in options.dataEra:
        process.source.lumisToProcess = LumiList.LumiList(filename = os.getenv('CMSSW_BASE')+"/src/BoostedTTH/BoostedAnalyzer/data/lumi_jsons/Cert_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_JSON.txt").getVLuminosityBlockRange()

if options.isData:
  process.BoostedAnalyzer.dataset=cms.string(options.dataset)


process.BoostedAnalyzer.selectionNames = [
"FilterSelection",
"VertexSelection",
"LeptonSelection",
"JetTagSelection",
"METSelection"
]
if options.additionalSelection!="NONE":
  process.BoostedAnalyzer.selectionNames+=cms.vstring(options.additionalSelection)

if options.isData:
  process.BoostedAnalyzer.processorNames=cms.vstring(
  "WeightProcessor",
  "essentialBasicVarProcessor",
  "essentialMVAVarProcessor",
  "essentialRecoVarProcessor",
  "TriggerVarProcessor",
  "JABDTttbarProcessor",
  "JABDTthhProcessor",  
#  "JABDTtthProcessor",
  )
else:
  process.BoostedAnalyzer.processorNames=cms.vstring(
  "WeightProcessor",
  "MCMatchVarProcessor",
  "essentialBasicVarProcessor",
  "essentialMVAVarProcessor",
  "essentialRecoVarProcessor",
  "TriggerVarProcessor",
#   "JABDTttbarProcessor",
#   "JABDTthhProcessor",
#  "JABDTtthProcessor",
  )
if (process.BoostedAnalyzer.taggingSelection): process.BoostedAnalyzer.processorNames.append("SelectionTagProcessor")


printContent=False
if printContent:
    process.content = cms.EDAnalyzer("EventContentAnalyzer")

if options.dumpSyncExe:
    process.BoostedAnalyzer.processorNames = []
    process.BoostedAnalyzer.selectionNames = []
    process.BoostedAnalyzer.dumpSyncExe=True
    process.BoostedAnalyzer.dumpExtended=False
    process.BoostedAnalyzer.dumpAlwaysEvents=[
        # 2876878,
        # 2876882,
        # 2877695,
        # 2877028,
        # 2877912,
        # 7984609,
        # 7772477,
        2878485
        #3222838,
        #3211421,
        #527273,
        #3163883,
        #2865714,
        #2688365,
        #2786936,
        ]

if options.ProduceMemNtuples==True:
    process.BoostedAnalyzer.memNtuples=True
    process.BoostedAnalyzer.processorNames=cms.vstring("SlimmedNtuples")

# ------------------------------------------------------------------------------------------------------------------------------------------------- #

##### DEFINE PATH ##########
process.p = cms.Path()

# rerun DeepJet
# process.p.associate(process.updateJets)

# run ecalBadCalibReducedMINIAODFilter for 2017/2018 data
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2#2018_2017_data_and_MC_UL
# Not neede anymore in UL 
# if "2017" or "2018" in options.dataEra:
#     process.BoostedAnalyzer.additionalFilters = cms.VInputTag(["ecalBadCalibReducedMINIAODFilter"])
#     process.p *= process.ecalBadCalibReducedMINIAODFilter

# not needed naymore for UL
# https://twiki.cern.ch/twiki/bin/view/CMS/JetMET#Quick_links_to_current_recommend
# if options.recorrectMET:
#     process.p *= process.fullPatMetSequence

# electron scale and smearing corrections    
process.p *= process.egammaPostRecoSeq

if options.deterministicSeeds:
    process.p*=process.deterministicSeeds

process.p*=process.SelectedElectronProducer*process.SelectedMuonProducer

process.p*=process.CorrectedJetProducerAK4
# process.p*=process.CorrectedJetProducerAK8
# always produce (but not necessarily write to ntuple) nominal case as collections might be needed                                    

if "2016" in options.dataEra or "2018" in options.dataEra:
    process.p *= process.pileupJetIdUpdated

for s in [""]+systs:
    process.p *= getattr(process,'patSmearedJetsAK4'+s)
    # process.p *= getattr(process,'patSmearedJetsAK8'+s)
    process.p *= getattr(process,'SelectedJetProducerAK4'+s)
    # process.p *= getattr(process,'SelectedJetProducerAK8'+s)


if not options.isData and not options.isBoostedMiniAOD:
    process.p *= process.genParticlesForJetsNoNu*process.ak4GenJetsCustom*process.selectedHadronsAndPartons*process.genJetFlavourInfos*process.matchGenBHadron*process.matchGenCHadron*process.categorizeGenTtbar

#if "2018" not in options.dataEra:
process.p += process.prefiringweight

if printContent:
    process.p *= process.content

process.p *= process.BoostedAnalyzer
