# Default lepton selection of the "loose electrons/muons" defined at
# https://twiki.cern.ch/twiki/bin/view/CMS/TTbarHbbRun2ReferenceAnalysis#Object_selection_SPRING15

import FWCore.ParameterSet.Config as cms

SelectedElectronProducer2017 = cms.EDProducer(
    "SelectedLeptonProducer",
    
    leptonType = cms.string("electron"),

    isData       = cms.bool(False),
    
    era = cms.string("2017"),

    leptons = cms.InputTag("slimmedElectrons"),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    #eleMediumIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-medium","","boostedAnalysis"),
    #eleLooseIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-loose","","boostedAnalysis"),
    #eleVetoIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-veto","","boostedAnalysis"),
    #eleTightIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-tight","","boostedAnalysis"),

    ptMins   = cms.vdouble(15),
    etaMaxs  = cms.vdouble(2.4),
    leptonIDs = cms.vstring("loose"),
    collectionNames= cms.vstring("selectedElectronsLoose"),
    isoConeSizes = cms.vstring(""),
    isoCorrTypes = cms.vstring("rhoEA"),
    
    muonIsoTypes = cms.vstring("loose"),
    useMuonRC = cms.bool(False),
    useDeterministicSeeds = cms.bool(False),
    rc_dir = cms.string("BoostedTTH/Producers/data/muonSFs/RoccoR2017.txt"),
    
    ea_dir_electron = cms.string("BoostedTTH/Producers/data/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt"),

    # https://github.com/wweiphy/BoostedTTH/blob/TTHHUL/Producers/data/effAreaMuons_cone03_pfNeuHadronsAndPhotons_94X.txt
 
    ea_dir_muon=cms.string(
        "BoostedTTH/Producers/data/effAreaMuons_cone03_pfNeuHadronsAndPhotons_94X.txt"),

    # https://twiki.cern.ch/twiki/bin/view/CMS/EgammaUL2016To2018#SFs_for_Electrons_UL_2018
    file_EleLooseIDSF=cms.string(
        "BoostedTTH/Producers/data/electronSFs/egammaEffi.txt_EGM2D_Loose_UL17.root"),
    file_EleMediumIDSF=cms.string(
        "BoostedTTH/Producers/data/electronSFs/egammaEffi.txt_EGM2D_Medium_UL17.root"),
    file_EleTightIDSF=cms.string(
        "BoostedTTH/Producers/data/electronSFs/egammaEffi.txt_EGM2D_MVA80iso_UL17.root"),
    file_EleRecoSF_highPt=cms.string(
        "BoostedTTH/Producers/data/electronSFs/egammaEffi_ptAbove20.txt_EGM2D_UL2017.root"),
    file_EleRecoSF_lowPt=cms.string(
        "BoostedTTH/Producers/data/electronSFs/egammaEffi_ptBelow20.txt_EGM2D_UL2017.root"),
    file_MuonLooseIDSF=cms.string(""),
    file_MuonMediumIDSF=cms.string(""),
    file_MuonTightIDSF=cms.string(""),
    file_MuonIsoSF=cms.string(""),
    file_MuonRecoSF_highPt=cms.string(""),
    file_MuonRecoSF_lowPt=cms.string(""),
    # file_MuonIsoSF_lowPt=cms.string("")
    )

SelectedElectronProducer2016preVFP = SelectedElectronProducer2017.clone(
    era = cms.string("2016preVFP"),
    file_EleLooseIDSF=cms.string(
        "BoostedTTH/Producers/data/electronSFs/egammaEffi.txt_Ele_Loose_preVFP_EGM2D.root"),
    file_EleMediumIDSF=cms.string(
        "BoostedTTH/Producers/data/electronSFs/egammaEffi.txt_Ele_Medium_preVFP_EGM2D.root"),
    file_EleTightIDSF=cms.string(
        "BoostedTTH/Producers/data/electronSFs/egammaEffi.txt_Ele_wp80iso_preVFP_EGM2D.root"),
    file_EleRecoSF_highPt=cms.string(
        "BoostedTTH/Producers/data/electronSFs/egammaEffi_ptAbove20.txt_EGM2D_UL2016preVFP.root"),
    file_EleRecoSF_lowPt=cms.string(
        "BoostedTTH/Producers/data/electronSFs/egammaEffi_ptBelow20.txt_EGM2D_UL2016preVFP.root")
    )

SelectedElectronProducer2016postVFP = SelectedElectronProducer2017.clone(
    era=cms.string("2016postVFP"),
    file_EleLooseIDSF=cms.string(
        "BoostedTTH/Producers/data/electronSFs/egammaEffi.txt_Ele_Loose_postVFP_EGM2D.root"),
    file_EleMediumIDSF=cms.string(
        "BoostedTTH/Producers/data/electronSFs/egammaEffi.txt_Ele_Medium_postVFP_EGM2D.root"),
    file_EleTightIDSF=cms.string(
        "BoostedTTH/Producers/data/electronSFs/egammaEffi.txt_Ele_wp80iso_postVFP_EGM2D.root"),
    file_EleRecoSF_highPt=cms.string(
        "BoostedTTH/Producers/data/electronSFs/egammaEffi_ptAbove20.txt_EGM2D_UL2016postVFP.root"),
    file_EleRecoSF_lowPt=cms.string(
        "BoostedTTH/Producers/data/electronSFs/egammaEffi_ptBelow20.txt_EGM2D_UL2016postVFP.root")
)

SelectedElectronProducer2018 = SelectedElectronProducer2017.clone(
    era = cms.string("2018"),
    file_EleLooseIDSF=cms.string(
        "BoostedTTH/Producers/data/electronSFs/egammaEffi.txt_Ele_Loose_EGM2D_UL18.root"),
    file_EleMediumIDSF=cms.string(
        "BoostedTTH/Producers/data/electronSFs/egammaEffi.txt_Ele_Medium_EGM2D_UL18.root"),
    file_EleTightIDSF=cms.string(
        "BoostedTTH/Producers/data/electronSFs/egammaEffi.txt_Ele_wp80iso_EGM2D_UL18.root"),
    file_EleRecoSF_highPt=cms.string(
        "BoostedTTH/Producers/data/electronSFs/egammaEffi_ptAbove20.txt_EGM2D_UL2018.root"),
    file_EleRecoSF_lowPt=cms.string(
        "BoostedTTH/Producers/data/electronSFs/egammaEffi_ptBelow20.txt_EGM2D_UL2018.root")
    )

SelectedMuonProducer2017 = cms.EDProducer(
    "SelectedLeptonProducer",
    
    leptonType = cms.string("muon"),

    isData       = cms.bool(False),
    
    era = cms.string("2017"),

    leptons = cms.InputTag("slimmedMuons"),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),

    ptMins   = cms.vdouble(15),
    etaMaxs  = cms.vdouble(2.4),
    leptonIDs = cms.vstring("loose"),
    collectionNames= cms.vstring("selectedMuonsLoose"),
    isoConeSizes = cms.vstring(""),
    isoCorrTypes = cms.vstring("rhoEA"),
    
    muonIsoTypes = cms.vstring("loose"),
    useMuonRC = cms.bool(True),
    useDeterministicSeeds = cms.bool(False),
    rc_dir = cms.string("BoostedTTH/Producers/data/muonSFs/RoccoR2017.txt"),
    ea_dir_electron=cms.string(
        "BoostedTTH/Producers/data/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt"),
    ea_dir_muon=cms.string(
        "BoostedTTH/Producers/data/effAreaMuons_cone03_pfNeuHadronsAndPhotons_94X.txt"),
    # The following two parameters are dummies in case of muons
    # they are not used for the muon selection, which is defined
    # via the 'leptonID' value
    #eleMediumIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-medium","","boostedAnalysis"),
    #eleLooseIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-loose","","boostedAnalysis"),
    #eleVetoIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-veto","","boostedAnalysis"),
    #eleTightIdMap = cms.InputTag("egmGsfElectronIDs:cutBasedElectronID-Fall17-94X-V1-tight","","boostedAnalysis"),
    # ea_dir = cms.string("BoostedTTH/Producers/data/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt"),
    file_EleLooseIDSF=cms.string(""),
    file_EleMediumIDSF=cms.string(""),
    file_EleTightIDSF=cms.string(""),
    file_EleRecoSF_highPt=cms.string(""),
    file_EleRecoSF_lowPt=cms.string(""),

    # keep the muon Reco files the same for now because the low pt file does not exist? https://gitlab.cern.ch/cms-muonPOG/muonefficiencies/-/tree/master/Run2/UL/2018
    file_MuonRecoSF_highPt=cms.string(
        "BoostedTTH/Producers/data/muonSFs/2017/Efficiency_muon_generalTracks_Run2017_UL_trackerMuon.root"),
    file_MuonRecoSF_lowPt=cms.string(
        "BoostedTTH/Producers/data/muonSFs/2017/Efficiency_muon_generalTracks_Run2017_UL_trackerMuon.root"),

    file_MuonIDSF=cms.string(
        "BoostedTTH/Producers/data/muonSFs/2017/Efficiencies_muon_generalTracks_Z_Run2017_UL_ID.root"),
    histname_MuonLooseIDSF=cms.string("NUM_LooseID_DEN_TrackerMuons_abseta_pt"),
    histname_MuonMediumIDSF=cms.string(
        "NUM_MediumID_DEN_TrackerMuons_abseta_pt"),
    histname_MuonTightIDSF=cms.string(
        "NUM_TightID_DEN_TrackerMuons_abseta_pt"),

    file_MuonIsoSF=cms.string(
        "BoostedTTH/Producers/data/muonSFs/2017/Efficiencies_muon_generalTracks_Z_Run2017_UL_ISO.root"),
    histname_MuonLooseISO_LooseIDSF = cms.string("NUM_LooseRelIso_DEN_LooseID_abseta_pt"),
    histname_MuonLooseISO_MediumIDSF = cms.string("NUM_LooseRelIso_DEN_MediumID_abseta_pt"),
    histname_MuonLooseISO_TightIDSF = cms.string("NUM_LooseRelIso_DEN_TightIDandIPCut_abseta_pt"),

    histname_MuonTightISO_MediumIDSF = cms.string("NUM_TightRelIso_DEN_MediumID_abseta_pt"),
    histname_MuonTightISO_TightIDSF = cms.string("NUM_TightRelIso_DEN_TightIDandIPCut_abseta_pt"),
    )

SelectedMuonProducer2016postVFP = SelectedMuonProducer2017.clone(
    era = cms.string("2016postVFP"),
    rc_dir = cms.string("BoostedTTH/Producers/data/muonSFs/RoccoR2016.txt"),

    file_MuonRecoSF_highPt=cms.string(
        "BoostedTTH/Producers/data/muonSFs/2016postVFP/Efficiency_muon_generalTracks_Run2016postVFP_UL_trackerMuon.root"),
    file_MuonRecoSF_lowPt=cms.string(
        "BoostedTTH/Producers/data/muonSFs/2016postVFP/Efficiency_muon_generalTracks_Run2016postVFP_UL_trackerMuon.root"),

    file_MuonIDSF=cms.string(
        "BoostedTTH/Producers/data/muonSFs/2016postVFP/Efficiencies_muon_generalTracks_Z_Run2016_UL_ID.root"),
    histname_MuonLooseIDSF=cms.string("NUM_LooseID_DEN_TrackerMuons_abseta_pt"),
    histname_MuonMediumIDSF=cms.string("NUM_MediumID_DEN_TrackerMuons_abseta_pt"),
    histname_MuonTightIDSF=cms.string("NUM_TightID_DEN_TrackerMuons_abseta_pt"),

    file_MuonIsoSF=cms.string(
        "BoostedTTH/Producers/data/muonSFs/2016postVFP/Efficiencies_muon_generalTracks_Z_Run2016_UL_ISO.root"),

    histname_MuonLooseISO_LooseIDSF = cms.string("NUM_LooseRelIso_DEN_LooseID_abseta_pt"),
    histname_MuonLooseISO_MediumIDSF = cms.string("NUM_LooseRelIso_DEN_MediumID_abseta_pt"),
    histname_MuonLooseISO_TightIDSF = cms.string("NUM_LooseRelIso_DEN_TightIDandIPCut_abseta_pt"),

    histname_MuonTightISO_MediumIDSF = cms.string("NUM_TightRelIso_DEN_MediumID_abseta_pt"),
    histname_MuonTightISO_TightIDSF = cms.string("NUM_TightRelIso_DEN_TightIDandIPCut_abseta_pt"),
    )

SelectedMuonProducer2016preVFP = SelectedMuonProducer2017.clone(
    era = cms.string("2016preVFP"),
    rc_dir = cms.string("BoostedTTH/Producers/data/muonSFs/RoccoR2016.txt"),

    file_MuonRecoSF_highPt=cms.string(
        "BoostedTTH/Producers/data/muonSFs/2016preVFP/Efficiency_muon_generalTracks_Run2016preVFP_UL_trackerMuon.root"),
    file_MuonRecoSF_lowPt=cms.string(
        "BoostedTTH/Producers/data/muonSFs/2016preVFP/Efficiency_muon_generalTracks_Run2016preVFP_UL_trackerMuon.root"),

    file_MuonIDSF=cms.string(
        "BoostedTTH/Producers/data/muonSFs/2016preVFP/Efficiencies_muon_generalTracks_Z_Run2016_UL_HIPM_ID.root"),
    histname_MuonLooseIDSF=cms.string("NUM_LooseID_DEN_TrackerMuons_abseta_pt"),
    histname_MuonMediumIDSF=cms.string("NUM_MediumID_DEN_TrackerMuons_abseta_pt"),
    histname_MuonTightIDSF=cms.string("NUM_TightID_DEN_TrackerMuons_abseta_pt"),

    file_MuonIsoSF=cms.string(
        "BoostedTTH/Producers/data/muonSFs/2016preVFP/Efficiencies_muon_generalTracks_Z_Run2016_UL_HIPM_ISO.root"),

    histname_MuonLooseISO_LooseIDSF = cms.string("NUM_LooseRelIso_DEN_LooseID_abseta_pt"),
    histname_MuonLooseISO_MediumIDSF = cms.string("NUM_LooseRelIso_DEN_MediumID_abseta_pt"),
    histname_MuonLooseISO_TightIDSF = cms.string("NUM_LooseRelIso_DEN_TightIDandIPCut_abseta_pt"),

    histname_MuonTightISO_MediumIDSF = cms.string("NUM_TightRelIso_DEN_MediumID_abseta_pt"),
    histname_MuonTightISO_TightIDSF = cms.string("NUM_TightRelIso_DEN_TightIDandIPCut_abseta_pt"),
    )

SelectedMuonProducer2018 = SelectedMuonProducer2017.clone(
    era = cms.string("2018"),
    rc_dir = cms.string("BoostedTTH/Producers/data/muonSFs/RoccoR2018.txt"),

    file_MuonRecoSF_highPt=cms.string(
        "BoostedTTH/Producers/data/muonSFs/2018/Efficiency_muon_generalTracks_Run2018_UL_trackerMuon.root"),
    file_MuonRecoSF_lowPt=cms.string(
        "BoostedTTH/Producers/data/muonSFs/2018/Efficiency_muon_generalTracks_Run2018_UL_trackerMuon.root"),

    file_MuonIDSF=cms.string(
        "BoostedTTH/Producers/data/muonSFs/2018/Efficiencies_muon_generalTracks_Z_Run2018_UL_ID.root"),
    histname_MuonLooseIDSF=cms.string("NUM_LooseID_DEN_TrackerMuons_abseta_pt"),
    histname_MuonMediumIDSF=cms.string("NUM_MediumID_DEN_TrackerMuons_abseta_pt"),
    histname_MuonTightIDSF=cms.string("NUM_TightID_DEN_TrackerMuons_abseta_pt"),

    file_MuonIsoSF=cms.string(
        "BoostedTTH/Producers/data/muonSFs/2018/Efficiencies_muon_generalTracks_Z_Run2018_UL_ISO.root"),

    histname_MuonLooseISO_LooseIDSF = cms.string("NUM_LooseRelIso_DEN_LooseID_abseta_pt"),
    histname_MuonLooseISO_MediumIDSF = cms.string("NUM_LooseRelIso_DEN_MediumID_abseta_pt"),
    histname_MuonLooseISO_TightIDSF = cms.string("NUM_LooseRelIso_DEN_TightIDandIPCut_abseta_pt"),

    histname_MuonTightISO_MediumIDSF = cms.string("NUM_TightRelIso_DEN_MediumID_abseta_pt"),
    histname_MuonTightISO_TightIDSF = cms.string("NUM_TightRelIso_DEN_TightIDandIPCut_abseta_pt"),

    )
