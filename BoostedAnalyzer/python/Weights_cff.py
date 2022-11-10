import FWCore.ParameterSet.Config as cms

# PU weights
# ------------------------------------------------------------

#2018
NominalPUWeight2018 = cms.PSet(
    fileNameMCNPU = cms.string("MiniAOD/MiniAODHelper/data/puweights/MC/N_True2018.root"),
    histNameMCNPU = cms.string("N_True"),
    fileNameDataNPUEstimated = cms.string("MiniAOD/MiniAODHelper/data/puweights/Run2017/DataPileupHistogram_Run2017_294927-306462_13TeV_EOY2017ReReco_MinBiasNominal-69200.root"),
    histNameDataNPUEstimated = cms.string("pileup")
)
AdditionalPUWeights2018 = cms.VPSet(
  cms.PSet(
    namePUWeight = cms.string("Weight_pu69p2"),
    fileNameMCNPU = cms.string("MiniAOD/MiniAODHelper/data/puweights/MC/N_True2018.root"),
    histNameMCNPU = cms.string("N_True"),
    fileNameDataNPUEstimated = cms.string("MiniAOD/MiniAODHelper/data/puweights/Run2018/DataPileupHistogram_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_MinBiasNominal-69200.root"),
    histNameDataNPUEstimated = cms.string("pileup")
  ),

  cms.PSet(
    namePUWeight = cms.string("Weight_pu69p2Up"),
    fileNameMCNPU = cms.string("MiniAOD/MiniAODHelper/data/puweights/MC/N_True2018.root"),
    histNameMCNPU = cms.string("N_True"),
    fileNameDataNPUEstimated = cms.string("MiniAOD/MiniAODHelper/data/puweights/Run2018/DataPileupHistogram_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_MinBiasUp-72383.root"),
    histNameDataNPUEstimated = cms.string("pileup")
  ),

  cms.PSet(
    namePUWeight = cms.string("Weight_pu69p2Down"),
    fileNameMCNPU = cms.string("MiniAOD/MiniAODHelper/data/puweights/MC/N_True2018.root"),
    histNameMCNPU = cms.string("N_True"),
    fileNameDataNPUEstimated = cms.string("MiniAOD/MiniAODHelper/data/puweights/Run2018/DataPileupHistogram_314472-325175_13TeV_17SeptEarlyReReco2018ABC_PromptEraD_Collisions18_MinBiasDown-66017.root"),
    histNameDataNPUEstimated = cms.string("pileup")
  ),
)

#2017
NominalPUWeight2017 = cms.PSet(
    fileNameMCNPU = cms.string("MiniAOD/MiniAODHelper/data/puweights/MC/MCNPUTrue.root"),
    histNameMCNPU = cms.string("MCPUDistributionProducer/NumTruePU"),
    fileNameDataNPUEstimated = cms.string("MiniAOD/MiniAODHelper/data/puweights/Run2017/DataPileupHistogram_Run2017_294927-306462_13TeV_EOY2017ReReco_MinBiasNominal-69200.root"),
    histNameDataNPUEstimated = cms.string("pileup")
)
AdditionalPUWeights2017 = cms.VPSet(
  cms.PSet(
    namePUWeight = cms.string("Weight_pu69p2"),
    fileNameMCNPU = cms.string("MiniAOD/MiniAODHelper/data/puweights/MC/MCNPUTrue.root"),
    histNameMCNPU = cms.string("MCPUDistributionProducer/NumTruePU"),
    fileNameDataNPUEstimated = cms.string("MiniAOD/MiniAODHelper/data/puweights/Run2017/DataPileupHistogram_Run2017_294927-306462_13TeV_EOY2017ReReco_MinBiasNominal-69200.root"),
    histNameDataNPUEstimated = cms.string("pileup")
  ),

  cms.PSet(
    namePUWeight = cms.string("Weight_pu69p2Up"),
    fileNameMCNPU = cms.string("MiniAOD/MiniAODHelper/data/puweights/MC/MCNPUTrue.root"),
    histNameMCNPU = cms.string("MCPUDistributionProducer/NumTruePU"),
    fileNameDataNPUEstimated = cms.string("MiniAOD/MiniAODHelper/data/puweights/Run2017/DataPileupHistogram_Run2017_294927-306462_13TeV_EOY2017ReReco_MinBiasUp-72383.root"),
    histNameDataNPUEstimated = cms.string("pileup")
  ),

  cms.PSet(
    namePUWeight = cms.string("Weight_pu69p2Down"),
    fileNameMCNPU = cms.string("MiniAOD/MiniAODHelper/data/puweights/MC/MCNPUTrue.root"),
    histNameMCNPU = cms.string("MCPUDistributionProducer/NumTruePU"),
    fileNameDataNPUEstimated = cms.string("MiniAOD/MiniAODHelper/data/puweights/Run2017/DataPileupHistogram_Run2017_294927-306462_13TeV_EOY2017ReReco_MinBiasDown-66017.root"),
    histNameDataNPUEstimated = cms.string("pileup")
  ),
)

# 2016
NominalPUWeight2016preVFP = cms.PSet(
    fileNameMCNPU = cms.string("MiniAOD/MiniAODHelper/data/puweights/MC/Summer16_NumTruePU.root"),
    histNameMCNPU = cms.string("hNumTruePUPdf"),
    fileNameDataNPUEstimated = cms.string("MiniAOD/MiniAODHelper/data/puweights/Run2016/DataPileupHistogram_Run2016-Complete_MinBias69200.root"),
    histNameDataNPUEstimated = cms.string("pileup")
)
AdditionalPUWeights2016preVFP = cms.VPSet(
  cms.PSet(
    namePUWeight = cms.string("Weight_pu69p2"),
    fileNameMCNPU = cms.string("MiniAOD/MiniAODHelper/data/puweights/MC/Summer16_NumTruePU.root"),
    histNameMCNPU = cms.string("hNumTruePUPdf"),
    fileNameDataNPUEstimated = cms.string("MiniAOD/MiniAODHelper/data/puweights/Run2016/DataPileupHistogram_Run2016-Complete_MinBias69200.root"),
    histNameDataNPUEstimated = cms.string("pileup")
  ),

  cms.PSet(
    namePUWeight = cms.string("Weight_pu69p2Up"),
    fileNameMCNPU = cms.string("MiniAOD/MiniAODHelper/data/puweights/MC/Summer16_NumTruePU.root"),
    histNameMCNPU = cms.string("hNumTruePUPdf"),
    fileNameDataNPUEstimated = cms.string("MiniAOD/MiniAODHelper/data/puweights/Run2016/DataPileupHistogram_Run2016-Complete_MinBias72383.root"),
    histNameDataNPUEstimated = cms.string("pileup")
  ),

  cms.PSet(
    namePUWeight = cms.string("Weight_pu69p2Down"),
    fileNameMCNPU = cms.string("MiniAOD/MiniAODHelper/data/puweights/MC/Summer16_NumTruePU.root"),
    histNameMCNPU = cms.string("hNumTruePUPdf"),
    fileNameDataNPUEstimated = cms.string("MiniAOD/MiniAODHelper/data/puweights/Run2016/DataPileupHistogram_Run2016-Complete_MinBias66017.root"),
    histNameDataNPUEstimated = cms.string("pileup")
  ),  
)


NominalPUWeight2016postVFP = cms.PSet(
    fileNameMCNPU = cms.string("MiniAOD/MiniAODHelper/data/puweights/MC/Summer16_NumTruePU.root"),
    histNameMCNPU = cms.string("hNumTruePUPdf"),
    fileNameDataNPUEstimated = cms.string("MiniAOD/MiniAODHelper/data/puweights/Run2016/DataPileupHistogram_Run2016-Complete_MinBias69200.root"),
    histNameDataNPUEstimated = cms.string("pileup")
)
AdditionalPUWeights2016postVFP = cms.VPSet(
  cms.PSet(
    namePUWeight = cms.string("Weight_pu69p2"),
    fileNameMCNPU = cms.string("MiniAOD/MiniAODHelper/data/puweights/MC/Summer16_NumTruePU.root"),
    histNameMCNPU = cms.string("hNumTruePUPdf"),
    fileNameDataNPUEstimated = cms.string("MiniAOD/MiniAODHelper/data/puweights/Run2016/DataPileupHistogram_Run2016-Complete_MinBias69200.root"),
    histNameDataNPUEstimated = cms.string("pileup")
  ),

  cms.PSet(
    namePUWeight = cms.string("Weight_pu69p2Up"),
    fileNameMCNPU = cms.string("MiniAOD/MiniAODHelper/data/puweights/MC/Summer16_NumTruePU.root"),
    histNameMCNPU = cms.string("hNumTruePUPdf"),
    fileNameDataNPUEstimated = cms.string("MiniAOD/MiniAODHelper/data/puweights/Run2016/DataPileupHistogram_Run2016-Complete_MinBias72383.root"),
    histNameDataNPUEstimated = cms.string("pileup")
  ),

  cms.PSet(
    namePUWeight = cms.string("Weight_pu69p2Down"),
    fileNameMCNPU = cms.string("MiniAOD/MiniAODHelper/data/puweights/MC/Summer16_NumTruePU.root"),
    histNameMCNPU = cms.string("hNumTruePUPdf"),
    fileNameDataNPUEstimated = cms.string("MiniAOD/MiniAODHelper/data/puweights/Run2016/DataPileupHistogram_Run2016-Complete_MinBias66017.root"),
    histNameDataNPUEstimated = cms.string("pileup")
  ),  
)


# B-tagging SF
# ------------------------------------------------------------

# The 94X DeepJet SF
BTagSFs94XDeepJet2018 = cms.PSet(
    fileNameHF = cms.string("MiniAOD/MiniAODHelper/data/sfs_deepjet_2018_hf.root"),
    nHFPtBins = cms.int32(5),
    nLFPtBins = cms.int32(4),
    nLFEtaBins = cms.int32(3),
    fileNameLF = cms.string("MiniAOD/MiniAODHelper/data/sfs_deepjet_2018_lf.root")
)
BTagSFs94XDeepJet2017 = cms.PSet(
    fileNameHF = cms.string("MiniAOD/MiniAODHelper/data/sfs_deepjet_2017_hf.root"),
    nHFPtBins = cms.int32(5),
    nLFPtBins = cms.int32(4),
    nLFEtaBins = cms.int32(3),
    fileNameLF = cms.string("MiniAOD/MiniAODHelper/data/sfs_deepjet_2017_lf.root")
)
BTagSFs94XDeepJet2016preVFP = cms.PSet(
    fileNameHF = cms.string("MiniAOD/MiniAODHelper/data/sfs_deepjet_2016_hf.root"),
    nHFPtBins = cms.int32(5),
    nLFPtBins = cms.int32(4),
    nLFEtaBins = cms.int32(3),
    fileNameLF = cms.string("MiniAOD/MiniAODHelper/data/sfs_deepjet_2016_lf.root")
)
BTagSFs94XDeepJet2016postVFP = cms.PSet(
    fileNameHF = cms.string("MiniAOD/MiniAODHelper/data/sfs_deepjet_2016_hf.root"),
    nHFPtBins = cms.int32(5),
    nLFPtBins = cms.int32(4),
    nLFEtaBins = cms.int32(3),
    fileNameLF = cms.string("MiniAOD/MiniAODHelper/data/sfs_deepjet_2016_lf.root")
)

# Trigger SFs

TriggerSFs2016preVFP = cms.PSet(
    elecFileName = cms.string("MiniAOD/MiniAODHelper/data/Run2Legacy/SingleEG_JetHT_Trigger_Scale_Factors_ttHbb2016_v2.root"),
    elecHistName = cms.string("ele27_ele_pt_ele_sceta"),
    muonFileName=cms.string(
        "MiniAOD/MiniAODHelper/data/leptonTriggerSF_UL/2016preVFP/Efficiencies_muon_generalTracks_Z_Run2016_UL_HIPM_SingleMuonTriggers.root"),
    muonHistName = cms.string("NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdTight_and_PFIsoTight_abseta_pt"),
)

TriggerSFs2016postVFP = cms.PSet(
    elecFileName = cms.string("MiniAOD/MiniAODHelper/data/Run2Legacy/SingleEG_JetHT_Trigger_Scale_Factors_ttHbb2016_v2.root"),
    elecHistName = cms.string("ele27_ele_pt_ele_sceta"),
    muonFileName=cms.string(
        "MiniAOD/MiniAODHelper/data/leptonTriggerSF_UL/2016preVFP/Efficiencies_muon_generalTracks_Z_Run2016_UL_SingleMuonTriggers.root"),
    muonHistName=cms.string(
        "NUM_IsoMu24_or_IsoTkMu24_DEN_CutBasedIdTight_and_PFIsoTight_abseta_pt"),
)

TriggerSFs2017 = cms.PSet(
    elecFileName = cms.string("MiniAOD/MiniAODHelper/data/Run2Legacy/SingleEG_JetHT_Trigger_Scale_Factors_ttHbb2017_v2.root"),
    elecHistName = cms.string("ele28_ht150_OR_ele32_ele_pt_ele_sceta"),
    muonFileName=cms.string(
        "MiniAOD/MiniAODHelper/data/leptonTriggerSF_UL/2016preVFP/Efficiencies_muon_generalTracks_Z_Run2017_UL_SingleMuonTriggers.root"),
    muonHistName=cms.string(
        "NUM_IsoMu27_DEN_CutBasedIdTight_and_PFIsoTight_abseta_pt"),
)

TriggerSFs2018 = cms.PSet(
    elecFileName = cms.string("MiniAOD/MiniAODHelper/data/Run2Legacy/SingleEG_JetHT_Trigger_Scale_Factors_ttHbb2018_v2.root"),
    elecHistName = cms.string("ele28_ht150_OR_ele32_ele_pt_ele_sceta"),
    muonFileName=cms.string(
        "MiniAOD/MiniAODHelper/data/leptonTriggerSF_UL/2016preVFP/Efficiencies_muon_generalTracks_Z_Run2018_UL_SingleMuonTriggers.root"),
    muonHistName=cms.string(
        "NUM_IsoMu24_DEN_CutBasedIdTight_and_PFIsoTight_abseta_pt"),
)



