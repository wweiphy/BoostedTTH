#include "BoostedTTH/BoostedAnalyzer/interface/SpinCorrelationProcessor.hpp"

TLorentzVector Boost(TLorentzVector in_vec, Int_t frame_number, TLorentzVector vec_top_, TLorentzVector vec_antitop_){
  TLorentzVector out_vec=in_vec;
  //cout << "out_vec pt before boost: " << out_vec.Pt() << endl;
  //cout << "boost frame_number: " << frame_number << endl;
  switch(frame_number){
    case 0:
      break;
    case 1:
      out_vec.Boost(- (vec_top_+vec_antitop_).BoostVector() );
      break;
    case 2:
      out_vec.Boost(- vec_top_.BoostVector() );
      break;
    case 3:
      out_vec.Boost(- vec_antitop_.BoostVector() );
      break;
  }
  //cout << "out_vec pt after boost: " << out_vec.Pt() << endl;
  return out_vec;
}

void SetAllVectors(TLorentzVector& vec_top_, TLorentzVector& vec_antitop_, TLorentzVector& vec_b_, TLorentzVector& vec_antib_, TLorentzVector& vec_lepton_, TLorentzVector& vec_antilepton_, int identifier){
  
  //cout << "frame identifier: " << identifier << endl;
  
  TLorentzVector vec_lepton_tmp=vec_lepton_;
  TLorentzVector vec_antilepton_tmp=vec_antilepton_;
  TLorentzVector vec_b_tmp=vec_b_;
  TLorentzVector vec_antib_tmp=vec_antib_;
  TLorentzVector vec_top_tmp=vec_top_;
  TLorentzVector vec_antitop_tmp=vec_antitop_;
  
    /*cout << "top pt before: " << vec_top_.Pt() << endl;
    cout << "antitop pt before: " << vec_antitop_.Pt() << endl;
    cout << "b pt before: " << vec_b_.Pt() << endl;
    cout << "antib pt before: " << vec_antib_.Pt() << endl;
    cout << "lepton pt before: " << vec_lepton_.Pt() << endl;
    cout << "antilepton pt before: " << vec_antilepton_.Pt() << endl;*/
  
  switch(identifier) {
    case 4:
      vec_lepton_=Boost(vec_lepton_tmp,1,vec_top_tmp,vec_antitop_tmp);//boost lepton in ttbar cm system
      vec_antilepton_=Boost(vec_antilepton_tmp,1,vec_top_tmp,vec_antitop_tmp);//boost antilepton in ttbar cm system
      vec_lepton_=Boost(vec_lepton_,3,Boost(vec_top_tmp,1,vec_top_tmp,vec_antitop_tmp),Boost(vec_antitop_tmp,1,vec_top_tmp,vec_antitop_tmp));//boost lepton in antitop rest frame
      vec_antilepton_=Boost(vec_antilepton_,2,Boost(vec_top_tmp,1,vec_top_tmp,vec_antitop_tmp),Boost(vec_antitop_tmp,1,vec_top_tmp,vec_antitop_tmp));//boost antilepton in top rest frame
      vec_b_=Boost(vec_b_tmp,1,vec_top_tmp,vec_antitop_tmp);//boost b quark in ttbar cm system
      vec_antib_=Boost(vec_antib_tmp,1,vec_top_tmp,vec_antitop_tmp);//boost anti b quark in ttbar cm system
      vec_b_=Boost(vec_b_,2,Boost(vec_top_tmp,1,vec_top_tmp,vec_antitop_tmp),Boost(vec_antitop_tmp,1,vec_top_tmp,vec_antitop_tmp));//boost b quark in top rest frame
      vec_antib_=Boost(vec_antib_,3,Boost(vec_top_tmp,1,vec_top_tmp,vec_antitop_tmp),Boost(vec_antitop_tmp,1,vec_top_tmp,vec_antitop_tmp));//boost anti b quark in antitop rest frame
      vec_top_=Boost(vec_top_tmp,1,vec_top_tmp,vec_antitop_tmp);
      vec_antitop_=Boost(vec_antitop_tmp,1,vec_top_tmp,vec_antitop_tmp);
      //vec_top_=Boost(vec_top_,2,Boost(vec_top_tmp,1,vec_top_tmp,vec_antitop_tmp),Boost(vec_antitop_tmp,1,vec_top_tmp,vec_antitop_tmp));
      //vec_antitop_=Boost(vec_antitop_,3,Boost(vec_top_tmp,1,vec_top_tmp,vec_antitop_tmp),Boost(vec_antitop_tmp,1,vec_top_tmp,vec_antitop_tmp));
      break;
    default:
      vec_lepton_=Boost(vec_lepton_tmp,identifier,vec_top_tmp,vec_antitop_tmp);//boost lepton in corresponding system
      vec_antilepton_=Boost(vec_antilepton_tmp,identifier,vec_top_tmp,vec_antitop_tmp);//boost antilepton in corresponding system
      vec_top_=Boost(vec_top_tmp,identifier,vec_top_tmp,vec_antitop_tmp);
      vec_antitop_=Boost(vec_antitop_tmp,identifier,vec_top_tmp,vec_antitop_tmp);
      vec_b_=Boost(vec_b_tmp,identifier,vec_top_tmp,vec_antitop_tmp);//boost b quark in corresponding system
      vec_antib_=Boost(vec_antib_tmp,identifier,vec_top_tmp,vec_antitop_tmp);//boost anti b quark in corresponding system
      break;
  }
  
    /*cout << "top pt after: " << vec_top_.Pt() << endl;
    cout << "antitop pt after: " << vec_antitop_.Pt() << endl;
    cout << "b pt after: " << vec_b_.Pt() << endl;
    cout << "antib pt after: " << vec_antib_.Pt() << endl;
    cout << "lepton pt after: " << vec_lepton_.Pt() << endl;
    cout << "antilepton pt after: " << vec_antilepton_.Pt() << endl;*/
}

Double_t GetVars(TLorentzVector vec_top_, TLorentzVector vec_antitop_, TLorentzVector vec_b_,TLorentzVector vec_antib_, TLorentzVector vec_lepton_,TLorentzVector vec_antilepton_, Int_t var_number) {
  double out=-1;
  //cout << "var number 2: " << var_number << endl;
  switch(var_number) {
  
    case 0:
      out=TMath::Cos((vec_b_.Vect()).Angle(vec_antib_.Vect()));
      break;
    case 1:
      out=TMath::Abs(vec_b_.Eta()-vec_antib_.Eta());
      break;
    case 2:
      out=TMath::Abs(vec_b_.Phi()-vec_antib_.Phi());
      if(out>TMath::Pi()){
 	out=2*TMath::Pi()-out;
      }
      break;
    case 3:
      out=TMath::Cos((vec_lepton_.Vect()).Angle(vec_antilepton_.Vect()));
      break;
    case 4:
      out=TMath::Abs(vec_lepton_.Phi()-vec_antilepton_.Phi());
      if(out>TMath::Pi()){
 	out=2*TMath::Pi()-out;
      }
      break;
    case 5:
      out=TMath::Abs(vec_lepton_.Eta()-vec_antilepton_.Eta());
      break;
    case 6:
      out=TMath::Cos((vec_lepton_.Vect()).Angle(vec_antitop_.Vect()));
      break;
    case 7:
      out=TMath::Cos((vec_antilepton_.Vect()).Angle(vec_top_.Vect()));
      break;
    case 8:
      out=TMath::Cos((vec_lepton_.Vect()).Angle(vec_b_.Vect()));
      break;
    case 9:
      out=TMath::Cos((vec_antilepton_.Vect()).Angle(vec_antib_.Vect()));
      break;
    case 10:
      out=TMath::Abs(vec_lepton_.Phi()-vec_b_.Phi());
      if(out>TMath::Pi()){
 	out=2*TMath::Pi()-out;
      }
      break;
    case 11:
      out=TMath::Abs(vec_antilepton_.Phi()-vec_antib_.Phi());
      if(out>TMath::Pi()){
 	out=2*TMath::Pi()-out;
      }
      break; 
    case 12:
      out=TMath::Cos((vec_lepton_.Vect()).Angle(vec_antitop_.Vect()))*TMath::Cos((vec_antilepton_.Vect()).Angle(vec_top_.Vect()));
      break;
    default:
      cerr << "no identifier for used variable" << endl;
  }
  return out;
}

//////////////////////////////////////////////////////////////////////////////////////////////////////

using namespace std;

SpinCorrelationProcessor::SpinCorrelationProcessor (){}
SpinCorrelationProcessor::~SpinCorrelationProcessor (){}

void SpinCorrelationProcessor::Init(const InputCollections& input,VariableContainer& vars){
  
  std::vector<TString> frames;
  std::vector<TString> variables;
  std::vector<TString> decay_type;
  
  frames.push_back("lab");
  frames.push_back("ttbar_cm");
  //frames.push_back("top_rest");
  //frames.push_back("antitop_rest");
  frames.push_back("special");
  
  variables.push_back("cos_theta_ll");
  variables.push_back("cos_theta_bb");
  variables.push_back("cos_theta_l");
  variables.push_back("cos_theta_lbar");
  variables.push_back("cos_theta_lb");
  variables.push_back("cos_theta_lbarbbar");
  variables.push_back("Delta_Phi_lb");
  variables.push_back("Delta_Phi_lbarbbar");
  variables.push_back("Delta_Phi_ll");
  variables.push_back("Delta_Phi_bb");
  variables.push_back("Delta_Eta_ll");
  variables.push_back("Delta_Eta_bb");
  variables.push_back("cos_theta_l_x_cos_theta_lbar");
  
  decay_type.push_back("GEN");
  decay_type.push_back("RECO");
  
  for(auto it_frames=frames.begin();it_frames!=frames.end();++it_frames) {
    for(auto it_variables=variables.begin();it_variables!=variables.end();++it_variables) {
      for(auto it_type=decay_type.begin();it_type!=decay_type.end();++it_type) {
	vars.InitVar((*it_type)+"__"+(*it_frames)+"__"+(*it_variables),-9.,"F");
      }
      //cout << (*it_frames)+"|"+(*it_variables) << " initialized " << endl;
    }
  }
  
  initialized=true;
  
}


void SpinCorrelationProcessor::Process(const InputCollections& input,VariableContainer& vars){
  if(!initialized) cerr << "tree processor not initialized" << endl;
 
  std::map<TString,int> frames;
  std::map<TString,int> variables;
  std::vector<TString> decay_type;
  
  frames["lab"]=0;
  frames["ttbar_cm"]=1;
  //frames["top_rest"]=2;
  //frames["antitop_rest"]=3;
  frames["special"]=4;
  
  decay_type.push_back("GEN");
  decay_type.push_back("RECO");
  
  
  variables["cos_theta_bb"]=0;
  variables["Delta_Eta_bb"]=1;
  variables["Delta_Phi_bb"]=2;
  
  
  
  if(!(input.genTopEvt.IsFilled()) && !(input.selectedJets.size()>=4)) {
    cerr << "Top Event isnt filled and reconstruction not possible! " << endl;
    return;
  }
  
  
  ///////////////////////////////////////////////////////////////////////////////////////////
  // Set Vectors, which are present in every ttbar event
  math::XYZTLorentzVector vec_top;
  math::XYZTLorentzVector vec_antitop;
  math::XYZTLorentzVector vec_b;
  math::XYZTLorentzVector vec_antib;
  math::XYZTLorentzVector vec_lepton;
  math::XYZTLorentzVector vec_antilepton;
  math::XYZTLorentzVector vec_zero(0.,0.,0.,0.);
  math::XYZTLorentzVector vec_top_tmp;
  math::XYZTLorentzVector vec_antitop_tmp;
  math::XYZTLorentzVector vec_b_tmp;
  math::XYZTLorentzVector vec_antib_tmp;
  
  bool isDL=false;
  bool isSL=false;
  int leptonflag=0;
  
  for(auto it_type=decay_type.begin();it_type!=decay_type.end();++it_type) {
    //cout << "GEN or RECO? " << *it_type << endl;
    TString dec_type=*it_type;
    //////////////////////////////////////////////////////////////////////////////////////////
    if(input.genTopEvt.IsFilled() && dec_type.EqualTo("GEN")){
      //cout << "GenTopEvt is filled and decay type GEN " << endl;
      std::vector<reco::GenParticle> tophad;
      std::vector<reco::GenParticle> bhad;
      std::vector<reco::GenParticle> toplep;
      std::vector<reco::GenParticle> blep;
      std::vector<reco::GenParticle> lep;
      tophad=input.genTopEvt.GetAllTopHads();
      bhad=input.genTopEvt.GetAllTopHadDecayQuarks();
      toplep=input.genTopEvt.GetAllTopLeps();
      blep=input.genTopEvt.GetAllTopLepDecayQuarks();
      lep=input.genTopEvt.GetAllLeptons();
      //additional_bs=input.genTopEvt.GetAdditionalBGenJets();
    
      if(tophad.size()==0 and toplep.size()==2) {
	isDL=true;
	isSL=false;
	//cout << "Dilepton Event! " << endl;
      }
      if(tophad.size()==1 and toplep.size()==1) {
	isSL=true;
	isDL=false;
	//cout << "Single Lepton Event! " << endl;
      }
      if(tophad.size()==2 and toplep.size()==0) {
	isSL=false;
	isDL=false;
	//cout << "Fully hadronic Event! " << endl;
	return;
      }
       
      for(auto it=tophad.begin();it!=tophad.end();++it) {
	if(it->pdgId()>0) { vec_top=it->p4(); }
	else if(it->pdgId()<0) { vec_antitop=it->p4(); }
      }
      for(auto it=toplep.begin();it!=toplep.end();++it) {
	if(it->pdgId()>0) { vec_top=it->p4(); }
	else if(it->pdgId()<0) { vec_antitop=it->p4(); }
      }
      for(auto it=bhad.begin();it!=bhad.end();++it) {
	if(it->pdgId()>0) { vec_b=it->p4(); }
	else if(it->pdgId()<0) { vec_antib=it->p4(); }
      }
      for(auto it=blep.begin();it!=blep.end();++it) {
	if(it->pdgId()>0) { vec_b=it->p4(); }
	else if(it->pdgId()<0) { vec_antib=it->p4(); }
      }
      ///////////////////////////////////////////////////////////////////////////////////////////

      
      if(isSL) {
	if(lep[0].pdgId()>0) {
	  vec_lepton=lep[0].p4();
	  vec_antilepton=vec_zero;
	  leptonflag=1;
	  //cout << "Lepton! " << endl;
	}
	else if(lep[0].pdgId()<0) {
	  vec_antilepton=lep[0].p4();
	  vec_lepton=vec_zero;
	  leptonflag=-1;
	  //cout << "Antilepton! " << endl;
	}   
      }
      
      if(isDL) {
	if(lep[0].pdgId()>0) {
	  vec_lepton=lep[0].p4();
	}
	else if(lep[0].pdgId()<0) {
	  vec_antilepton=lep[0].p4();
	}
	if(lep[1].pdgId()>0) {
	  vec_lepton=lep[1].p4();
	}
	else if(lep[1].pdgId()<0) {
	  vec_antilepton=lep[1].p4();
	}
      }
      vec_top_tmp=vec_top;
      vec_antitop_tmp=vec_antitop;
      vec_b_tmp=vec_b;
      vec_antib_tmp=vec_antib;
    }
    /////////////////////////////////////////////////////////////////////////////////////////////
    else if(input.selectedJets.size()>=4 && dec_type.EqualTo("RECO") && ((input.selectedElectrons.size()+input.selectedMuons.size())==1)){
      //cout << "N_jets>=4 and decay type RECO and Electrons+Muons==1" << endl;
      isSL=true;
      isDL=false;
      std::vector<TLorentzVector> jetvecs = BoostedUtils::GetTLorentzVectors(BoostedUtils::GetJetVecs(input.selectedJets));
      std::vector<float> jetcsvs;
      int ntags=0;
      for(auto j=input.selectedJets.begin(); j!=input.selectedJets.end(); j++){
	jetcsvs.push_back(MiniAODHelper::GetJetCSV(*j));
	if(BoostedUtils::PassesCSV(*j)) ntags++;
      }
      TLorentzVector lepvec = BoostedUtils::GetTLorentzVector(BoostedUtils::GetPrimLepVec(input.selectedElectrons,input.selectedMuons));
      TVector2 metvec(input.pfMET.px(),input.pfMET.py());
      if(input.genTopEvt.IsFilled()&&input.genTopEvt.IsSemiLepton()){
	vector<TLorentzVector> bs_true= BoostedUtils::GetTLorentzVectors(input.genTopEvt.GetHiggsDecayProductVecs());
	vector<TLorentzVector> qs_true= BoostedUtils::GetTLorentzVectors(input.genTopEvt.GetWQuarksVecs());
	if(bs_true.size()==2){
	  TLorentzVector bhad_true = BoostedUtils::GetTLorentzVector(input.genTopEvt.GetTopHadDecayQuarkVec());
	  TLorentzVector blep_true = BoostedUtils::GetTLorentzVector(input.genTopEvt.GetTopLepDecayQuarkVec());
	  TLorentzVector lep_true = BoostedUtils::GetTLorentzVector(input.genTopEvt.GetLeptonVec());
	  TLorentzVector nu_true = BoostedUtils::GetTLorentzVector(input.genTopEvt.GetNeutrinoVec());
	  mcmatcher.Setup(bhad_true,qs_true[0],qs_true[1],blep_true,lep_true,nu_true,bs_true[0],bs_true[1]);
	}
      }
      Interpretation** ints = generator.GenerateTTHInterpretations(jetvecs,jetcsvs,lepvec,metvec);
      uint nints = generator.GetNints();
      Interpretation* best_int_lr=0;
      float best_lr=-99999;
      //    float best_chi2=-99999;
      for(uint i=0; i<nints; i++){
	  // likelihood ratio good ttbar reco / combinatorial background
	  float lr=quality.TTLikelihood_comb(*(ints[i]));
	  // simple chi2 reconstruction using hadronic W and both to masses
	  /*	float chi2=quality.TTChi2(*(ints[i]));
	  if(chi2>best_chi2){
	      best_chi2=chi2;
	      best_int_chi2=ints[i];
	      }*/
	  if(lr>best_lr){
	      best_lr=lr;
	      best_int_lr=ints[i];
	  }
      }
      if(best_int_lr!=0) {
	if(input.selectedElectrons.size()==1){
	  leptonflag=-input.selectedElectrons[0].charge();
	  if(leptonflag>0) {
	    //cout << "Electron! " << endl;
	    vec_lepton.SetPxPyPzE(input.selectedElectrons[0].px(),input.selectedElectrons[0].py(),input.selectedElectrons[0].pz(),input.selectedElectrons[0].energy());
	    vec_antilepton=vec_zero;
	  }
	  else if(leptonflag<0) {
	    //cout << "Positron! " << endl;
	    vec_antilepton.SetPxPyPzE(input.selectedElectrons[0].px(),input.selectedElectrons[0].py(),input.selectedElectrons[0].pz(),input.selectedElectrons[0].energy());
	    vec_lepton=vec_zero;
	  }
	}
	if(input.selectedMuons.size()==1) {
	  leptonflag=-input.selectedMuons[0].charge();
	  if(leptonflag>0) {
	    //cout << "Muon! " << endl;
	    vec_lepton.SetPxPyPzE(input.selectedMuons[0].px(),input.selectedMuons[0].py(),input.selectedMuons[0].pz(),input.selectedMuons[0].energy());
	    vec_antilepton=vec_zero;
	  }
	  else if(leptonflag<0) {
	    //cout << "AntiMuon! " << endl;
	    vec_antilepton.SetPxPyPzE(input.selectedMuons[0].px(),input.selectedMuons[0].py(),input.selectedMuons[0].pz(),input.selectedMuons[0].energy());
	    vec_lepton=vec_zero;
	  }
	}
	if(leptonflag>0) {
	  vec_antitop.SetPxPyPzE(best_int_lr->TopLep().Px(),best_int_lr->TopLep().Py(),best_int_lr->TopLep().Pz(),best_int_lr->TopLep().E());
	  vec_top.SetPxPyPzE(best_int_lr->TopHad().Px(),best_int_lr->TopHad().Py(),best_int_lr->TopHad().Pz(),best_int_lr->TopHad().E());
	  vec_antib.SetPxPyPzE(best_int_lr->BLep().Px(),best_int_lr->BLep().Py(),best_int_lr->BLep().Pz(),best_int_lr->BLep().E());
	  vec_b.SetPxPyPzE(best_int_lr->BHad().Px(),best_int_lr->BHad().Py(),best_int_lr->BHad().Pz(),best_int_lr->BHad().E()); 
	}
	else if(leptonflag<0) {
	  vec_antitop.SetPxPyPzE(best_int_lr->TopHad().Px(),best_int_lr->TopHad().Py(),best_int_lr->TopHad().Pz(),best_int_lr->TopHad().E());
	  vec_top.SetPxPyPzE(best_int_lr->TopLep().Px(),best_int_lr->TopLep().Py(),best_int_lr->TopLep().Pz(),best_int_lr->TopLep().E());
	  vec_antib.SetPxPyPzE(best_int_lr->BHad().Px(),best_int_lr->BHad().Py(),best_int_lr->BHad().Pz(),best_int_lr->BHad().E());
	  vec_b.SetPxPyPzE(best_int_lr->BLep().Px(),best_int_lr->BLep().Py(),best_int_lr->BLep().Pz(),best_int_lr->BLep().E()); 
	}
	float dR_max=0.4;
	//cout << "vor dR" << endl;
	float dR_top=BoostedUtils::DeltaR(vec_top,vec_top_tmp);
	float dR_antitop=BoostedUtils::DeltaR(vec_antitop,vec_antitop_tmp);
	float dR_b=BoostedUtils::DeltaR(vec_b,vec_b_tmp);
	float dR_antib=BoostedUtils::DeltaR(vec_antib,vec_antib_tmp);
	//cout << "nach dR" << endl;
	if(dR_top>dR_max || dR_antitop>dR_max || dR_b>dR_max || dR_antib>dR_max) {
	  //cout << endl;
	  //cout << "reconstruction not correct, abort!! " << endl;
	  //cout << endl;
	  continue;
	}
	//cout << endl;
	//cout << "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!reconstruction succesfull!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!" << endl;
	//cout << endl;
      }
      else {
	//cout << "Interpretation = 0, abort!! " << endl;
	continue;
      }
    }
    
    else {
      //cout << "Neither Gen nor RECO reconstruction possible, abort!! " << endl;
      continue;
    }
    
    
    for(auto it_frames=frames.begin();it_frames!=frames.end();++it_frames) {
      TLorentzVector vec_lepton_=BoostedUtils::GetTLorentzVector(vec_lepton);
      TLorentzVector vec_antilepton_=BoostedUtils::GetTLorentzVector(vec_antilepton);
      TLorentzVector vec_top_=BoostedUtils::GetTLorentzVector(vec_top);
      TLorentzVector vec_antitop_=BoostedUtils::GetTLorentzVector(vec_antitop);
      TLorentzVector vec_b_=BoostedUtils::GetTLorentzVector(vec_b);
      TLorentzVector vec_antib_=BoostedUtils::GetTLorentzVector(vec_antib);
      //cout << "frame: " << it_frames->first << " " << it_frames->second << endl;
      SetAllVectors(vec_top_,vec_antitop_,vec_b_,vec_antib_,vec_lepton_,vec_antilepton_,it_frames->second);
      /*cout << "top m: " << vec_top_.M() << endl;
      cout << "antitop m: " << vec_antitop_.M() << endl;
      cout << "b m: " << vec_b_.M() << endl;
      cout << "antib m: " << vec_antib_.M() << endl;
      cout << "lepton m: " << vec_lepton_.M() << endl;
      cout << "antilepton m: " << vec_antilepton_.M() << endl;*/

      
      
      if(isSL) {
	if(leptonflag==1) {
	  variables["cos_theta_l"]=6;
	  variables["cos_theta_lb"]=8;
	  variables["Delta_Phi_lb"]=10;
	}
	if(leptonflag==-1) {
	  variables["cos_theta_lbar"]=7;
	  variables["cos_theta_lbarbbar"]=9;
	  variables["Delta_Phi_lbarbbar"]=11;
	}
      }
      if(isDL) {
	variables["cos_theta_ll"]=3;
	variables["Delta_Phi_ll"]=4;
	variables["Delta_Eta_ll"]=5;
	variables["cos_theta_l"]=6;
	variables["cos_theta_lbar"]=7;
	variables["cos_theta_lb"]=8;
	variables["cos_theta_lbarbbar"]=9;
	variables["Delta_Phi_lb"]=10;
	variables["Delta_Phi_lbarbbar"]=11; 
	variables["cos_theta_l_x_cos_theta_lbar"]=12;
      }

      for(auto it_variables=variables.begin();it_variables!=variables.end();++it_variables) {
	  vars.FillVar(*it_type+"__"+it_frames->first+"__"+it_variables->first,GetVars(vec_top_,vec_antitop_,vec_b_,vec_antib_,vec_lepton_,vec_antilepton_,it_variables->second));
	  //cout << *it_type+"__"+it_frames->first+"__"+it_variables->first << " filled with " << GetVars(vec_top_,vec_antitop_,vec_b_,vec_antib_,vec_lepton_,vec_antilepton_,it_variables->second) << endl;
	
      }
    }
  }
  
  
}