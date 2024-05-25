import FWCore.ParameterSet.Config as cms
from BoostedTTH.BoostedAnalyzer.Selection_cff import *
from BoostedTTH.BoostedAnalyzer.Inputs_cff import *
from BoostedTTH.BoostedAnalyzer.Weights_cff import *
from BoostedTTH.BoostedAnalyzer.JetAssignment_cff import *

BoostedAnalyzer2017 = cms.EDAnalyzer(
    'BoostedAnalyzer',
    Inputs_TTHHUL_SL, # defined in Inputs_cff
    DiLeptonSelectionMC,  # defined in Selection_cff
    JetTagSelection, # defined in Selection_cff
    METSelection, # defined in Selection_cff
    checkBasicMCTriggers, # defined in Selection_cff
    # filtersMC, # defined in Selection_cff
    
    LeptonSelection = LeptonSelectionMC2017,
    
    # weight of one event: calculated as
    # cross section * lumi / (number of generated events with positive weight  -  number of generated events with negative weight )
    # so that the sum of weights corresponds to the number of events for the given lumi
    eventWeight = cms.double(1.),
    isData = cms.bool(False),
    dataset=cms.string("NA"),
    dataEra = cms.string("2017"),

    # turn off the SFs calculations as this will be updated later
    # will develop code after producing the ntuples
    # b-tag SF, defined in Weights_cff
    bTagSFs = BTagSFs94XDeepJet2017,

    # PU weights, defined in Weights_cff
    nominalPUWeight = NominalPUWeight2017,
    additionalPUWeights = AdditionalPUWeights2017,

    # information about lepton trigger SFs, defined in Weights_cff
    leptonTriggerSFInfos = TriggerSFs2017,
    # information about jet assignment weight .xml file
    
    JetAssignmentOptions = JetAssignment2017,
    #MET Filters
    METfilters = filtersMC1718,

    systematics = cms.vstring(""),
    doJERsystematic = cms.bool(False),

    generatorName = cms.string("notSpecified"),

    # this does not exist in the plugins
    # isreHLT = cms.bool(False),

    useFatJets = cms.bool(True),
    useForwardJets = cms.bool(False),
    useGenHadronMatch = cms.bool(True),

    dumpSyncExe = cms.bool(False),
    dumpExtended = cms.bool(False),
    dumpAlwaysEvents = cms.vint32(),
    doBoostedMEM = cms.bool(True),
    
    memNtuples = cms.bool(False),

    minJetsForMEM = cms.int32(4),
    minTagsForMEM = cms.int32(3),

    selectionNames = cms.vstring("VertexSelection","LeptonSelection"),
    processorNames = cms.vstring("WeightProcessor","MCMatchVarProcessor","BoostedMCMatchVarProcessor","BasicVarProcessor","MVAVarProcessor","BDTVarProcessor","TriggerVarProcessor","BoostedJetVarProcessor","BoostedTopHiggsVarProcessor", "AK8JetProcessor", "SelectionTagProcessor", "JABDTttbarProcessor"),
    outfileName = cms.string("BoostedTTH"),

    taggingSelection=cms.bool(False),
)

BoostedAnalyzer2017test = BoostedAnalyzer2017.clone(
    LeptonSelection=LeptonSelectionNoTrigger,
)

BoostedAnalyzer2016preVFP = BoostedAnalyzer2017.clone(
    LeptonSelection = LeptonSelectionMC2016,    
    dataEra = cms.string("2016preVFP"),
    bTagSFs = BTagSFs94XDeepJet2016preVFP,
    leptonTriggerSFInfos = TriggerSFs2016preVFP,
    nominalPUWeight=NominalPUWeight2016preVFP,
    additionalPUWeights=AdditionalPUWeights2016preVFP,
    METfilters = filtersMC16,
    JetAssignmentOptions=JetAssignment2016preVFP,

)
BoostedAnalyzer2016postVFP = BoostedAnalyzer2017.clone(
    LeptonSelection = LeptonSelectionMC2016,    
    dataEra = cms.string("2016postVFP"),
    bTagSFs = BTagSFs94XDeepJet2016postVFP,
    leptonTriggerSFInfos=TriggerSFs2016postVFP,
    nominalPUWeight=NominalPUWeight2016postVFP,
    additionalPUWeights=AdditionalPUWeights2016postVFP,
    METfilters = filtersMC16,
    JetAssignmentOptions = JetAssignment2016postVFP,

)

BoostedAnalyzer2018 = BoostedAnalyzer2017.clone(
    LeptonSelection = LeptonSelectionMC2018,
    dataEra = cms.string("2018"),
    bTagSFs = BTagSFs94XDeepJet2018,
    leptonTriggerSFInfos = TriggerSFs2018,
    nominalPUWeight = NominalPUWeight2018,
    additionalPUWeights = AdditionalPUWeights2018,
    JetAssignmentOptions = JetAssignment2018,

    
)

BoostedAnalyzer2016preVFPTrigger = BoostedAnalyzer2017.clone(
    LeptonSelection = LeptonSelectionMC2016Trigger,    
    dataEra = cms.string("2016preVFP"),
    bTagSFs = BTagSFs94XDeepJet2016preVFP,
    leptonTriggerSFInfos = TriggerSFs2016preVFP,
    nominalPUWeight=NominalPUWeight2016preVFP,
    additionalPUWeights=AdditionalPUWeights2016preVFP,
    METfilters = filtersMC16,
    JetAssignmentOptions=JetAssignment2016preVFP,

)
BoostedAnalyzer2016postVFPTrigger = BoostedAnalyzer2017.clone(
    LeptonSelection = LeptonSelectionMC2016Trigger,    
    dataEra = cms.string("2016postVFP"),
    bTagSFs = BTagSFs94XDeepJet2016postVFP,
    leptonTriggerSFInfos=TriggerSFs2016postVFP,
    nominalPUWeight=NominalPUWeight2016postVFP,
    additionalPUWeights=AdditionalPUWeights2016postVFP,
    METfilters = filtersMC16,
    JetAssignmentOptions = JetAssignment2016postVFP,

)

BoostedAnalyzer2018Trigger = BoostedAnalyzer2017.clone(
    LeptonSelection = LeptonSelectionMC2018Trigger,
    dataEra = cms.string("2018"),
    bTagSFs = BTagSFs94XDeepJet2018,
    leptonTriggerSFInfos = TriggerSFs2018,
    nominalPUWeight = NominalPUWeight2018,
    additionalPUWeights = AdditionalPUWeights2018,
    JetAssignmentOptions = JetAssignment2018,

    
)

BoostedAnalyzer2017Trigger = BoostedAnalyzer2017.clone(
    LeptonSelection = LeptonSelectionMC2017Trigger    
)