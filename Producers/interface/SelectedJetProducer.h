// -*- C++ -*-
//
// Package:    BoostedTTH/SelectedJetProducer
// Class:      SelectedJetProducer
//
/**\class SelectedJetProducer SelectedJetProducer.cc BoostedTTH/SelectedJetProducer/plugins/SelectedJetProducer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Hannes Mildner
//         Created:  Tue, 05 Apr 2016 09:53:41 GMT
//
//


#ifndef SelectedJetProducer_h
#define SelectedJetProducer_h

// system include files
#include <memory>
#include <vector>
#include <utility>
#include <fstream>
#include <exception>
#include <iostream>
// #include <memory>
#include <string>
// #include <vector>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/StreamID.h"
#include "FWCore/Utilities/interface/Exception.h"

#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/Muon.h"

#include "../interface/SystematicsHelper.h"

// correction stuff
#include "JetMETCorrections/Objects/interface/JetCorrector.h"
#include "JetMETCorrections/Objects/interface/JetCorrectionsRecord.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "CondFormats/JetMETObjects/interface/FactorizedJetCorrector.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"

//To use when the object is either a reference or a pointer
template <typename T>
T *ptr(T &obj) { return &obj; } //turn reference into pointer!
template <typename T>
T *ptr(T *obj) { return obj; } //obj is already pointer, return it!

//
// class declaration
//

class SelectedJetProducer : public edm::EDProducer
{
public:
  explicit SelectedJetProducer(const edm::ParameterSet &);
  ~SelectedJetProducer();

  static void fillDescriptions(edm::ConfigurationDescriptions &descriptions);
  enum class JetID
  {
    None,
    Loose,
    Tight,
    TightLepVeto
  };
  enum class PUJetIDWP
  {
    None,
    Loose,
    Medium,
    Tight
  };
  enum class JetType
  {
      AK4PFCHS,
      AK8PFCHS
  };

private:
  // some enums to make things nicer

  // member functions
  // virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
  // virtual void produce(edm::Event &, const edm::EventSetup &) override;
  // virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

  virtual void beginJob() override;
  virtual void produce(edm::Event &, const edm::EventSetup &) override;
  virtual void endJob() override;
  
  std::string systName(std::string name, SystematicsHelper::Type) const;
  
  bool fileExists(const std::string &fileName) const;
  
  void UpdateJetCorrectorUncertainties(const edm::EventSetup &iSetup);
  JetCorrectionUncertainty *CreateJetCorrectorUncertainty(const edm::EventSetup &iSetup, const std::string &jetTypeLabel, const std::string &uncertaintyLabel) const;
  
  std::vector<pat::Jet> GetSelectedJets(const std::vector<pat::Jet> &, const float iMinPt, const float iMaxAbsEta, const JetID, const PUJetIDWP = PUJetIDWP::None) const;
  bool isGoodJet(const pat::Jet &iJet, const float iMinPt, const float iMaxAbsEta, const JetID, const PUJetIDWP wp) const;
  std::vector<pat::Jet> GetUncorrectedJets(const std::vector<pat::Jet> &inputJets) const;
  std::vector<pat::Jet> GetDeltaRCleanedJets(const std::vector<pat::Jet> &inputJets, const std::vector<pat::Muon> &inputMuons, const std::vector<pat::Electron> &inputElectrons, const double deltaRCut) const;
  std::vector<pat::Jet> GetCorrectedJets(const std::vector<pat::Jet> &, const edm::Event &, const edm::EventSetup &, const edm::Handle<reco::GenJetCollection> &, const SystematicsHelper::Type iSysType = SystematicsHelper::NA, const bool &doJES = true, const bool &doJER = true, const float &corrFactor = 1, const float &uncFactor = 1);
  
  pat::Jet GetCorrectedJet(const pat::Jet &, const edm::Event &, const edm::EventSetup &, const edm::Handle<reco::GenJetCollection> &, const SystematicsHelper::Type iSysType = SystematicsHelper::NA, const bool doJES = true, const bool doJER = true, const float corrFactor = 1, const float uncFactor = 1);
  
  void ApplyJetEnergyCorrection(pat::Jet &jet, double &totalCorrFactor, const edm::Event &event, const edm::EventSetup &setup, const edm::Handle<reco::GenJetCollection> &genjets, const SystematicsHelper::Type iSysType, const bool doJES, const bool doJER, const bool addUserFloats, const float corrFactor, float uncFactor);
  
  double GetJECUncertainty(const pat::Jet &jet, const edm::EventSetup &iSetup, const SystematicsHelper::Type iSysType);
  void AddJetCorrectorUncertainty(const edm::EventSetup &iSetup, const std::string &uncertaintyLabel);
  
  template <typename T> T GetSortedByPt(const T &) const;
  
  int TranslateJetPUIDtoInt(PUJetIDWP wp) const;

  //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
  //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
  //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
  //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
  const std::string jetType;
  JetType JetType_;
  const bool isData;
  /** min pt of jet collections **/
  const std::vector<double> ptMins;
  /** max eta of jet collections **/
  const std::vector<double> etaMaxs;
  /** min dir to lepton for jets **/
  const double leptonJetDr;

  /** apply jet energy correciton? **/
  const bool applyCorrection;
  const bool doJER;

  /** names of output jet collections **/
  const std::vector<std::string> collectionNames;
  /** pileupjetid for collections **/
  const std::vector<std::string> PUJetIDMins;
  /** jetid **/
  const std::vector<std::string> JetID_;
  /** Systematics used **/
  const std::vector<std::string> systematics_config;
  std::vector<SystematicsHelper::Type> systematics;

  // ----------member data ---------------------------
  /** input jets data access token **/
  edm::EDGetTokenT<pat::JetCollection> jetsToken;
  /** genjets data access token (for getcorrected jets) **/
  edm::EDGetTokenT<reco::GenJetCollection> genjetsToken;
  /** muons data access token (for jet cleaning)**/
  edm::EDGetTokenT<pat::MuonCollection> muonsToken;
  /** electrons data access token (for jet cleaning)**/
  edm::EDGetTokenT<pat::ElectronCollection> electronsToken;
  /** rho data access token (for jet cleaning)**/
  edm::EDGetTokenT<double> rhoToken;

  //JEC files
  const std::string jecFileAK4_2016preVFP;
  const std::string jecFileAK8_2016preVFP;
  const std::string jecFileAK4_2016postVFP;
  const std::string jecFileAK8_2016postVFP;
  const std::string jecFileAK4_2017;
  const std::string jecFileAK8_2017;
  const std::string jecFileAK4_2018;
  const std::string jecFileAK8_2018;

  const std::string era;


  // selection criterias
  std::vector<JetID> Jet_ID;
  std::vector<PUJetIDWP> PUJetID_WP;

  // some variables neccessary for systematics
  std::string jetTypeLabelForJECUncertainty;
  std::string jecUncertaintyTxtFileName;
  std::map<std::string, std::unique_ptr<JetCorrectionUncertainty>> jecUncertainties_;
  const JetCorrector *corrector;
  std::string correctorlabel = "";
  const bool doJES = true;
  const std::map<std::string, std::vector<std::string>> groups = {
          { "JESAbsolute", { "JESAbsoluteMPFBias", "JESAbsoluteScale", "JESFragmentation", "JESPileUpDataMC", "JESPileUpPtRef", "JESRelativeFSR", "JESSinglePionECAL", "JESSinglePionHCAL" } },
          { "JESAbsoluteyear", { "JESAbsoluteStat", "JESRelativeStatFSR", "JESTimePtEta" } },
          { "JESFlavorQCD", { "JESFlavorQCD" } },
          { "JESBBEC1", { "JESPileUpPtBB", "JESPileUpPtEC1", "JESRelativePtBB" } },
          { "JESBBEC1year", { "JESRelativeJEREC1", "JESRelativePtEC1", "JESRelativeStatEC" } },
          { "JESEC2", { "JESPileUpPtEC2" } },
          { "JESEC2year", { "JESRelativeJEREC2", "JESRelativePtEC2" } },
          { "JESHF", { "JESPileUpPtHF", "JESRelativeJERHF", "JESRelativePtHF" } },
          { "JESHFyear", { "JESRelativeStatHF" } },
          { "JESRelativeBal", { "JESRelativeBal" } },
          { "JESRelativeSampleyear", { "JESRelativeSample" } },

      };


};

#endif
