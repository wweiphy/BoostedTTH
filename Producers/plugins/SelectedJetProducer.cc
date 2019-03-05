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

// system include files
#include <memory>
#include <vector>
#include <utility>
#include <fstream>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/stream/EDProducer.h"
#include "FWCore/Framework/interface/ESHandle.h"

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

class SelectedJetProducer : public edm::stream::EDProducer<>
{
  public:
    explicit SelectedJetProducer(const edm::ParameterSet &);
    ~SelectedJetProducer();

    static void fillDescriptions(edm::ConfigurationDescriptions &descriptions);

  private:
    // some enums to make things nicer
    enum class JetID
    {
        Loose,
        Tight,
        none,
        jetMETcorrection
    };
    enum PUJetIDWP
    {
        none,
        loose,
        medium,
        tight
    };

    // member functions
    virtual void beginStream(edm::StreamID) override;
    virtual void produce(edm::Event &, const edm::EventSetup &) override;
    virtual void endStream() override;
    std::string systName(std::string name, SystematicsHelper::Type);
    bool fileExists(const std::string &fileName);
    void UpdateJetCorrectorUncertainties(const edm::EventSetup &iSetup);
    JetCorrectionUncertainty *CreateJetCorrectorUncertainty(const edm::EventSetup &iSetup, const std::string &jetTypeLabel, const std::string &uncertaintyLabel) const;
    std::vector<pat::Jet> GetSelectedJets(const std::vector<pat::Jet> &, const float iMinPt, const float iMaxAbsEta, const JetID, const PUJetIDWP = PUJetIDWP::none);
    bool isGoodJet(const pat::Jet &iJet, const float iMinPt, const float iMaxAbsEta, const JetID, const PUJetIDWP wp);
    std::vector<pat::Jet> GetUncorrectedJets(const std::vector<pat::Jet> &inputJets);
    std::vector<pat::Jet> GetDeltaRCleanedJets(const std::vector<pat::Jet> &inputJets, const std::vector<pat::Muon> &inputMuons, const std::vector<pat::Electron> &inputElectrons, const double deltaRCut);
    std::vector<pat::Jet> GetCorrectedJets(const std::vector<pat::Jet> &, const edm::Event &, const edm::EventSetup &, const edm::Handle<reco::GenJetCollection> &, const SystematicsHelper::Type iSysType = SystematicsHelper::NA, const bool &doJES = true, const bool &doJER = true, const float &corrFactor = 1, const float &uncFactor = 1);
    pat::Jet GetCorrectedJet(const pat::Jet &, const edm::Event &, const edm::EventSetup &, const edm::Handle<reco::GenJetCollection> &, const SystematicsHelper::Type iSysType = SystematicsHelper::NA, const bool doJES = true, const bool doJER = true, const float corrFactor = 1, const float uncFactor = 1);
    void ApplyJetEnergyCorrection(pat::Jet &jet, double &totalCorrFactor, const edm::Event &event, const edm::EventSetup &setup, const edm::Handle<reco::GenJetCollection> &genjets, const SystematicsHelper::Type iSysType, const bool doJES, const bool doJER, const bool addUserFloats, const float corrFactor, const float uncFactor);
    double GetJECUncertainty(const pat::Jet &jet, const edm::EventSetup &iSetup, const SystematicsHelper::Type iSysType);
    void AddJetCorrectorUncertainty(const edm::EventSetup &iSetup, const std::string &uncertaintyLabel);
    template <typename T>
    T GetSortedByPt(const T &);
    int TranslateJetPUIDtoInt(PUJetIDWP wp);

    //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
    //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
    //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
    //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

    std::string JetType;
    const bool isData;
    /** min pt of jet collections **/
    std::vector<double> ptMins;
    /** max eta of jet collections **/
    std::vector<double> etaMaxs;
    /** min dir to lepton for jets **/
    double leptonJetDr;

    /** apply jet energy correciton? **/
    const bool applyCorrection;
    const bool doJER;

    /** names of output jet collections **/
    std::vector<std::string> collectionNames;
    /** pileupjetid for collections **/
    std::vector<std::string> PUJetIDMins;
    /** jetid **/
    const std::string JetID_;
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
    const std::string jecFileAK4;
    const std::string jecFileAK8;

    // selection criterias
    JetID Jet_ID;
    std::vector<PUJetIDWP> PUJetID_WP;

    // some variables neccessary for systematics
    std::string jetTypeLabelForJECUncertainty;
    std::string jecUncertaintyTxtFileName;
    std::map<std::string, std::unique_ptr<JetCorrectionUncertainty>> jecUncertainties_;
    const JetCorrector *corrector;
    const bool doJES = true;
};
//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
SelectedJetProducer::SelectedJetProducer(const edm::ParameterSet &iConfig) : JetType{iConfig.getParameter<std::string>("JetType")},
                                                                             isData{iConfig.getParameter<bool>("isData")},
                                                                             ptMins{iConfig.getParameter<std::vector<double>>("ptMins")},
                                                                             etaMaxs{iConfig.getParameter<std::vector<double>>("etaMaxs")},
                                                                             leptonJetDr{iConfig.getParameter<double>("leptonJetDr")},
                                                                             applyCorrection{iConfig.getParameter<bool>("applyCorrection")},
                                                                             doJER{iConfig.getParameter<bool>("doJER")},
                                                                             collectionNames{iConfig.getParameter<std::vector<std::string>>("collectionNames")},
                                                                             PUJetIDMins{iConfig.getParameter<std::vector<std::string>>("PUJetIDMins")},
                                                                             JetID_{iConfig.getParameter<std::string>("JetID")},
                                                                             systematics_config{iConfig.getParameter<std::vector<std::string>>("systematics")},
                                                                             // inputs
                                                                             jetsToken{consumes<pat::JetCollection>(iConfig.getParameter<edm::InputTag>("jets"))},
                                                                             genjetsToken{consumes<reco::GenJetCollection>(iConfig.getParameter<edm::InputTag>("miniAODGenJets"))},
                                                                             muonsToken{consumes<pat::MuonCollection>(iConfig.getParameter<edm::InputTag>("muons"))},
                                                                             electronsToken{consumes<pat::ElectronCollection>(iConfig.getParameter<edm::InputTag>("electrons"))},
                                                                             rhoToken{consumes<double>(iConfig.getParameter<edm::InputTag>("rho"))},
                                                                             jecFileAK4{iConfig.getParameter<std::string>("jecFileAK4")},
                                                                             jecFileAK8{iConfig.getParameter<std::string>("jecFileAK8")}
{
    // do this for getJetCorrector call with JetType as argument, because it needs ak4... or ak8 ... instead of AK4... or AK8...
    JetType.replace(JetType.begin(), JetType.begin() + 2, "ak");

    // make sure everything is consistent
    assert(ptMins.size() == etaMaxs.size());
    assert(ptMins.size() == collectionNames.size());

    // load systematics
    for (uint i = 0; i < systematics_config.size(); i++)
    {
        try
        {
            systematics.push_back(SystematicsHelper::get(systematics_config[i]));
        }
        catch (cms::Exception &e)
        {
            throw cms::Exception("InvalidUncertaintyName") << "SelectedJetProducer: systematic name " << systematics_config[i] << " not recognized" << std::endl;
        }
    }

    // produce Jet collections
    produces<pat::JetCollection>("rawJets");
    for (uint i = 0; i < collectionNames.size(); i++)
    {
        for (uint j = 0; j < systematics.size(); j++)
        {
            produces<pat::JetCollection>(systName(collectionNames[i], systematics[j]));
        }
    }

    // set JEC File
    if (TString(JetType).Contains("ak4"))
    {
        jetTypeLabelForJECUncertainty = "AK4PFchs";
        jecUncertaintyTxtFileName = std::string(getenv("CMSSW_BASE")) + "/src/BoostedTTH/Producers/data/jec/" + jecFileAK4;
    }
    else if (TString(JetType).Contains("ak8"))
    {
        jetTypeLabelForJECUncertainty = "AK8PFchs";
        jecUncertaintyTxtFileName = std::string(getenv("CMSSW_BASE")) + "/src/BoostedTTH/Producers/data/jec/" + jecFileAK8;
    }

    if (jecUncertaintyTxtFileName != "")
    {
        if (!fileExists(jecUncertaintyTxtFileName))
        { // check if JEC uncertainty file exists
            throw cms::Exception("InvalidJECUncertaintyFile") << "No JEC uncertainty file '" << jecUncertaintyTxtFileName << "' found";
        }
    }
    else
    {
        throw cms::Exception("NoJECUncertaintyFile") << "No JEC uncertainty file specified";
    }
}

SelectedJetProducer::~SelectedJetProducer()
{
    // do anything here that needs to be done at destruction time
    // (e.g. close files, deallocate resources etc.)
}

//
// member functions
//

// check if a given file exists
bool SelectedJetProducer::fileExists(const std::string &fileName)
{
    std::ifstream infile(fileName.c_str());
    return infile.good();
}

// === Returned sorted input collection, by descending pT === //
template <typename T>
T SelectedJetProducer::GetSortedByPt(const T &collection)
{
    T result = collection;
    std::sort(result.begin(), result.end(), [](typename T::value_type a, typename T::value_type b) { return ptr(a)->pt() > ptr(b)->pt(); });
    return result;
}

void SelectedJetProducer::UpdateJetCorrectorUncertainties(const edm::EventSetup &iSetup)
{
    for (auto &jecUncIt : jecUncertainties_)
    {
        jecUncIt.second.reset(CreateJetCorrectorUncertainty(iSetup, jetTypeLabelForJECUncertainty, jecUncIt.first));
    }
}

void SelectedJetProducer::AddJetCorrectorUncertainty(const edm::EventSetup &iSetup, const std::string &uncertaintyLabel)
{
    jecUncertainties_[uncertaintyLabel] = std::unique_ptr<JetCorrectionUncertainty>(CreateJetCorrectorUncertainty(iSetup, jetTypeLabelForJECUncertainty, uncertaintyLabel));
}

// function to generate JetCorrectionUncertainty
JetCorrectionUncertainty *SelectedJetProducer::CreateJetCorrectorUncertainty(const edm::EventSetup &iSetup,
                                                                             const std::string &jetTypeLabel,
                                                                             const std::string &uncertaintyLabel) const
{
    try
    {
        JetCorrectorParameters jetCorPar;
        if (jecUncertaintyTxtFileName != "")
        {
            if (uncertaintyLabel == "Uncertainty")
            { // this is the key in the database but not in txt...
                jetCorPar = JetCorrectorParameters(jecUncertaintyTxtFileName, "Total");
            }
            else
            {
                jetCorPar = JetCorrectorParameters(jecUncertaintyTxtFileName, uncertaintyLabel);
            }
        }
        else
        {
            edm::ESHandle<JetCorrectorParametersCollection> JetCorParColl;
            iSetup.get<JetCorrectionsRecord>().get(jetTypeLabel, JetCorParColl);
            //JetCorrectorParameters const & JetCorPar = (*JetCorParColl)[uncertaintyLabel];
            jetCorPar = (*JetCorParColl)[uncertaintyLabel];
        }
        return new JetCorrectionUncertainty(jetCorPar);
    }
    catch (cms::Exception &e)
    {
        throw cms::Exception("InvalidJECUncertaintyLabel") << "No JEC uncertainty with label '" << uncertaintyLabel << "' found in event setup";
    }
    return 0;
}

// function to return Jets, whoch fullfill all IDs
std::vector<pat::Jet> SelectedJetProducer::GetSelectedJets(const std::vector<pat::Jet> &inputJets,
                                                           const float iMinPt, const float iMaxAbsEta, const JetID iJetID, const PUJetIDWP wp)
{
    // iterate through inputjets and find good Jets
    std::vector<pat::Jet> selectedJets;
    for (std::vector<pat::Jet>::const_iterator it = inputJets.begin(), ed = inputJets.end(); it != ed; ++it)
    {   
        std::cout << it->pt() << std::endl; 
        if (isGoodJet(*it, iMinPt, iMaxAbsEta, iJetID, wp))
            selectedJets.push_back(*it);
    }

    return selectedJets;
}

// return Systematic name
std::string SelectedJetProducer::systName(std::string name, SystematicsHelper::Type sysType)
{
    if (sysType == SystematicsHelper::NA)
        return name;
    else
        return name + SystematicsHelper::toString(sysType);
}

// function to check if Jet FullFills IDs
bool SelectedJetProducer::isGoodJet(const pat::Jet &iJet, const float iMinPt, const float iMaxAbsEta,
                                    const JetID iJetID, const PUJetIDWP wp)
{
    //   CheckVertexSetUp();

    // Transverse momentum requirement
    if (iJet.pt() < iMinPt)
        return false;

    // Absolute eta requirement
    if (fabs(iJet.eta()) > iMaxAbsEta)
        return false;

    // Jet ID
    bool loose = false;
    bool tight = false;
    bool goodForMETCorrection = false;

    if (iJetID != JetID::none && iJet.isPFJet())
    {
        // these are the loose requirements for Run 2016 80X
        loose = (iJet.neutralHadronEnergyFraction() < 0.99 &&
                 iJet.neutralEmEnergyFraction() < 0.99 &&
                 iJet.numberOfDaughters() > 1);
        // these are the tight requirements for Run 2017 90X. Since the tight JetID efficiency is > 99% everywhere for this era,
        // loose is not recommended anymore.
        tight = (iJet.neutralHadronEnergyFraction() < 0.90 &&
                 iJet.neutralEmEnergyFraction() < 0.90 &&
                 iJet.numberOfDaughters() > 1);

        if (fabs(iJet.eta()) < 2.4)
        {
            loose = (loose &&
                     iJet.chargedHadronEnergyFraction() > 0.0 &&
                     iJet.chargedMultiplicity() > 0 &&
                     iJet.chargedEmEnergyFraction() < 0.99);
            tight = (tight &&
                     iJet.chargedHadronEnergyFraction() > 0.0 &&
                     iJet.chargedMultiplicity() > 0
                     //iJet.chargedEmEnergyFraction() < 0.99
            );
        }

        if (iJetID == JetID::jetMETcorrection)
        { //only check this if asked, otherwise there could be problems
            goodForMETCorrection = (iJet.correctedJet(0).pt() > 10.0 &&
                                    ((!iJet.isPFJet() && iJet.emEnergyFraction() < 0.9) ||
                                     (iJet.isPFJet() && (iJet.neutralEmEnergyFraction() + iJet.chargedEmEnergyFraction()) < 0.9)));
        }
    }

    switch (iJetID)
    {
    // deprecated??
    // case JetID::jetPU:
    // case JetID::jetMinimal:
    // case JetID::jetLooseAOD:
    case JetID::none:
    case JetID::jetMETcorrection:
        if (!goodForMETCorrection)
            return false;
        break;

    case JetID::Loose:
        if (!loose)
            return false;
        break;
    case JetID::Tight:
        if (!tight)
            return false;
        break;
    default:
        break;
    }
    // PileUP Jet ID
    if (iJet.hasUserInt("pileupJetId:fullId"))
    {
        if (iJet.userInt("pileupJetId:fullId") < TranslateJetPUIDtoInt(wp))
            return false;
    }

    return true;
}

// function to Translate PUJetIDWP into its corresponding int
int SelectedJetProducer::TranslateJetPUIDtoInt(PUJetIDWP wp)
{
    if (wp == PUJetIDWP::loose)
        return 4;
    else if (wp == PUJetIDWP::medium)
        return 6;
    else if (wp == PUJetIDWP::tight)
        return 7;
    else
        return 0;
}

// function to return Jets without any correction
std::vector<pat::Jet> SelectedJetProducer::GetUncorrectedJets(const std::vector<pat::Jet> &inputJets)
{
    std::vector<pat::Jet> outputJets;
    outputJets.reserve(inputJets.size());
    // loop over inputJets and save a uncorrected version
    for (std::vector<pat::Jet>::const_iterator it = inputJets.begin(), ed = inputJets.end(); it != ed; ++it)
    {
        pat::Jet jet = (*it);
        jet.setP4(it->correctedJet(0).p4());
        outputJets.push_back(jet);
    }
    return outputJets;
}

// function to return Jets with no lepton inside a particular DeltaR
std::vector<pat::Jet> SelectedJetProducer::GetDeltaRCleanedJets(const std::vector<pat::Jet> &inputJets, const std::vector<pat::Muon> &inputMuons,
                                                                const std::vector<pat::Electron> &inputElectrons, const double deltaRCut)
{

    std::vector<pat::Jet> outputJets; //resulting jets
    // loop over inputJets
    for (std::vector<pat::Jet>::const_iterator iJet = inputJets.begin(); iJet != inputJets.end(); ++iJet)
    {
        bool isOverlap = false;
        // get Jet 4-momentum
        TLorentzVector jet_p4;
        jet_p4.SetPxPyPzE(iJet->px(), iJet->py(), iJet->pz(), iJet->energy());
        // loop over all electrons
        for (std::vector<pat::Electron>::const_iterator iEle = inputElectrons.begin(); iEle != inputElectrons.end(); iEle++)
        {
            // get electron 4-momentum
            TLorentzVector ele_p4;
            ele_p4.SetPxPyPzE(iEle->px(), iEle->py(), iEle->pz(), iEle->energy());
            //calculate DeltaR between Jet and electron
            double delta_tmp = jet_p4.DeltaR(ele_p4);
            if (delta_tmp < deltaRCut)
            { // check for overlap
                isOverlap = true;
                break;
            }
        }

        if (isOverlap)
            continue;

        // loop over all muons
        for (std::vector<pat::Muon>::const_iterator iMuon = inputMuons.begin(); iMuon != inputMuons.end(); iMuon++)
        {
            // get muon 4-momentum
            TLorentzVector muon_p4;
            muon_p4.SetPxPyPzE(iMuon->px(), iMuon->py(), iMuon->pz(), iMuon->energy());
            // calculate DeltaR between jet and electron
            double delta_tmp = jet_p4.DeltaR(muon_p4);
            if (delta_tmp < deltaRCut)
            { // check for overlap
                isOverlap = true;
                break;
            }
        }

        if (isOverlap)
            continue;

        // save Jet if no overlap is found
        outputJets.push_back(*iJet);
    }
    return outputJets;
}

// function to return a vector of corrected Jets
std::vector<pat::Jet> SelectedJetProducer::GetCorrectedJets(const std::vector<pat::Jet> &inputJets, const edm::Event &event,
                                                            const edm::EventSetup &setup, const edm::Handle<reco::GenJetCollection> &genjets,
                                                            const SystematicsHelper::Type iSysType, const bool &doJES, const bool &doJER,
                                                            const float &corrFactor, const float &uncFactor)
{
    // do nothing if neither JES or JER is demanded
    if (!doJES && !doJER)
        return inputJets;

    //resulting corrected Jets
    std::vector<pat::Jet> outputJets;

    //loop over input jets and correct each one
    for (std::vector<pat::Jet>::const_iterator it = inputJets.begin(), ed = inputJets.end(); it != ed; ++it)
    {
        outputJets.push_back(GetCorrectedJet(*it, event, setup, genjets, iSysType, doJES, doJER, corrFactor, uncFactor));
    }
    return outputJets;
}

// function to return one corrected Jet
pat::Jet SelectedJetProducer::GetCorrectedJet(const pat::Jet &inputJet, const edm::Event &event,
                                              const edm::EventSetup &setup, const edm::Handle<reco::GenJetCollection> &genjets,
                                              const SystematicsHelper::Type iSysType, const bool doJES, const bool doJER,
                                              const float corrFactor, const float uncFactor)
{
    double factor = 1.;
    pat::Jet outputJet = inputJet;
    bool addUserFloats = true;
    ApplyJetEnergyCorrection(outputJet, factor, event, setup, genjets, iSysType, doJES, doJER, addUserFloats, corrFactor, uncFactor);

    return outputJet;
}

// function to apply JES, JER needs to be implemente (is currently done via SmearedJetProducer)
void SelectedJetProducer::ApplyJetEnergyCorrection(pat::Jet &jet, double &totalCorrFactor, const edm::Event &event, const edm::EventSetup &setup,
                                                   const edm::Handle<reco::GenJetCollection> &genjets, const SystematicsHelper::Type iSysType,
                                                   const bool doJES, const bool doJER,
                                                   const bool addUserFloats,
                                                   const float corrFactor, const float uncFactor)
{
    totalCorrFactor = 1.;
    if (doJES || doJER)
    { // check again if JES or JER is demanded
        /// JES
        if (doJES)
        {
            double scale = 1.;
            if (corrector)
            {
                scale = corrector->correction(jet, event, setup);
            }
            else
            {
                edm::LogError("SelectedJetProducer") << "Trying to use GetCorrectedJets() without setting jet corrector!";
            }

            const double jec = scale * corrFactor;
            jet.scaleEnergy(jec);
            totalCorrFactor *= jec;

            if (addUserFloats)
            {
                jet.addUserFloat("HelperJES", scale);
                const double uncUp = GetJECUncertainty(jet, setup, SystematicsHelper::JESup);
                const double uncDown = GetJECUncertainty(jet, setup, SystematicsHelper::JESdown);
                const double jecvarUp = 1. + (uncUp);
                const double jecvarDown = 1. + (uncDown);
                jet.addUserFloat("HelperJESup", jecvarUp);
                jet.addUserFloat("HelperJESdown", jecvarDown);
            }

            if (SystematicsHelper::isJECUncertainty(iSysType))
            {
                const double unc = GetJECUncertainty(jet, setup, iSysType);
                const double jecvar = 1. + (unc * uncFactor);
                if (addUserFloats)
                {
                    jet.addUserFloat("Helper" + SystematicsHelper::toString(iSysType), jecvar);
                }
                jet.scaleEnergy(jecvar);
                totalCorrFactor *= jecvar;
            }
            // implement on demand
            // if (doJER){
            //}
        }
    }
}

// Return the JEC uncertainty value
// Scale JES by (1+value) to apply uncertainty
// Note: for JEC down, value will internally be multiplied by -1
// --> *always* scale JES by (1+value).
double SelectedJetProducer::GetJECUncertainty(const pat::Jet &jet, const edm::EventSetup &iSetup, const SystematicsHelper::Type iSysType)
{
    const std::string uncertaintyLabel = SystematicsHelper::GetJECUncertaintyLabel(iSysType);
    std::map<std::string, std::unique_ptr<JetCorrectionUncertainty>>::iterator jecUncIt = jecUncertainties_.find(uncertaintyLabel);
    if (jecUncIt == jecUncertainties_.end())
    { // Lazy initialization
        AddJetCorrectorUncertainty(iSetup, uncertaintyLabel);
        jecUncIt = jecUncertainties_.find(uncertaintyLabel);
    }
    JetCorrectionUncertainty *unc = jecUncIt->second.get();

    unc->setJetEta(jet.eta());
    unc->setJetPt(jet.pt()); // here you must use the CORRECTED jet pt
    if (SystematicsHelper::isJECUncertaintyUp(iSysType))
        return +1. * unc->getUncertainty(true);
    else
        return -1. * unc->getUncertainty(false);
}

// ------------ method called to produce the data  ------------
void SelectedJetProducer::produce(edm::Event &iEvent, const edm::EventSetup &iSetup)
{
    using namespace edm;
    UpdateJetCorrectorUncertainties(iSetup);

    edm::Handle<double> hRho;
    iEvent.getByToken(rhoToken, hRho);
    if (not hRho.isValid())
    {
        std::cerr << "\n\nERROR: retrieved pile-up energy density is not valid" << std::endl;
        throw std::exception();
    }

    edm::Handle<pat::JetCollection> inputJets;
    iEvent.getByToken(jetsToken, inputJets);
    if (not inputJets.isValid())
    {
        std::cerr << "\n\nERROR: retrieved jet collection is not valid" << std::endl;
        throw std::exception();
    }

    edm::Handle<reco::GenJetCollection> genJets;
    if (!isData)
    {
        iEvent.getByToken(genjetsToken, genJets);
        if (not genJets.isValid())
        {
            std::cerr << "\n\nERROR: retrieved genjet collection is not valid" << std::endl;
            throw std::exception();
        }
    }

    edm::Handle<pat::ElectronCollection> inputElectrons;
    iEvent.getByToken(electronsToken, inputElectrons);
    if (not inputElectrons.isValid())
    {
        std::cerr << "\n\nERROR: retrieved electron collection is not valid" << std::endl;
        throw std::exception();
    }

    edm::Handle<pat::MuonCollection> inputMuons;
    iEvent.getByToken(muonsToken, inputMuons);
    if (not inputMuons.isValid())
    {
        std::cerr << "\n\nERROR: retrieved muon collection is not valid" << std::endl;
        throw std::exception();
    }

    //translate Jet_ID
    if (JetID_ == "none")
        Jet_ID = JetID::none;
    else if (JetID_ == "loose")
        Jet_ID = JetID::Loose;
    else if (JetID_ == "tight")
        Jet_ID = JetID::Tight;
    else
    {
        std::cerr << "\n\nERROR: No matching JetID found for: " << JetID_ << std::endl;
        throw std::exception();
    }

    //translate Jet_PUID
    // fill Jet_PUIDs with default values
    PUJetID_WP = std::vector<PUJetIDWP>(PUJetIDMins.size(), PUJetIDWP::loose);
    for (size_t i = 0; i < PUJetIDMins.size(); i++)
    {
        if (PUJetIDMins[i] == "none")
            PUJetID_WP[i] = PUJetIDWP::none;
        else if (PUJetIDMins[i] == "loose")
            PUJetID_WP[i] = PUJetIDWP::loose;
        else if (PUJetIDMins[i] == "medium")
            PUJetID_WP[i] = PUJetIDWP::medium;
        else if (PUJetIDMins[i] == "tight")
            PUJetID_WP[i] = PUJetIDWP::tight;
        else
        {
            std::cerr << "\n\nERROR: No matching PUJetID_WP found for: " << PUJetIDMins[i] << std::endl;
            throw std::exception();
        }
    }

    // selected jets with jet ID cuts ( do this before jet energy correction !!! )
    const std::vector<pat::Jet> idJets = GetSelectedJets(*inputJets, 0., 9999., Jet_ID);

    std::vector<std::vector<pat::Jet>> unsortedJets;
    if (applyCorrection)
    {
        // initialize jetcorrector
        corrector = JetCorrector::getJetCorrector(JetType + "L1L2L3", iSetup);

        // Get raw jets
        std::vector<pat::Jet> rawJets = GetUncorrectedJets(idJets);
        std::unique_ptr<pat::JetCollection> rawJets_ = std::make_unique<pat::JetCollection>(rawJets);
        iEvent.put(std::move(rawJets_), "rawJets");
        // Clean muons and electrons from jets
        std::vector<pat::Jet> cleanJets = GetDeltaRCleanedJets(rawJets, *inputMuons, *inputElectrons, leptonJetDr);
        // Apply jet corrections
        // Get genjets for new JER recommendation (JER is done in extra producer SmearedJetProducer, the manual JER application is therefore disabled doJER=false)
        for (uint i = 0; i < systematics.size(); i++)
        {
            unsortedJets.push_back(GetCorrectedJets(cleanJets, iEvent, iSetup, genJets, systematics[i], doJES, doJER));
        }
    }

    // if no correction is to be applied, still remove jets close to a lepton
    else
    {
        for (uint i = 0; i < systematics.size(); i++)
        {
            unsortedJets.push_back(GetDeltaRCleanedJets(idJets, *inputMuons, *inputElectrons, leptonJetDr));
        }
    }
    // loop over all jetcollections and each systematic and apply pt,eta as well as pujetid cut on them
    for (uint i = 0; i < ptMins.size(); i++)
    {
        for (uint j = 0; j < systematics.size(); j++)
        {
            //Get jet Collection which passes selections
            std::vector<pat::Jet> selectedJets_unsorted = GetSelectedJets(unsortedJets[j], ptMins[i], etaMaxs[i], JetID::none, PUJetID_WP[i]);
            // sort the selected jets with respect to pt
            std::unique_ptr<pat::JetCollection> selectedJets = std::make_unique<pat::JetCollection>(GetSortedByPt(selectedJets_unsorted));
            iEvent.put(std::move(selectedJets), systName(collectionNames[i], systematics[j]));
        }
    }
}

// ------------ method called once each stream before processing any runs, lumis or events  ------------
void
    SelectedJetProducer::beginStream(edm::StreamID)
{
}

// ------------ method called once each stream after processing all runs, lumis and events  ------------
void SelectedJetProducer::endStream()
{
}

// ------------ method called when starting to processes a run  ------------
/*
void
SelectedJetProducer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void
SelectedJetProducer::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void
SelectedJetProducer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void
SelectedJetProducer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void SelectedJetProducer::fillDescriptions(edm::ConfigurationDescriptions &descriptions)
{
    //The following says we do not know what parameters are allowed so do no validation
    // Please change this to state exactly what you do use, even if it is no parameters
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(SelectedJetProducer);
