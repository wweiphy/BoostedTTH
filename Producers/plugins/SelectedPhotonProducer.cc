#include "BoostedTTH/Producers/interface/SelectedPhotonProducer.h"

SelectedPhotonProducer::SelectedPhotonProducer(const edm::ParameterSet& iConfig) :

    ptMins_ {iConfig.getParameter< std::vector<double> >("ptMins")},
    etaMaxs_ {iConfig.getParameter< std::vector<double> >("etaMaxs")},
    collectionNames_ {iConfig.getParameter< std::vector<std::string> >("collectionNames")},
    ids_ {iConfig.getParameter< std::vector<std::string> >("IDs")},
    
    // inputs
    EDMRhoToken{consumes< double >                  (iConfig.getParameter<edm::InputTag>("rho"))},
    EDMVertexToken{consumes< reco::VertexCollection >  (iConfig.getParameter<edm::InputTag>("vertices"))},
    EDMPhotonsToken{consumes< pat::PhotonCollection >(iConfig.getParameter<edm::InputTag>("photons"))}

{    
    if( era.find("2016")==std::string::npos and era.find("2017")==std::string::npos and era.find("2018")==std::string::npos){
        std::cerr << "\n\nERROR: Unknown era" << era << "in SelectedPhotonProducer " << std::endl;
        std::cerr << "Please select '2016' or '2017' or '2018'\n" << std::endl;
        throw std::exception();
    }
    
    photonIDs_        = std::vector<PhotonID>(ids_.size(),PhotonID::Loose);
    
    assert(ptMins_.size()==etaMaxs_.size());
    assert(ids_.size()==etaMaxs_.size());
    assert(collectionNames_.size()==etaMaxs_.size());
    
    for(size_t i=0; i<ptMins_.size(); i++){
        if(      ids_.at(i) == "loose"   )         photonIDs_.at(i) = PhotonID::Loose;
        else if( ids_.at(i) == "medium"  )         photonIDs_.at(i) = PhotonID::Medium;
        else if( ids_.at(i) == "tight"   )         photonIDs_.at(i) = PhotonID::Tight;
        else if( ids_.at(i) == "veto"   )          photonIDs_.at(i) = PhotonID::Veto;
        else if( ids_.at(i) == "none"   )          photonIDs_.at(i) = PhotonID::None;
        else {
            std::cerr << "\n\nERROR: No matching photon ID type found for: " << ids_.at(i) << std::endl;
            throw std::exception();
        }
    }
    
    for(size_t i=0;i<ptMins_.size();i++){
        produces<pat::PhotonCollection>(collectionNames_[i]);
    }
}

SelectedPhotonProducer::~SelectedPhotonProducer() {}

void
SelectedPhotonProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    // get the vertices and the rho (average pile-up energy density per unit area in the phi-eta plane)
    edm::Handle<reco::VertexCollection> hVtxs;
    iEvent.getByToken(EDMVertexToken,hVtxs);
    if(not hVtxs.isValid()) {
        std::cerr << "\n\nERROR: retrieved vertex collection is not valid" << std::endl;
        throw std::exception();
    }
    else if(hVtxs->empty()) {
        std::cerr << "\n\nERROR: retrieved vertex collection is empty" << std::endl;
        throw std::exception();
    }
    // primary vertex
    vertex = hVtxs->at(0);
    
    edm::Handle<double> hRho;
    iEvent.getByToken(EDMRhoToken,hRho);
    if(not hRho.isValid()) {
        std::cerr << "\n\nERROR: retrieved pile-up energy density is not valid" << std::endl;
        throw std::exception();
    }
    //pile-up density
    rho = *hRho;
    
    // get input photon collection
    edm::Handle< pat::PhotonCollection > inputPhotons;
    iEvent.getByToken(EDMPhotonsToken,inputPhotons);
    if(not inputPhotons.isValid()) {
        std::cerr << "\n\nERROR: retrieved photon collection is not valid" << std::endl;
        throw std::exception();
    }
    
    for(size_t i=0; i<ptMins_.size(); i++) {
        std::vector<pat::Photon> updatedPhotons = *inputPhotons;
        std::vector<pat::Photon> selectedPhotons = GetSortedByPt(GetSelectedPhotons(updatedPhotons,ptMins_.at(i),etaMaxs_.at(i),photonIDs_.at(i)));
        // produce the different photon collections and create a unique ptr to it      
        std::unique_ptr<pat::PhotonCollection> selectedPhotons_ptr =  std::make_unique<pat::PhotonCollection>(selectedPhotons);
        
        // put the collection into the event with help of the unique ptr
        iEvent.put(std::move(selectedPhotons_ptr),collectionNames_.at(i));
    }
}

// ------------ method called once each job just before starting event loop  ------------
void
SelectedPhotonProducer::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void
SelectedPhotonProducer::endJob() {
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
SelectedPhotonProducer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

std::vector<pat::Photon> SelectedPhotonProducer::GetSelectedPhotons(const std::vector<pat::Photon>& inputPhotons, const float iMinPt, const float iMaxEta, const PhotonID photonID)
{
    std::vector<pat::Photon> selectedPhotons;

    for( std::vector<pat::Photon>::const_iterator it = inputPhotons.begin(), ed = inputPhotons.end(); it != ed; ++it ){
        if( isGoodPhoton(*it,iMinPt,iMaxEta,photonID) ) selectedPhotons.push_back(*it);
    }

    return selectedPhotons;
}

bool SelectedPhotonProducer::isGoodPhoton(const pat::Photon& iPhoton, const float iMinPt, const float iMaxEta, const PhotonID iPhotonID)
{
    bool passesKinematics = (iMinPt<=iPhoton.pt()) and (iMaxEta>=fabs(iPhoton.eta()));
    bool inCrack = false;
    bool passesID = false;
    
    double absSCeta = 999; 
    if( iPhoton.superCluster().isAvailable() ){
        absSCeta = fabs(iPhoton.superCluster()->position().eta());
        inCrack = (absSCeta>1.4442 and absSCeta<1.5660 );
    }
    
    
    switch(iPhotonID){
        case PhotonID::None:
            passesID = true;
            break;
        case PhotonID::Veto:
            passesID = iPhoton.photonID("cutBasedPhotonID-Fall17-94X-V2-veto");
            break;
        case PhotonID::Loose:
            passesID = iPhoton.photonID("cutBasedPhotonID-Fall17-94X-V2-loose");
            break;
        case PhotonID::Medium:
            passesID = iPhoton.photonID("cutBasedPhotonID-Fall17-94X-V2-medium");
            break;
        case PhotonID::Tight:
            passesID = iPhoton.photonID("cutBasedPhotonID-Fall17-94X-V2-tight");
            break;
        default:
            std::cerr << "\n\nERROR: InvalidPhotonID" <<  std::endl;
            throw std::exception();
    }
    
    return passesKinematics and (not inCrack) and passesID;
}

template <typename T> T SelectedPhotonProducer::GetSortedByPt(const T& collection){
    T result = collection;
    std::sort(result.begin(), result.end(), [] (typename T::value_type a, typename T::value_type b) { return a.pt() > b.pt();});
    return result;
}

//define this as a plug-in
DEFINE_FWK_MODULE(SelectedPhotonProducer);