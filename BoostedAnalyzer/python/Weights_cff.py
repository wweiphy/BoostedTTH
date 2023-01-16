import FWCore.ParameterSet.Config as cms

# PU weights
# ------------------------------------------------------------

#2018
NominalPUWeight2018 = cms.PSet(
    fileNameMCNPU=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/MC/mcPileupUL2018.root"),
    histNameMCNPU=cms.string("pu_mc"),
    # fileNameMCNPU=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/MC/MCNPUTrue_18_UL.root"),
    # histNameMCNPU=cms.string("MCPUDistributionProducer/NumTruePU"),
    fileNameDataNPUEstimated=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/Run2018/PileupHistogram-UL2018-100bins_withVar.root"),
    histNameDataNPUEstimated = cms.string("pileup")
    # fileNameDataNPUEstimated=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/Run2017/PileupHistogram-goldenJSON-13tev-2018-69200ub-99bins.root"),
    # histNameDataNPUEstimated = cms.string("pileup")
)
AdditionalPUWeights2018 = cms.VPSet(
  cms.PSet(
    namePUWeight = cms.string("Weight_pu69p2"),
    fileNameMCNPU=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/MC/mcPileupUL2018.root"),
    histNameMCNPU=cms.string("pu_mc"),
    # fileNameMCNPU=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/MC/MCNPUTrue_18_UL.root"),
    # histNameMCNPU=cms.string("MCPUDistributionProducer/NumTruePU"),
    fileNameDataNPUEstimated=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/Run2018/PileupHistogram-UL2018-100bins_withVar.root"),
    histNameDataNPUEstimated=cms.string("pileup")
    # fileNameDataNPUEstimated=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/Run2017/PileupHistogram-goldenJSON-13tev-2018-69200ub-99bins.root"),
    # histNameDataNPUEstimated = cms.string("pileup")
  ),

  cms.PSet(
    namePUWeight = cms.string("Weight_pu69p2Up"),
    fileNameMCNPU=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/MC/mcPileupUL2018.root"),
    histNameMCNPU=cms.string("pu_mc"),
    # fileNameMCNPU=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/MC/MCNPUTrue_18_UL.root"),
    # histNameMCNPU=cms.string("MCPUDistributionProducer/NumTruePU"),
    fileNameDataNPUEstimated=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/Run2018/PileupHistogram-UL2018-100bins_withVar.root"),
    histNameDataNPUEstimated=cms.string("pileup_plus")
    # fileNameDataNPUEstimated=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/Run2018/PileupHistogram-goldenJSON-13tev-2018-72400ub-99bins.root"),
    # histNameDataNPUEstimated = cms.string("pileup")
  ),

  cms.PSet(
    namePUWeight = cms.string("Weight_pu69p2Down"),
    fileNameMCNPU=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/MC/mcPileupUL2018.root"),
    histNameMCNPU=cms.string("pu_mc"),
    # fileNameMCNPU=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/MC/MCNPUTrue_18_UL.root"),
    # histNameMCNPU=cms.string("MCPUDistributionProducer/NumTruePU"),
    fileNameDataNPUEstimated=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/Run2018/PileupHistogram-UL2018-100bins_withVar.root"),
    histNameDataNPUEstimated=cms.string("pileup_minus")
    # fileNameDataNPUEstimated=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/Run2018/PileupHistogram-goldenJSON-13tev-2018-66000ub-99bins.root"),
    # histNameDataNPUEstimated = cms.string("pileup")
  ),
)

#2017
NominalPUWeight2017 = cms.PSet(
    fileNameMCNPU=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/MC/mcPileupUL2017.root"),
    histNameMCNPU = cms.string("pu_mc"),
    # fileNameMCNPU=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/MC/MCNPUTrue_17_UL.root"),
    # histNameMCNPU = cms.string("MCPUDistributionProducer/NumTruePU"),
    fileNameDataNPUEstimated=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/Run2017/PileupHistogram-UL2017-100bins_withVar.root"),
    histNameDataNPUEstimated = cms.string("pileup")
    # fileNameDataNPUEstimated=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/Run2017/PileupHistogram-goldenJSON-13tev-2017-69200ub-99bins.root"),
    # histNameDataNPUEstimated = cms.string("pileup")
)
AdditionalPUWeights2017 = cms.VPSet(
  cms.PSet(
    namePUWeight = cms.string("Weight_pu69p2"),
    fileNameMCNPU=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/MC/mcPileupUL2017.root"),
    histNameMCNPU=cms.string("pu_mc"),
    # fileNameMCNPU=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/MC/MCNPUTrue_17_UL.root"),
    # histNameMCNPU = cms.string("MCPUDistributionProducer/NumTruePU"),
    fileNameDataNPUEstimated=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/Run2017/PileupHistogram-UL2017-100bins_withVar.root"),
    histNameDataNPUEstimated=cms.string("pileup")
    # fileNameDataNPUEstimated=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/Run2017/PileupHistogram-goldenJSON-13tev-2017-69200ub-99bins.root"),
    # histNameDataNPUEstimated = cms.string("pileup")
  ),

  cms.PSet(
    namePUWeight = cms.string("Weight_pu69p2Up"),
    fileNameMCNPU=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/MC/mcPileupUL2017.root"),
    histNameMCNPU=cms.string("pu_mc"),
    # fileNameMCNPU=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/MC/MCNPUTrue_17_UL.root"),
    # histNameMCNPU = cms.string("MCPUDistributionProducer/NumTruePU"),
    fileNameDataNPUEstimated=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/Run2017/PileupHistogram-UL2017-100bins_withVar.root"),
    histNameDataNPUEstimated=cms.string("pileup_plus")
    # fileNameDataNPUEstimated=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/Run2017/PileupHistogram-goldenJSON-13tev-2017-72400ub-99bins.root"),
    # histNameDataNPUEstimated = cms.string("pileup")
  ),

  cms.PSet(
    namePUWeight = cms.string("Weight_pu69p2Down"),
    fileNameMCNPU=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/MC/mcPileupUL2017.root"),
    histNameMCNPU=cms.string("pu_mc"),
    # fileNameMCNPU=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/MC/MCNPUTrue_17_UL.root"),
    # histNameMCNPU = cms.string("MCPUDistributionProducer/NumTruePU"),
    fileNameDataNPUEstimated=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/Run2017/PileupHistogram-UL2017-100bins_withVar.root"),
    histNameDataNPUEstimated=cms.string("pileup_minus")
    # fileNameDataNPUEstimated=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/Run2017/PileupHistogram-goldenJSON-13tev-2017-66000ub-99bins.root"),
    # histNameDataNPUEstimated = cms.string("pileup")
  ),
)

# 2016
NominalPUWeight2016preVFP = cms.PSet(
    fileNameMCNPU=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/MC/mcPileupUL2016.root"),
    histNameMCNPU = cms.string("pu_mc"),
    # fileNameMCNPU=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/MC/MCNPUTrue_16preVFP_UL.root"),
    # histNameMCNPU = cms.string("MCPUDistributionProducer/NumTruePU"),
    fileNameDataNPUEstimated=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/Run2016/PileupHistogram-UL2016-100bins_withVar.root"),
    histNameDataNPUEstimated = cms.string("pileup")
    # fileNameDataNPUEstimated=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/Run2016/PileupHistogram-goldenJSON-13tev-2016-69200ub-99bins.root"),
    # histNameDataNPUEstimated = cms.string("pileup")
)
AdditionalPUWeights2016preVFP = cms.VPSet(
  cms.PSet(
    namePUWeight = cms.string("Weight_pu69p2"),
    fileNameMCNPU=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/MC/mcPileupUL2016.root"),
    histNameMCNPU=cms.string("pu_mc"),
    # fileNameMCNPU=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/MC/MCNPUTrue_16preVFP_UL.root"),
    # histNameMCNPU = cms.string("MCPUDistributionProducer/NumTruePU"),
    fileNameDataNPUEstimated=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/Run2016/PileupHistogram-UL2016-100bins_withVar.root"),
    histNameDataNPUEstimated=cms.string("pileup")
    # fileNameDataNPUEstimated=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/Run2016/PileupHistogram-goldenJSON-13tev-2016-69200ub-99bins.root"),
    # histNameDataNPUEstimated = cms.string("pileup")
  ),

  cms.PSet(
    namePUWeight = cms.string("Weight_pu69p2Up"),
    fileNameMCNPU=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/MC/mcPileupUL2016.root"),
    histNameMCNPU=cms.string("pu_mc"),
    # fileNameMCNPU=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/MC/MCNPUTrue_16preVFP_UL.root"),
    # histNameMCNPU = cms.string("MCPUDistributionProducer/NumTruePU"),
    fileNameDataNPUEstimated=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/Run2016/PileupHistogram-UL2016-100bins_withVar.root"),
    histNameDataNPUEstimated=cms.string("pileup_plus")
    # fileNameDataNPUEstimated=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/Run2016/PileupHistogram-goldenJSON-13tev-2016-72400ub-99bins.root"),
    # histNameDataNPUEstimated = cms.string("pileup")
  ),

  cms.PSet(
    namePUWeight = cms.string("Weight_pu69p2Down"),
    fileNameMCNPU=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/MC/mcPileupUL2016.root"),
    histNameMCNPU=cms.string("pu_mc"),
    # fileNameMCNPU=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/MC/MCNPUTrue_16preVFP_UL.root"),
    # histNameMCNPU = cms.string("MCPUDistributionProducer/NumTruePU"),
    fileNameDataNPUEstimated=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/Run2016/PileupHistogram-UL2016-100bins_withVar.root"),
    histNameDataNPUEstimated=cms.string("pileup_minus")
    # fileNameDataNPUEstimated=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/Run2016/PileupHistogram-goldenJSON-13tev-2016-66000ub-99bins.root"),
    # histNameDataNPUEstimated = cms.string("pileup")
  ),  
)


NominalPUWeight2016postVFP = cms.PSet(
    fileNameMCNPU=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/MC/mcPileupUL2016.root"),
    histNameMCNPU=cms.string("pu_mc"),
    # fileNameMCNPU=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/MC/MCNPUTrue_16postVFP_UL.root"),
    # histNameMCNPU = cms.string("MCPUDistributionProducer/NumTruePU"),
    fileNameDataNPUEstimated=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/Run2016/PileupHistogram-UL2016-100bins_withVar.root"),
    histNameDataNPUEstimated=cms.string("pileup")
    # fileNameDataNPUEstimated=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/Run2016/PileupHistogram-goldenJSON-13tev-2016-69200ub-99bins.root"),
    # histNameDataNPUEstimated = cms.string("pileup")
)
AdditionalPUWeights2016postVFP = cms.VPSet(
  cms.PSet(
    namePUWeight = cms.string("Weight_pu69p2"),
    fileNameMCNPU=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/MC/mcPileupUL2016.root"),
    histNameMCNPU=cms.string("pu_mc"),
    # fileNameMCNPU=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/MC/MCNPUTrue_16postVFP_UL.root"),
    # histNameMCNPU = cms.string("MCPUDistributionProducer/NumTruePU"),
    fileNameDataNPUEstimated=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/Run2016/PileupHistogram-UL2016-100bins_withVar.root"),
    histNameDataNPUEstimated=cms.string("pileup")
    # fileNameDataNPUEstimated=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/Run2016/PileupHistogram-goldenJSON-13tev-2016-69200ub-99bins.root"),
    # histNameDataNPUEstimated = cms.string("pileup")
  ),

  cms.PSet(
    namePUWeight = cms.string("Weight_pu69p2Up"),
    fileNameMCNPU=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/MC/mcPileupUL2016.root"),
    histNameMCNPU=cms.string("pu_mc"),
    # fileNameMCNPU=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/MC/MCNPUTrue_16postVFP_UL.root"),
    # histNameMCNPU = cms.string("MCPUDistributionProducer/NumTruePU"),
    fileNameDataNPUEstimated=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/Run2016/PileupHistogram-UL2016-100bins_withVar.root"),
    histNameDataNPUEstimated=cms.string("pileup_plus")
    # fileNameDataNPUEstimated=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/Run2016/PileupHistogram-goldenJSON-13tev-2016-72400ub-99bins.root"),
    # histNameDataNPUEstimated = cms.string("pileup")
  ),

  cms.PSet(
    namePUWeight = cms.string("Weight_pu69p2Down"),
    fileNameMCNPU=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/MC/mcPileupUL2016.root"),
    histNameMCNPU=cms.string("pu_mc"),
    # fileNameMCNPU=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/MC/MCNPUTrue_16postVFP_UL.root"),
    # histNameMCNPU = cms.string("MCPUDistributionProducer/NumTruePU"),
    fileNameDataNPUEstimated=cms.string(
        "MiniAOD/MiniAODHelper/data/puweights/Run2016/PileupHistogram-UL2016-100bins_withVar.root"),
    histNameDataNPUEstimated=cms.string("pileup_minus")
    # fileNameDataNPUEstimated=cms.string(
    #     "MiniAOD/MiniAODHelper/data/puweights/Run2016/PileupHistogram-goldenJSON-13tev-2016-66000ub-99bins.root"),
    # histNameDataNPUEstimated = cms.string("pileup")
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
        "MiniAOD/MiniAODHelper/data/leptonTriggerSF_UL/2017/Efficiencies_muon_generalTracks_Z_Run2017_UL_SingleMuonTriggers.root"),
    muonHistName=cms.string(
        "NUM_IsoMu27_DEN_CutBasedIdTight_and_PFIsoTight_abseta_pt"),
)

TriggerSFs2018 = cms.PSet(
    elecFileName = cms.string("MiniAOD/MiniAODHelper/data/Run2Legacy/SingleEG_JetHT_Trigger_Scale_Factors_ttHbb2018_v2.root"),
    elecHistName = cms.string("ele28_ht150_OR_ele32_ele_pt_ele_sceta"),
    muonFileName=cms.string(
        "MiniAOD/MiniAODHelper/data/leptonTriggerSF_UL/2018/Efficiencies_muon_generalTracks_Z_Run2018_UL_SingleMuonTriggers.root"),
    muonHistName=cms.string(
        "NUM_IsoMu24_DEN_CutBasedIdTight_and_PFIsoTight_abseta_pt"),
)



