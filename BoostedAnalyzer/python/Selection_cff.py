import FWCore.ParameterSet.Config as cms

LeptonSelectionNoTrigger = cms.PSet(
    muonTriggers = cms.vstring("None"),
    electronTriggers = cms.vstring("None"),
    channel = cms.string("both")
)

LeptonSelectionData2016 = cms.PSet(
    muonTriggers = cms.vstring("HLT_IsoMu24_v*","HLT_IsoTkMu24_v*"),
    electronTriggers = cms.vstring("HLT_Ele27_WPTight_Gsf_v*"),
    channel = cms.string("both")
)


LeptonSelectionData2016Trigger = cms.PSet(
    muonTriggers = cms.vstring("HLT_IsoMu24_v*","HLT_IsoTkMu24_v*"),
    electronTriggers = cms.vstring("HLT_Ele27_WPTight_Gsf_v*"),
    channel = cms.string("el-TriggerEff")
)

LeptonSelectionData2017 = cms.PSet(
    muonTriggers = cms.vstring("HLT_IsoMu27_v*"),
    electronTriggers = cms.vstring("HLT_Ele32_WPTight_Gsf_L1DoubleEG_v*","HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v*"),
    channel = cms.string("both")
)

LeptonSelectionData2017Trigger = cms.PSet(
    muonTriggers = cms.vstring("HLT_IsoMu27_v*"),
    electronTriggers = cms.vstring("HLT_Ele32_WPTight_Gsf_L1DoubleEG_v*","HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v*"),
    channel = cms.string("el-TriggerEff")
)

LeptonSelectionData2018 = cms.PSet(
    muonTriggers = cms.vstring("HLT_IsoMu24_v*"),
    electronTriggers = cms.vstring("HLT_Ele32_WPTight_Gsf_v*","HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v*"),
    channel = cms.string("both")
)
LeptonSelectionData2018Trigger = cms.PSet(
    muonTriggers = cms.vstring("HLT_IsoMu24_v*"),
    electronTriggers = cms.vstring("HLT_Ele32_WPTight_Gsf_v*","HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v*"),
    channel = cms.string("el-TriggerEff")
)


LeptonSelectionMC2016 = cms.PSet(
    muonTriggers = cms.vstring("HLT_IsoMu24_v*","HLT_IsoTkMu24_v*"),
    electronTriggers = cms.vstring("HLT_Ele27_WPTight_Gsf_v*"),
    channel = cms.string("both")
)


LeptonSelectionMC2017 = cms.PSet(
    muonTriggers = cms.vstring("HLT_IsoMu27_v*"),
    electronTriggers = cms.vstring("HLT_Ele32_WPTight_Gsf_L1DoubleEG_v*","HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v*"),
    channel = cms.string("both")
)

LeptonSelectionMC2018 = cms.PSet(
    muonTriggers = cms.vstring("HLT_IsoMu24_v*"),
    electronTriggers = cms.vstring("HLT_Ele32_WPTight_Gsf_v*","HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v*"),
    channel = cms.string("both")
)


LeptonSelectionMC2016Trigger = cms.PSet(
    muonTriggers = cms.vstring("HLT_IsoMu24_v*","HLT_IsoTkMu24_v*"),
    electronTriggers = cms.vstring("HLT_Ele27_WPTight_Gsf_v*"),
    channel = cms.string("el-TriggerEff")
)

LeptonSelectionMC2017Trigger = cms.PSet(
    muonTriggers = cms.vstring("HLT_IsoMu27_v*"),
    electronTriggers = cms.vstring("HLT_Ele32_WPTight_Gsf_L1DoubleEG_v*","HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v*"),
    channel = cms.string("el-TriggerEff")
)

LeptonSelectionMC2018Trigger = cms.PSet(
    muonTriggers = cms.vstring("HLT_IsoMu24_v*"),
    electronTriggers = cms.vstring("HLT_Ele32_WPTight_Gsf_v*","HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v*"),
    channel = cms.string("el-TriggerEff")
)

DiLeptonSelectionNoTrigger  = cms.PSet(
    mumuTriggers = cms.vstring("None"),
    elelTriggers = cms.vstring("None"),
    elmuTriggers = cms.vstring("None"),
    dlchannel = cms.string("all"),
)

DiLeptonSelectionMC = cms.PSet(
    mumuTriggers = cms.vstring("HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v*","HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v*",
                               "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v*"),
    elelTriggers = cms.vstring("HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v*","HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*"),
    elmuTriggers = cms.vstring("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v*","HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*",
                               "HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*","HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*"),
    muonTriggers=cms.vstring("HLT_IsoMu27_v*"),
    electronTriggers=cms.vstring(
        "HLT_Ele32_WPTight_Gsf_L1DoubleEG_v*", "HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v*"),
    dlchannel = cms.string("all"),
)
DiLeptonSelectionData = cms.PSet(
    mumuTriggers = cms.vstring("HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v*","HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v*",
                               "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v*"),
    elelTriggers = cms.vstring("HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v*","HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*"),
    elmuTriggers = cms.vstring("HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v*","HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*",
                               "HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*","HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*"),
    dlchannel = cms.string("all"),
)

METSelection = cms.PSet(
    minMET = cms.double(20.),
    maxMET = cms.double(100000.),
)

DiLeptonMETSelection = cms.PSet(
    minMET = cms.double(-1),
    maxMET = cms.double(800),
)

# JetTagSelection = cms.PSet(
#     minJets = cms.vint32(4),
#     maxJets = cms.vint32(-1),
#     minTags = cms.vint32(3),
#     maxTags = cms.vint32(-1)
# ) # for baseline selection


JetTagSelection = cms.PSet(
    minJets = cms.vint32(4),
    maxJets = cms.vint32(-1),
    minTags = cms.vint32(-1),
    maxTags = cms.vint32(-1)
) # for control region study

# TODO - update the trigger for data when later include it
checkBasicDataTriggers= cms.PSet(
    relevantTriggers=cms.vstring(
                                 "HLT_Ele35_WPTight_Gsf_v*",
                                 "HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v*",
                                 "HLT_Ele27_WPTight_Gsf_v*",
                                 "HLT_Ele32_WPTight_Gsf_v*",
                                 "HLT_IsoMu27_v*",
                                 "HLT_IsoMu24_v*",
                                 "HLT_IsoTkMu24_v*",
                                 "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v*",
                                 "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*",
                                 "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v*",
                                 "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*",
                                 "HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*",
                                 "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*",
                                 "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v*",
                                 "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v*",
                                 "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v*",
                                 "HLT_Ele32_WPTight_Gsf_L1DoubleEG_v*",
                                 "HLT_Ele32_WPTight_Gsf_2017Seeds*"
                                 )
)

# TODO - check the trigger list
checkBasicMCTriggers= cms.PSet(
    relevantTriggers=cms.vstring(
                                 "HLT_Ele35_WPTight_Gsf_v*",
                                 "HLT_Ele28_eta2p1_WPTight_Gsf_HT150_v*",
                                 "HLT_Ele27_WPTight_Gsf_v*",
                                 "HLT_Ele32_WPTight_Gsf_v*",
                                 "HLT_IsoMu27_v*",
                                 "HLT_IsoMu24_v*",
                                 "HLT_IsoTkMu24_v*",
                                 "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_v*",
                                 "HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*",
                                 "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_v*",
                                 "HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ_v*",
                                 "HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*",
                                 "HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ_v*",
                                 "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_v*",
                                 "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass3p8_v*",
                                 "HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8_v*",
                                 "HLT_Ele32_WPTight_Gsf_L1DoubleEG_v*",
                                 "HLT_Ele32_WPTight_Gsf_2017Seeds*"
                                 )
)

checkNoTriggers= cms.PSet(
    relevantTriggers=cms.vstring()
    )

#  Updated from https://twiki.cern.ch/twiki/bin/viewauth/CMS/MissingETOptionalFiltersRun2#What_is_available_in_MiniAOD
filtersData1718=cms.vstring(
                    "Flag_goodVertices",
                    "Flag_globalSuperTightHalo2016Filter",
                    "Flag_HBHENoiseFilter",
                    "Flag_HBHENoiseIsoFilter",
                    "Flag_EcalDeadCellTriggerPrimitiveFilter",
                    "Flag_BadPFMuonFilter",
                    "Flag_BadPFMuonDzFilter",  # TODO - Remove for now, may need to be added later
                    # "Flag_hfNoisyHitsFilter",
                    # "Flag_BadChargedCandidateFilter",
                    "Flag_eeBadScFilter",
                    "Flag_ecalBadCalibFilter"
                    )

filtersMC1718=cms.vstring("Flag_goodVertices",
                    "Flag_goodVertices",
                    "Flag_globalSuperTightHalo2016Filter",
                    "Flag_HBHENoiseFilter",
                    "Flag_HBHENoiseIsoFilter",
                    "Flag_EcalDeadCellTriggerPrimitiveFilter",
                    "Flag_BadPFMuonFilter",
                    "Flag_BadPFMuonDzFilter",
                    # "Flag_hfNoisyHitsFilter",
                    # "Flag_BadChargedCandidateFilter",
                    "Flag_eeBadScFilter",
                    "Flag_ecalBadCalibFilter"
                    )

filtersData16=cms.vstring(
                    "Flag_goodVertices",
                    "Flag_globalSuperTightHalo2016Filter",
                    "Flag_HBHENoiseFilter",
                    "Flag_HBHENoiseIsoFilter",
                    "Flag_EcalDeadCellTriggerPrimitiveFilter",
                    "Flag_BadPFMuonFilter",
                    "Flag_BadPFMuonDzFilter",
                    "Flag_eeBadScFilter",
                    # "Flag_hfNoisyHitsFilter",
                    )

filtersMC16=cms.vstring(
                    "Flag_goodVertices",
                    "Flag_globalSuperTightHalo2016Filter",
                    "Flag_HBHENoiseFilter",
                    "Flag_HBHENoiseIsoFilter",
                    "Flag_EcalDeadCellTriggerPrimitiveFilter",
                    "Flag_BadPFMuonFilter",
                    "Flag_BadPFMuonDzFilter",
                    "Flag_eeBadScFilter",
                    # "Flag_hfNoisyHitsFilter",
                    )

# process.BoostedAnalyzer.additionalFilters = cms.VInputTag(["ecalBadCalibReducedMINIAODFilter"])
