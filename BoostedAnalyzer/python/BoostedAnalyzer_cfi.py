import FWCore.ParameterSet.Config as cms
from BoostedTTH.BoostedAnalyzer.Selection_cff import *

BoostedAnalyzer = cms.EDAnalyzer(
    'BoostedAnalyzer',
    LeptonSelection,
    JetTagSelection,  
    relevantTriggers = cms.vstring("HLT_IsoMu24_eta2p1_IterTrk02_v1","HLT_Ele27_eta2p1_WP85_Gsf_v1","HLT_Ele23_Ele12_CaloId_TrackId_Iso_v1","HLT_Mu30_TkMu11_v1","HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_v1","HLT_Mu17_TrkIsoVVL_TkMu8_TrkIsoVVL_v1","HLT_Mu23_TrkIsoVVL_Ele12_Gsf_CaloId_TrackId_Iso_MediumWP_v1","HLT_Mu8_TrkIsoVVL_Ele23_Gsf_CaloId_TrackId_Iso_MediumWP_v1"),
    era = cms.string("2012_53x"),
    analysisType = cms.string("LJ"),
    luminosity = cms.double(19.7),
    sampleID = cms.int32(9125),
    xs = cms.double(248),
    nMCEvents = cms.int32(25000000),
    isData = cms.bool(False),
    useFatJets = cms.bool(False),
    disableObjectSelections = cms.bool(False), # disables selection of some objects for synch exe
    outfileName = cms.string("BoostedTTH"),
    selectionNames = cms.vstring("VertexSelection","LeptonSelection"),
    processorNames = cms.vstring("WeightProcessor","MCMatchVarProcessor","MVAVarProcessor","BDTVarProcessor","BoostedJetVarProcessor","BoostedTopHiggsVarProcessor","BoostedTopVarProcessor","BoostedHiggsVarProcessor")
)
