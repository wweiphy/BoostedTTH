import FWCore.ParameterSet.Config as cms

SelectedJetProducer = cms.EDProducer(
    "SelectedJetProducer",
    isData       = cms.bool(False),
    applyCorrection = cms.bool(True),
    doJER = cms.bool(False),
    jets = cms.InputTag("slimmedJets"),
    miniAODGenJets = cms.InputTag("slimmedGenJets"),
    electrons = cms.InputTag("SelectedElectronProducer:selectedElectronsLoose"),
    muons = cms.InputTag("SelectedMuonProducer:selectedMuonsLoose"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    ptMins   = cms.vdouble(30,20),
    etaMaxs  = cms.vdouble(2.4,2.4),
    PUJetIDMins = cms.vstring("none","none"),
    leptonJetDr = cms.double(0.4),
    collectionNames  = cms.vstring("selectedJets","selectedJetsLoose"),
    systematics = cms.vstring(""),
    JetID = cms.vstring("none"),
    JetType = cms.string("AK4PFCHS"),

    # https://twiki.cern.ch/twiki/bin/view/CMS/JECDataMC#Recommended_for_MC
    # TODO - should be updated for 20UL
    # jecFileAK4_2016 = cms.string("Summer16_07Aug2017_V11_MC_UncertaintySources_AK4PFchs.txt"),
    jecFileAK8_2016preVFP=cms.string(
        "Summer19UL16APV_V7_MC_UncertaintySources_AK8PFchs.txt"),
    jecFileAK8_2016postVFP=cms.string(
        "Summer19UL16_V7_MC_UncertaintySources_AK8PFchs.txt"),
    # jecFileAK4_2017 = cms.string("Fall17_17Nov2017_V32_MC_UncertaintySources_AK4PFchs.txt"),
    jecFileAK8_2017=cms.string(
        "Summer19UL17_V5_MC_UncertaintySources_AK8PFchs.txt"),
    # jecFileAK4_2018 = cms.string("Autumn18_V19_MC_UncertaintySources_AK4PFchs.txt"),
    jecFileAK8_2018=cms.string(
        "Summer19UL18_V5_MC_UncertaintySources_AK8PFchs.txt"),
    
    jecFileAK4_2016preVFP=cms.string(
        "RegroupedV2_Summer19UL16APV_V7_MC_UncertaintySources_AK4PFchs.txt"),
    jecFileAK4_2016postVFP=cms.string(
        "RegroupedV2_Summer19UL16_V7_MC_UncertaintySources_AK4PFchs.txt"),
    jecFileAK4_2017=cms.string(
        "RegroupedV2_Summer19UL17_V5_MC_UncertaintySources_AK4PFchs.txt"),
    jecFileAK4_2018=cms.string(
        "RegroupedV2_Summer19UL18_V5_MC_UncertaintySources_AK4PFchs.txt"),
    
    era = cms.string("2017")
)

