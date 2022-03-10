#include "BoostedTTH/BoostedAnalyzer/interface/MCMatchVarProcessor.hpp"

using namespace std;

MCMatchVarProcessor::MCMatchVarProcessor (){}
MCMatchVarProcessor::~MCMatchVarProcessor (){}


void MCMatchVarProcessor::Init(const InputCollections& input,VariableContainer& vars){

 
  vars.InitVar( "GenEvt_I_TTPlusCC",-1,"I" );
  vars.InitVar( "GenEvt_I_TTPlusBB",-1,"I" );
  vars.InitVar( "GenEvt_TTxId_FromProducer",-1,"I" );
  vars.InitVar( "N_GoodTagsM",-1,"I" );
  vars.InitVar( "N_MisTagsM",-1,"I" );
  
  vars.InitVar( "N_GenTopHad", -1, "I" );
  vars.InitVars( "GenTopHad_Pt",-9.,"N_GenTopHad" );
  vars.InitVars( "GenTopHad_Eta",-9.,"N_GenTopHad" );
  vars.InitVars( "GenTopHad_Phi",-9.,"N_GenTopHad" );
  vars.InitVars( "GenTopHad_E",-9.,"N_GenTopHad" );
  vars.InitVars( "GenTopHad_W_Pt",-9.,"N_GenTopHad" );
  vars.InitVars( "GenTopHad_B_Pt",-9.,"N_GenTopHad" );
  vars.InitVars( "GenTopHad_Q1_Pt",-9.,"N_GenTopHad" );
  vars.InitVars( "GenTopHad_Q2_Pt",-9.,"N_GenTopHad" );
  vars.InitVars( "GenTopHad_W_Eta",-9.,"N_GenTopHad" );
  vars.InitVars( "GenTopHad_B_Eta",-9.,"N_GenTopHad" );
  vars.InitVars( "GenTopHad_Q1_Eta",-9.,"N_GenTopHad" );
  vars.InitVars( "GenTopHad_Q2_Eta",-9.,"N_GenTopHad" );
  vars.InitVars( "GenTopHad_W_Phi",-9.,"N_GenTopHad" );
  vars.InitVars( "GenTopHad_B_Phi",-9.,"N_GenTopHad" );
  vars.InitVars( "GenTopHad_Q1_Phi",-9.,"N_GenTopHad" );
  vars.InitVars( "GenTopHad_Q2_Phi",-9.,"N_GenTopHad" );
  vars.InitVars( "GenTopHad_W_E",-9.,"N_GenTopHad" );
  vars.InitVars( "GenTopHad_B_E",-9.,"N_GenTopHad" );
  vars.InitVars( "GenTopHad_Q1_E",-9.,"N_GenTopHad" );
  vars.InitVars( "GenTopHad_Q2_E",-9.,"N_GenTopHad" );
 
  vars.InitVar( "N_GenTopLep",-1,"I" );
  vars.InitVars( "GenTopLep_Pt",-9.,"N_GenTopLep" );
  vars.InitVars( "GenTopLep_Eta",-9.,"N_GenTopLep" );
  vars.InitVars( "GenTopLep_Phi",-9.,"N_GenTopLep" );
  vars.InitVars( "GenTopLep_E",-9.,"N_GenTopLep" );
  vars.InitVars( "GenTopLep_W_Pt",-9.,"N_GenTopLep" );
  vars.InitVars( "GenTopLep_B_Pt",-9.,"N_GenTopLep" );
  vars.InitVars( "GenTopLep_Lep_Pt",-9.,"N_GenTopLep" );
  vars.InitVars( "GenTopLep_Nu_Pt",-9.,"N_GenTopLep" );
  vars.InitVars( "GenTopLep_W_Eta",-9.,"N_GenTopLep" );
  vars.InitVars( "GenTopLep_B_Eta",-9.,"N_GenTopLep" );
  vars.InitVars( "GenTopLep_Lep_Eta",-9.,"N_GenTopLep" );
  vars.InitVars( "GenTopLep_Nu_Eta",-9.,"N_GenTopLep" );
  vars.InitVars( "GenTopLep_W_Phi",-9.,"N_GenTopLep" );
  vars.InitVars( "GenTopLep_B_Phi",-9.,"N_GenTopLep" );
  vars.InitVars( "GenTopLep_Lep_Phi",-9.,"N_GenTopLep" );
  vars.InitVars( "GenTopLep_Nu_Phi",-9.,"N_GenTopLep" );
  vars.InitVars( "GenTopLep_W_E",-9.,"N_GenTopLep" );
  vars.InitVars( "GenTopLep_B_E",-9.,"N_GenTopLep" );
  vars.InitVars( "GenTopLep_Lep_E",-9.,"N_GenTopLep" );
  vars.InitVars( "GenTopLep_Nu_E",-9.,"N_GenTopLep" );
  
  vars.InitVar( "GenHiggs1_Pt",-9. );
  vars.InitVar( "GenHiggs1_Eta",-9. );
  vars.InitVar( "GenHiggs1_Phi",-9. );
  vars.InitVar( "GenHiggs1_E",-9. );
  vars.InitVar( "GenHiggs1_Y",-9. );
    
  vars.InitVar( "GenHiggs2_Pt",-9. );
  vars.InitVar( "GenHiggs2_Eta",-9. );
  vars.InitVar( "GenHiggs2_Phi",-9. );
  vars.InitVar( "GenHiggs2_E",-9. );
  vars.InitVar( "GenHiggs2_Y",-9. );
    
    
  vars.InitVar( "GenHiggs1_B1_Pt",-9. );
  vars.InitVar( "GenHiggs1_B2_Pt",-9. );
  vars.InitVar( "GenHiggs1_B1_Eta",-9. );
  vars.InitVar( "GenHiggs1_B2_Eta",-9. );
  vars.InitVar( "GenHiggs1_B1_Phi",-9. );
  vars.InitVar( "GenHiggs1_B2_Phi",-9. );
  vars.InitVar( "GenHiggs1_B1_E",-9. );
  vars.InitVar( "GenHiggs1_B2_E",-9. );
    
  vars.InitVar( "GenHiggs2_B3_Pt",-9. );
  vars.InitVar( "GenHiggs2_B4_Pt",-9. );
  vars.InitVar( "GenHiggs2_B3_Eta",-9. );
  vars.InitVar( "GenHiggs2_B4_Eta",-9. );
  vars.InitVar( "GenHiggs2_B3_Phi",-9. );
  vars.InitVar( "GenHiggs2_B4_Phi",-9. );
  vars.InitVar( "GenHiggs2_B3_E",-9. );
  vars.InitVar( "GenHiggs2_B4_E",-9. );
  
  vars.InitVar( "GenZ1_Pt",-9. );
  vars.InitVar( "GenZ1_Eta",-9. );
  vars.InitVar( "GenZ1_Phi",-9. );
  vars.InitVar( "GenZ1_E",-9. );
  vars.InitVar( "GenZ1_Y",-9. );
  vars.InitVar( "GenZ2_Pt",-9. );
  vars.InitVar( "GenZ2_Eta",-9. );
  vars.InitVar( "GenZ2_Phi",-9. );
  vars.InitVar( "GenZ2_E",-9. );
  vars.InitVar( "GenZ2_Y",-9. );
    
  vars.InitVar( "GenZ1_B1_Pt",-9. );
  vars.InitVar( "GenZ1_B2_Pt",-9. );
  vars.InitVar( "GenZ1_B1_Eta",-9. );
  vars.InitVar( "GenZ1_B2_Eta",-9. );
  vars.InitVar( "GenZ1_B1_Phi",-9. );
  vars.InitVar( "GenZ1_B2_Phi",-9. );
  vars.InitVar( "GenZ1_B1_E",-9. );
  vars.InitVar( "GenZ1_B2_E",-9. );
  vars.InitVar( "GenZ2_B3_Pt",-9. );
  vars.InitVar( "GenZ2_B4_Pt",-9. );
  vars.InitVar( "GenZ2_B3_Eta",-9. );
  vars.InitVar( "GenZ2_B4_Eta",-9. );
  vars.InitVar( "GenZ2_B3_Phi",-9. );
  vars.InitVar( "GenZ2_B4_Phi",-9. );
  vars.InitVar( "GenZ2_B3_E",-9. );
  vars.InitVar( "GenZ2_B4_E",-9. );
    
    
  vars.InitVar( "GenZH_Z_Pt",-9. );
  vars.InitVar( "GenZH_Z_Eta",-9. );
  vars.InitVar( "GenZH_Z_Phi",-9. );
  vars.InitVar( "GenZH_Z_E",-9. );
  vars.InitVar( "GenZH_Z_Y",-9. );
  vars.InitVar( "GenZH_H_Pt",-9. );
  vars.InitVar( "GenZH_H_Eta",-9. );
  vars.InitVar( "GenZH_H_Phi",-9. );
  vars.InitVar( "GenZH_H_E",-9. );
  vars.InitVar( "GenZH_H_Y",-9. );
  vars.InitVar( "GenZH_Z_B1_Pt",-9. );
  vars.InitVar( "GenZH_Z_B2_Pt",-9. );
  vars.InitVar( "GenZH_Z_B1_Eta",-9. );
  vars.InitVar( "GenZH_Z_B2_Eta",-9. );
  vars.InitVar( "GenZH_Z_B1_Phi",-9. );
  vars.InitVar( "GenZH_Z_B2_Phi",-9. );
  vars.InitVar( "GenZH_Z_B1_E",-9. );
  vars.InitVar( "GenZH_Z_B2_E",-9. );
  vars.InitVar( "GenZH_H_B3_Pt",-9. );
  vars.InitVar( "GenZH_H_B4_Pt",-9. );
  vars.InitVar( "GenZH_H_B3_Eta",-9. );
  vars.InitVar( "GenZH_H_B4_Eta",-9. );
  vars.InitVar( "GenZH_H_B3_Phi",-9. );
  vars.InitVar( "GenZH_H_B4_Phi",-9. );
  vars.InitVar( "GenZH_H_B3_E",-9. );
  vars.InitVar( "GenZH_H_B4_E",-9. );



  vars.InitVars( "GenTopHad_B_Idx",-1,"N_GenTopHad" );
  vars.InitVars( "GenTopHad_Q1_Idx",-1,"N_GenTopHad" );
  vars.InitVars( "GenTopHad_Q2_Idx",-1,"N_GenTopHad" );
  vars.InitVars( "GenTopLep_B_Idx",-1,"N_GenTopLep" );
  vars.InitVar( "GenHiggs_B1_Idx",-1 );
  vars.InitVar( "GenHiggs_B2_Idx",-1 );
  //vars.InitVar( "GenZ_B1_Idx",-1 );
  //vars.InitVar( "GenZ_B2_Idx",-1 );
  
  vars.InitVar( "GenHiggs_DecProd1_Pt",-9. );
  vars.InitVar( "GenHiggs_DecProd1_Eta",-9. );
  vars.InitVar( "GenHiggs_DecProd1_E",-9. );
  vars.InitVar( "GenHiggs_DecProd1_PDGID",-999 );
  vars.InitVar( "GenHiggs_DecProd2_Pt",-9. );
  vars.InitVar( "GenHiggs_DecProd2_Eta",-9. );
  vars.InitVar( "GenHiggs_DecProd2_E",-9. );
  vars.InitVar( "GenHiggs_DecProd2_PDGID",-999 );
    
    vars.InitVar( "N_GenHiggs_BBar", -1, "I" );
    vars.InitVar( "N_GenHiggs_B", -1, "I" );

  vars.InitVars( "GenHiggs_BBar_GenJet_Pt",-9., "N_GenHiggs_BBar" );
  vars.InitVars( "GenHiggs_B_GenJet_Pt",-9., "N_GenHiggs_B");
  vars.InitVars( "GenHiggs_BBar_GenJet_Eta",-9., "N_GenHiggs_BBar");
  vars.InitVars( "GenHiggs_B_GenJet_Eta",-9., "N_GenHiggs_B");
  vars.InitVars( "GenHiggs_BBar_GenJet_Phi",-9., "N_GenHiggs_BBar");
  vars.InitVars( "GenHiggs_B_GenJet_Phi",-9., "N_GenHiggs_B");
  vars.InitVars( "GenHiggs_BBar_GenJet_E",-9., "N_GenHiggs_BBar");
  vars.InitVars( "GenHiggs_B_GenJet_E",-9., "N_GenHiggs_B");
    
  vars.InitVar( "GenHiggs1_B_GenJet_M",-9 );
  vars.InitVar( "GenHiggs2_B_GenJet_M",-9 );
    
    vars.InitVar( "N_GenHiggs", -1, "I" );
  vars.InitVars( "GenHiggs_B_GenJet_M",-9, "N_GenHiggs" );

  vars.InitVars( "GenTopLep_B_GenJet_Pt",-9., "N_GenTopLep" );
  vars.InitVars( "GenTopHad_B_GenJet_Pt",-9., "N_GenTopHad");
  vars.InitVars( "GenTopLep_B_GenJet_Eta",-9., "N_GenTopLep" );
  vars.InitVars( "GenTopHad_B_GenJet_Eta",-9., "N_GenTopHad");
  vars.InitVars( "GenTopLep_B_GenJet_Phi",-9., "N_GenTopLep" );
  vars.InitVars( "GenTopHad_B_GenJet_Phi",-9., "N_GenTopHad");
  vars.InitVars( "GenTopLep_B_GenJet_E",-9., "N_GenTopLep" );
  vars.InitVars( "GenTopHad_B_GenJet_E",-9., "N_GenTopHad");


    vars.InitVar( "N_GenHiggs_BBar_Hadron", -1, "I" );
    vars.InitVar( "N_GenHiggs_B_Hadron", -1, "I" );

  vars.InitVars( "GenHiggs_BBar_Hadron_Pt",-9., "N_GenHiggs_BBar_Hadron" );
  vars.InitVars( "GenHiggs_B_Hadron_Pt",-9., "N_GenHiggs_B_Hadron");
  vars.InitVars( "GenHiggs_BBar_Hadron_Eta",-9., "N_GenHiggs_BBar_Hadron");
  vars.InitVars( "GenHiggs_B_Hadron_Eta",-9., "N_GenHiggs_B_Hadron");
  vars.InitVars( "GenHiggs_BBar_Hadron_Phi",-9., "N_GenHiggs_BBar_Hadron");
  vars.InitVars( "GenHiggs_B_Hadron_Phi",-9., "N_GenHiggs_B_Hadron");
  vars.InitVars( "GenHiggs_BBar_Hadron_E",-9., "N_GenHiggs_BBar_Hadron");
  vars.InitVars( "GenHiggs_B_Hadron_E",-9., "N_GenHiggs_B_Hadron");
    
  vars.InitVar( "GenHiggs1_B_Hadron_M",-9 );
  vars.InitVar( "GenHiggs2_B_Hadron_M",-9 );
    
    vars.InitVar( "N_GenHiggs_Hadron", -1, "I" );
  vars.InitVars( "GenHiggs_B_Hadron_M",-9, "N_GenHiggs_Hadron" );
    
//  vars.InitVar( "GenHiggs_B1_Hadron_Pt",-9. );
//  vars.InitVar( "GenHiggs_B2_Hadron_Pt",-9. );
//  vars.InitVar( "GenHiggs_B1_Hadron_Eta",-9. );
//  vars.InitVar( "GenHiggs_B2_Hadron_Eta",-9. );
//  vars.InitVar( "GenHiggs_B1_Hadron_Phi",-9. );
//  vars.InitVar( "GenHiggs_B2_Hadron_Phi",-9. );
//  vars.InitVar( "GenHiggs_B1_Hadron_E",-9. );
//  vars.InitVar( "GenHiggs_B2_Hadron_E",-9. );

  vars.InitVars( "GenTopLep_B_Hadron_Pt",-9., "N_GenTopLep" );
  vars.InitVars( "GenTopHad_B_Hadron_Pt",-9., "N_GenTopHad");
  vars.InitVars( "GenTopLep_B_Hadron_Eta",-9., "N_GenTopLep" );
  vars.InitVars( "GenTopHad_B_Hadron_Eta",-9., "N_GenTopHad");
  vars.InitVars( "GenTopLep_B_Hadron_Phi",-9., "N_GenTopLep" );
  vars.InitVars( "GenTopHad_B_Hadron_Phi",-9., "N_GenTopHad");
  vars.InitVars( "GenTopLep_B_Hadron_E",-9., "N_GenTopLep" );
  vars.InitVars( "GenTopHad_B_Hadron_E",-9., "N_GenTopHad");
  
  // for THW
  vars.InitVar( "GenW_NotFromTop_Pt",-9. );
  vars.InitVar( "GenW_NotFromTop_Eta",-9. );
  vars.InitVar( "GenW_NotFromTop_Phi",-9. );
  vars.InitVar( "GenW_NotFromTop_E",-9. );
  vars.InitVar( "N_GenW_NotFromTop_DecProds",-1,"I" );
  vars.InitVars( "GenW_NotFromTop_DecProd_Pt",-9., "N_GenW_NotFromTop_DecProds" );
  vars.InitVars( "GenW_NotFromTop_DecProd_Eta",-9., "N_GenW_NotFromTop_DecProds" );
  vars.InitVars( "GenW_NotFromTop_DecProd_Phi",-9., "N_GenW_NotFromTop_DecProds" );
  vars.InitVars( "GenW_NotFromTop_DecProd_E",-9., "N_GenW_NotFromTop_DecProds" );
  vars.InitVars( "GenW_NotFromTop_DecProd_PDGID",-999, "N_GenW_NotFromTop_DecProds" );
  
  // for THQ
  vars.InitVar( "GenForwardQuark_Pt",-9. );
  vars.InitVar( "GenForwardQuark_Eta",-9. );
  vars.InitVar( "GenForwardQuark_Phi",-9. );
  vars.InitVar( "GenForwardQuark_E",-9. );
  vars.InitVar( "GenForwardQuark_PDGID",-999 );


  // ttH variables
  vars.InitVar( "Gen_ttH_M", -9. );
  vars.InitVar( "Gen_ttH_Pt", -9. );

  // HT variables
  vars.InitVar( "Gen_Ht_ttH", -9. );
  vars.InitVar( "Gen_Ht_Jets", -9. );

   vars.InitVar("GenHiggsMassFromMatchedJets",-9.);	
   //vars.InitVar("GenZMassFromMatchedJets",-9.);	  // HT variables
  vars.InitVars("GenHadTopMassFromMatchedJets",-9.,"N_GenTopHad");
  vars.InitVars("GenHadWMassFromMatchedJets",-9.,"N_GenTopHad");

  initialized = true;
}


void MCMatchVarProcessor::Process(const InputCollections& input,VariableContainer& vars){
  
  if(!initialized) cerr << "tree processor not initialized" << endl;
  
  int iBB = 0;
  int iCC = 0;
  
  if(input.sampleType == SampleType::ttbb) iBB = 3;
  if(input.sampleType == SampleType::ttb) iBB = 1;
  if(input.sampleType == SampleType::tt2b) iBB = 2;
  if(input.sampleType == SampleType::ttcc) iCC = 1;
    
<<<<<<< HEAD
  if(input.sampleType == SampleType::ttbbb) iBB = 4; // add tt+bbb
  if(input.sampleType == SampleType::tt4b) iBB = 5; // add tt+4b
=======
  if(input.sampleType == SampleType::ttbbb) iBB = 4; // added by Wei
  if(input.sampleType == SampleType::tt4b) iBB = 5; // added by Wei
>>>>>>> 9a3ff44fd8e6118ec38a24fc8dd8a004e99b7d31
  
  vars.FillVar( "GenEvt_I_TTPlusCC",iCC );
  vars.FillVar( "GenEvt_I_TTPlusBB",iBB );
  if(input.genTopEvt.IsFilled()){
      vars.FillVar( "GenEvt_TTxId_FromProducer",input.genTopEvt.GetTTxIdFromProducer());
  }
  int nGoodTagsM=0;
  int nMisTagsM=0;
  for(auto j=input.selectedJets.begin(); j!=input.selectedJets.end(); j++){
      if (!(CSVHelper::PassesCSV(*j, "DeepJet", CSVHelper::CSVwp::Medium,input.era))) continue;
      if(abs(j->hadronFlavour())==5) nGoodTagsM++;
      if(abs(j->hadronFlavour())!=5) nMisTagsM++;
  }  
  vars.FillVar( "N_GoodTagsM",nGoodTagsM);
  vars.FillVar( "N_MisTagsM",nMisTagsM);


  std::vector<reco::GenParticle> tophad;
  std::vector<reco::GenParticle> whad;
  std::vector<reco::GenParticle> bhad;
  std::vector<reco::GenParticle> q1;
  std::vector<reco::GenParticle> q2;
  std::vector<reco::GenParticle> toplep;
  std::vector<reco::GenParticle> wlep;
  std::vector<reco::GenParticle> blep;
  std::vector<reco::GenParticle> lep;
  std::vector<reco::GenParticle> nu;
  std::vector<reco::GenJet> addBJet;
  std::vector<reco::GenJet> addCJet;
  std::vector<reco::GenJet> addLFJet;
  reco::GenParticle higgs1;
  reco::GenParticle higgs2;
  // for ttZ
  reco::GenParticle Z1;
  reco::GenParticle Z2;
  // for THW
  reco::GenParticle w_not_from_top;
  std::vector<reco::GenParticle> w_not_from_top_decay_products;
  // for THQ
  reco::GenParticle forward_quark;
  std::vector<reco::GenParticle> higgs1_bs;
  std::vector<reco::GenParticle> higgs2_bs;
  std::vector<reco::GenParticle> Z1_bs;
  std::vector<reco::GenParticle> Z2_bs;
  if(input.genTopEvt.IsFilled()){
    tophad=input.genTopEvt.GetAllTopHads();
    whad=input.genTopEvt.GetAllWhads();
    bhad=input.genTopEvt.GetAllTopHadDecayQuarks();
    q1=input.genTopEvt.GetAllWQuarks();
    q2=input.genTopEvt.GetAllWAntiQuarks();
    toplep=input.genTopEvt.GetAllTopLeps();
    wlep=input.genTopEvt.GetAllWleps();
    blep=input.genTopEvt.GetAllTopLepDecayQuarks();
    lep=input.genTopEvt.GetAllLeptons();
    nu=input.genTopEvt.GetAllNeutrinos();
    addBJet=input.genTopEvt.GetAdditionalBGenJets();
    addCJet=input.genTopEvt.GetAdditionalCGenJets();
    addLFJet=input.genTopEvt.GetAdditionalLightGenJets();
    higgs1=input.genTopEvt.GetHiggs1();
    higgs2=input.genTopEvt.GetHiggs2();
    higgs1_bs=input.genTopEvt.GetHiggs1DecayProducts();
    higgs2_bs=input.genTopEvt.GetHiggs2DecayProducts();
    Z1_bs=input.genTopEvt.GetZ1DecayProducts();
    Z2_bs=input.genTopEvt.GetZ2DecayProducts();
    // for ttZZ
    Z1 = input.genTopEvt.GetZ1();
    Z2 = input.genTopEvt.GetZ2();
    // for THW
    w_not_from_top = input.genTopEvt.GetWNotFromTop();
    w_not_from_top_decay_products = input.genTopEvt.GetWNotFromTopDecayProducts();
    // for THQ
    forward_quark = input.genTopEvt.GetForwardQuark();
  }

  reco::GenParticle b1;
  reco::GenParticle b2;

  reco::GenParticle b3;
  reco::GenParticle b4;

  reco::GenParticle Zb1;
  reco::GenParticle Zb2;
  reco::GenParticle Zb3;
  reco::GenParticle Zb4;

  reco::GenParticle ZHZb1;
  reco::GenParticle ZHZb2;
  reco::GenParticle ZHHb3;
  reco::GenParticle ZHHb4;
    
  reco::GenParticle decProd1;
  reco::GenParticle decProd2;

  //create a TLorentzVector for the ttH system
  math::XYZTLorentzVector ttH;
  double ttH_HT=0.;
  double Gen_Jets_HT=0.;

  //if(higgs_bs.size()>2)std:://cout<<"MORE THAN TWO HIGGS PRODUCTS"<<std::endl;
  bool dfirst=true;

  if(Z1_bs.size()==0 &&  Z2_bs.size()==0 && higgs1_bs.size()==2 &&  higgs2_bs.size()==2 && higgs1.pt() > higgs2.pt()){
      for(auto p =higgs1_bs.begin(); p!=higgs1_bs.end(); p++){
          if(p->pdgId()==5) b1=*p;
          if(p->pdgId()==-5) b2=*p;
          if(dfirst){
              decProd1=*p;
              dfirst=false;
          }
          else{
              decProd2=*p;
          }
      }
      for(auto p =higgs2_bs.begin(); p!=higgs2_bs.end(); p++){
          if(p->pdgId()==5) b3=*p;
          if(p->pdgId()==-5) b4=*p;
      }
  }else if (Z1_bs.size()==0 &&  Z2_bs.size()==0 && higgs1_bs.size()==2 &&  higgs2_bs.size()==2 && higgs1.pt() <= higgs2.pt()){
      for(auto p =higgs2_bs.begin(); p!=higgs2_bs.end(); p++){
          if(p->pdgId()==5) b1=*p;
          if(p->pdgId()==-5) b2=*p;
          if(dfirst){
              decProd1=*p;
              dfirst=false;
          }
          else{
              decProd2=*p;
          }
      }
      for(auto p =higgs1_bs.begin(); p!=higgs1_bs.end(); p++){
          if(p->pdgId()==5) b3=*p;
          if(p->pdgId()==-5) b4=*p;
      }
  }
  
  // fill Higgs decay products
  if(decProd1.pt()>0.){
    vars.FillVar("GenHiggs_DecProd1_Pt",decProd1.pt());
    vars.FillVar("GenHiggs_DecProd2_Pt",decProd2.pt());
    vars.FillVar("GenHiggs_DecProd1_Eta",decProd1.eta());
    vars.FillVar("GenHiggs_DecProd2_Eta",decProd2.eta());
    vars.FillVar("GenHiggs_DecProd1_E",decProd1.energy());
    vars.FillVar("GenHiggs_DecProd2_E",decProd2.energy());
    vars.FillVar("GenHiggs_DecProd1_PDGID",decProd1.pdgId());
    vars.FillVar("GenHiggs_DecProd2_PDGID",decProd2.pdgId());
  }
 
  // find ZZ decay products
  if(Z1_bs.size()==2 &&  Z2_bs.size()==2 && Z1.pt() > Z2.pt() && higgs1_bs.size()==0 &&  higgs2_bs.size()==0){
      for(auto p = Z1_bs.begin(); p!=Z1_bs.end(); p++) {
          if(p->pdgId()==5) Zb1=*p;
          if(p->pdgId()==-5) Zb2=*p;
      }
      for(auto p = Z2_bs.begin(); p!=Z2_bs.end(); p++) {
          if(p->pdgId()==5) Zb3=*p;
          if(p->pdgId()==-5) Zb4=*p;
      }
  }else if (Z1_bs.size()==2 &&  Z2_bs.size()==2 && Z1.pt() <= Z2.pt() && higgs1_bs.size()==0 &&  higgs2_bs.size()==0){
      for(auto p = Z2_bs.begin(); p!=Z2_bs.end(); p++) {
          if(p->pdgId()==5) Zb1=*p;
          if(p->pdgId()==-5) Zb2=*p;
      }
      for(auto p = Z1_bs.begin(); p!=Z1_bs.end(); p++) {
          if(p->pdgId()==5) Zb3=*p;
          if(p->pdgId()==-5) Zb4=*p;
      }
  }
  //    ttZH
  if(Z1_bs.size()==2 &&  Z2_bs.size()==0 && higgs1_bs.size()==2 &&  higgs2_bs.size()==0){
      for(auto p = Z1_bs.begin(); p!=Z1_bs.end(); p++) {
          if(p->pdgId()==5) ZHZb1=*p;
          if(p->pdgId()==-5) ZHZb2=*p;
      }
      for(auto p = higgs1_bs.begin(); p!=higgs1_bs.end(); p++) {
          if(p->pdgId()==5) ZHHb3=*p;
          if(p->pdgId()==-5) ZHHb4=*p;
      }
  }
  
  vars.FillVar( "N_GenTopLep", toplep.size());
  vars.FillVar( "N_GenTopHad", tophad.size());
  
  vector<math::XYZTLorentzVector> jetvecs = BoostedUtils::GetJetVecs(input.selectedJets);
  
  // fill leptonic Top system
  for(size_t i=0;i<toplep.size();i++){
    math::XYZTLorentzVector gen_top=toplep[i].p4();
    ttH+=gen_top;
    ttH_HT+=toplep[i].pt();
    //cout<<"\n\t>>>>>\tadded leptnic top\t<<<<<\n";
    //cout<<gen_top.pt()<<"__"<<gen_top.px()<<"__"<<gen_top.py()<<"__"<<gen_top.pz()<<"__mass:_"<<gen_top.mass()<<endl;
    //cout<<ttH.pt()<<"__"<<ttH.px()<<"__"<<ttH.py()<<"__"<<ttH.pz()<<"__mass:_"<<ttH.mass()<<endl;
    vars.FillVars( "GenTopLep_Pt",i,toplep[i].pt());
    vars.FillVars( "GenTopLep_Eta",i,toplep[i].eta());
    vars.FillVars( "GenTopLep_Phi",i,toplep[i].phi());
    vars.FillVars( "GenTopLep_E",i,toplep[i].energy());
    vars.FillVars( "GenTopLep_W_Pt",i,wlep[i].pt());
    vars.FillVars( "GenTopLep_B_Pt",i,blep[i].pt());
    vars.FillVars( "GenTopLep_Lep_Pt",i,lep[i].pt());
    vars.FillVars( "GenTopLep_Nu_Pt",i,nu[i].pt());
    vars.FillVars( "GenTopLep_W_Eta",i,wlep[i].eta());
    vars.FillVars( "GenTopLep_B_Eta",i,blep[i].eta());
    vars.FillVars( "GenTopLep_Lep_Eta",i,lep[i].eta());
    vars.FillVars( "GenTopLep_Nu_Eta",i,nu[i].eta());
    vars.FillVars( "GenTopLep_W_Phi",i,wlep[i].phi());
    vars.FillVars( "GenTopLep_B_Phi",i,blep[i].phi());
    vars.FillVars( "GenTopLep_Lep_Phi",i,lep[i].phi());
    vars.FillVars( "GenTopLep_Nu_Phi",i,nu[i].phi());
    vars.FillVars( "GenTopLep_W_E",i,wlep[i].energy());
    vars.FillVars( "GenTopLep_B_E",i,blep[i].energy());
    vars.FillVars( "GenTopLep_Lep_E",i,lep[i].energy());
    vars.FillVars( "GenTopLep_Nu_E",i,nu[i].energy());
    
    int idxblep = -1;
    double minDrTopLep = 999;
    for(std::vector<math::XYZTLorentzVector>::iterator itJetVec = jetvecs.begin() ; itJetVec != jetvecs.end(); ++itJetVec){
      if(BoostedUtils::DeltaR(*itJetVec,blep[i].p4())<minDrTopLep){
        idxblep = itJetVec-jetvecs.begin();
        minDrTopLep = BoostedUtils::DeltaR(*itJetVec,blep[i].p4());
      }
    }
    
    if(minDrTopLep<.25){
      vars.FillVars( "GenTopLep_B_Idx",i,idxblep);
    }
  }
  

  // fill hadronic top system
  for(size_t i=0;i<tophad.size();i++){
    math::XYZTLorentzVector gen_top=tophad[i].p4();
    ttH+=gen_top;
    ttH_HT+=tophad[i].pt();
    //cout<<"\n\t>>>>>\tadded hadronic top\t<<<<<\n";
    //cout<<gen_top.pt()<<"__"<<gen_top.px()<<"__"<<gen_top.py()<<"__"<<gen_top.pz()<<"__mass:_"<<gen_top.mass()<<endl;
    //cout<<ttH.pt()<<"__"<<ttH.px()<<"__"<<ttH.py()<<"__"<<ttH.pz()<<"__mass:_"<<ttH.mass()<<endl;
    vars.FillVars( "GenTopHad_Pt",i,tophad[i].pt());
    vars.FillVars( "GenTopHad_Eta",i,tophad[i].eta());
    vars.FillVars( "GenTopHad_Phi",i,tophad[i].phi());
    vars.FillVars( "GenTopHad_E",i,tophad[i].energy());
    vars.FillVars( "GenTopHad_W_Pt",i,whad[i].pt());
    vars.FillVars( "GenTopHad_B_Pt",i,bhad[i].pt());
    vars.FillVars( "GenTopHad_Q1_Pt",i,q1[i].pt());
    vars.FillVars( "GenTopHad_Q2_Pt",i,q2[i].pt());
    vars.FillVars( "GenTopHad_W_Eta",i,whad[i].eta());
    vars.FillVars( "GenTopHad_B_Eta",i,bhad[i].eta());
    vars.FillVars( "GenTopHad_Q1_Eta",i,q1[i].eta());
    vars.FillVars( "GenTopHad_Q2_Eta",i,q2[i].eta());
    vars.FillVars( "GenTopHad_W_Phi",i,whad[i].phi());
    vars.FillVars( "GenTopHad_B_Phi",i,bhad[i].phi());
    vars.FillVars( "GenTopHad_Q1_Phi",i,q1[i].phi());
    vars.FillVars( "GenTopHad_Q2_Phi",i,q2[i].phi());
    vars.FillVars( "GenTopHad_W_E",i,whad[i].energy());
    vars.FillVars( "GenTopHad_B_E",i,bhad[i].energy());
    vars.FillVars( "GenTopHad_Q1_E",i,q1[i].energy());
    vars.FillVars( "GenTopHad_Q2_E",i,q2[i].energy());
    int idxbhad=-1;
    int idxq1=-1;
    int idxq2=-1;
    double minDrTopHadB = 999;
    double minDrTopHadQ1 = 999;
    double minDrTopHadQ2 = 999;
    
    for(size_t j=0; j<jetvecs.size(); j++){
            if(BoostedUtils::DeltaR(jetvecs[j],bhad[i].p4())<minDrTopHadB){
        idxbhad = j;
        minDrTopHadB = BoostedUtils::DeltaR(jetvecs[j],bhad[i].p4());
      }
      if(BoostedUtils::DeltaR(jetvecs[j],q1[i].p4())<minDrTopHadQ1){
        idxq1 = j;
        minDrTopHadQ1 = BoostedUtils::DeltaR(jetvecs[j],q1[i].p4());
      }
      if(BoostedUtils::DeltaR(jetvecs[j],q2[i].p4())<minDrTopHadQ2){
        idxq2 = j;
        minDrTopHadQ2 = BoostedUtils::DeltaR(jetvecs[j],q2[i].p4());
      }
    }
    
    if(minDrTopHadB<.25){
      vars.FillVars( "GenTopHad_B_Idx",i,idxbhad);
    }
    if(minDrTopHadQ1<.25){
      vars.FillVars( "GenTopHad_Q1_Idx",i,idxq1);
    }
    if(minDrTopHadQ2<.25){
      vars.FillVars( "GenTopHad_Q2_Idx",i,idxq2);
    }

    // get mass of dijet Whad system if quark indices were found
    if(minDrTopHadQ1<.25 && minDrTopHadQ2<.25)
    {
        // get tri
        math::XYZTLorentzVector hadw_vec = jetvecs[idxq1]+jetvecs[idxq2];
        vars.FillVars("GenHadWMassFromMatchedJets",i,hadw_vec.M());
    }

    // get mass of trijet hadtop system if quark indices were found
    if( minDrTopHadB<.25 && minDrTopHadQ1<.25 && minDrTopHadQ2<.25)
    {
        // get tri
        math::XYZTLorentzVector hadtop_vec = jetvecs[idxbhad]+jetvecs[idxq1]+jetvecs[idxq2];
        vars.FillVars("GenHadTopMassFromMatchedJets",i,hadtop_vec.M());
    }
    
  }


  // fill higgs system
  if(Z1_bs.size()==0 &&  Z2_bs.size()==0 && higgs1_bs.size()==2 &&  higgs2_bs.size()==2 && higgs1.pt() > higgs2.pt() && higgs2.pt()>0.){
      vars.FillVar( "GenHiggs1_Pt",higgs1.pt());
      vars.FillVar( "GenHiggs1_Eta",higgs1.eta());
      vars.FillVar( "GenHiggs1_Phi",higgs1.phi());
      vars.FillVar( "GenHiggs1_E",higgs1.energy());
      vars.FillVar( "GenHiggs1_Y",higgs1.rapidity());
      vars.FillVar( "GenHiggs2_Pt",higgs2.pt());
      vars.FillVar( "GenHiggs2_Eta",higgs2.eta());
      vars.FillVar( "GenHiggs2_Phi",higgs2.phi());
      vars.FillVar( "GenHiggs2_E",higgs2.energy());
      vars.FillVar( "GenHiggs2_Y",higgs2.rapidity());
      math::XYZTLorentzVector gen_higgs1=higgs1.p4();
      ttH+=gen_higgs1;
      ttH_HT+=gen_higgs1.pt();
      //cout<<"\n\t>>>>>\tadded higgs\t<<<<<\n";
      //cout<<gen_higgs.pt()<<"__"<<gen_higgs.px()<<"__"<<gen_higgs.py()<<"__"<<gen_higgs.pz()<<"__mass:_"<<gen_higgs.mass()<<endl;
      //cout<<ttH.pt()<<"__"<<ttH.px()<<"__"<<ttH.py()<<"__"<<ttH.pz()<<"__mass:_"<<ttH.mass()<<endl;
  }else if (Z1_bs.size()==0 &&  Z2_bs.size()==0 && higgs1_bs.size()==2 &&  higgs2_bs.size()==2 && higgs1.pt()>0. && higgs1.pt() <= higgs2.pt()){
      vars.FillVar( "GenHiggs1_Pt",higgs2.pt());
      vars.FillVar( "GenHiggs1_Eta",higgs2.eta());
      vars.FillVar( "GenHiggs1_Phi",higgs2.phi());
      vars.FillVar( "GenHiggs1_E",higgs2.energy());
      vars.FillVar( "GenHiggs1_Y",higgs2.rapidity());
      vars.FillVar( "GenHiggs2_Pt",higgs1.pt());
      vars.FillVar( "GenHiggs2_Eta",higgs1.eta());
      vars.FillVar( "GenHiggs2_Phi",higgs1.phi());
      vars.FillVar( "GenHiggs2_E",higgs1.energy());
      vars.FillVar( "GenHiggs2_Y",higgs1.rapidity());
      math::XYZTLorentzVector gen_higgs2=higgs2.p4();
      ttH+=gen_higgs2;
      ttH_HT+=gen_higgs2.pt();
  }

  // build HT from Jets and leptons
  for(std::vector<reco::GenJet>::const_iterator itJet = input.genJets.begin() ; itJet != input.genJets.end(); ++itJet){
      Gen_Jets_HT += itJet->pt();
      //cout<<Gen_Jets_HT<<endl;
  }
  // for(std::vector<reco::GenParticle>::const_iterator itEle = input.customGenElectrons.begin(); itEle != input.customGenElectrons.end(); ++itEle){
  //     Gen_Jets_HT += itEle->pt();
  //     //cout<<Gen_Jets_HT<<endl;
  // }
  // for(std::vector<reco::GenParticle>::const_iterator itMu = input.customGenMuons.begin(); itMu != input.customGenMuons.end(); ++itMu){
  //     Gen_Jets_HT += itMu->pt();
  //     //cout<<Gen_Jets_HT<<endl;
  // }
  // for(std::vector<reco::GenParticle>::const_iterator itGamma = input.customGenPhotons.begin(); itGamma != input.customGenPhotons.end(); ++itGamma){
  //     Gen_Jets_HT += itGamma->pt();
  //     //cout<<Gen_Jets_HT<<endl;
  // }

    
  if(Z1_bs.size()==0 &&  Z2_bs.size()==0 && higgs1_bs.size()==2 &&  higgs2_bs.size()==2 && b2.pt()>0. && b4.pt() > 0){
      vars.FillVar("GenHiggs1_B1_Pt",b1.pt());
      vars.FillVar("GenHiggs1_B2_Pt",b2.pt());
      vars.FillVar("GenHiggs1_B1_Eta",b1.eta());
      vars.FillVar("GenHiggs1_B2_Eta",b2.eta());
      vars.FillVar("GenHiggs1_B1_Phi",b1.phi());
      vars.FillVar("GenHiggs1_B2_Phi",b2.phi());
      vars.FillVar("GenHiggs1_B1_E",b1.energy());
      vars.FillVar("GenHiggs1_B2_E",b2.energy());
      vars.FillVar("GenHiggs2_B3_Pt",b3.pt());
      vars.FillVar("GenHiggs2_B4_Pt",b4.pt());
      vars.FillVar("GenHiggs2_B3_Eta",b3.eta());
      vars.FillVar("GenHiggs2_B4_Eta",b4.eta());
      vars.FillVar("GenHiggs2_B3_Phi",b3.phi());
      vars.FillVar("GenHiggs2_B4_Phi",b4.phi());
      vars.FillVar("GenHiggs2_B3_E",b3.energy());
      vars.FillVar("GenHiggs2_B4_E",b4.energy());
      
      int idxb1=-1;
      int idxb2=-1;
      
      double minDrB1 = 999;
      double minDrB2 = 999;
      
      for(std::vector<math::XYZTLorentzVector>::iterator itJetVec = jetvecs.begin() ; itJetVec != jetvecs.end(); ++itJetVec){
          assert(itJetVec->pt()>0);
          assert(b1.pt()>0);
          assert(b2.pt()>0);
          if(BoostedUtils::DeltaR(*itJetVec,b1.p4())<minDrB1){
              idxb1 = itJetVec-jetvecs.begin();
              minDrB1 = BoostedUtils::DeltaR(*itJetVec,b1.p4());
          }
          if(BoostedUtils::DeltaR(*itJetVec,b2.p4())<minDrB2){
              idxb2 = itJetVec-jetvecs.begin();
              minDrB2 = BoostedUtils::DeltaR(*itJetVec,b2.p4());
          }
      }
      
      if(minDrB1<.25){
          vars.FillVar( "GenHiggs_B1_Idx",idxb1);
      }
      if(minDrB2<.25){
          vars.FillVar( "GenHiggs_B2_Idx",idxb2);
      }
      
      // get mass of dijet system of B indices were found
      if( minDrB1<.25 && minDrB2<.25 )
      {
          // get dijet
          math::XYZTLorentzVector higgs_vec = jetvecs[idxb1]+jetvecs[idxb2];
          vars.FillVar("GenHiggsMassFromMatchedJets", higgs_vec.M());
      }

  }

  // for THW
  if(w_not_from_top.pt()>0.){  
    vars.FillVar( "GenW_NotFromTop_Pt",w_not_from_top.pt());
    vars.FillVar( "GenW_NotFromTop_Eta",w_not_from_top.eta());
    vars.FillVar( "GenW_NotFromTop_Phi",w_not_from_top.phi());
    vars.FillVar( "GenW_NotFromTop_E",w_not_from_top.energy());
  }
  vars.FillVar( "N_GenW_NotFromTop_DecProds",w_not_from_top_decay_products.size() );
  for(size_t i=0;i<w_not_from_top_decay_products.size();i++){
    vars.FillVars("GenW_NotFromTop_DecProd_Pt",i,w_not_from_top_decay_products.at(i).pt() );
    vars.FillVars("GenW_NotFromTop_DecProd_Eta",i,w_not_from_top_decay_products.at(i).eta() );
    vars.FillVars("GenW_NotFromTop_DecProd_Phi",i,w_not_from_top_decay_products.at(i).phi() );
    vars.FillVars("GenW_NotFromTop_DecProd_E",i,w_not_from_top_decay_products.at(i).energy() );
    vars.FillVars("GenW_NotFromTop_DecProd_PDGID",i,w_not_from_top_decay_products.at(i).pdgId() );
  }

  // for THQ
  if(forward_quark.pt()>0.){
    vars.FillVar( "GenForwardQuark_Pt",forward_quark.pt());
    vars.FillVar( "GenForwardQuark_Eta",forward_quark.eta());
    vars.FillVar( "GenForwardQuark_Phi",forward_quark.phi());
    vars.FillVar( "GenForwardQuark_E",forward_quark.energy());
    vars.FillVar( "GenForwardQuark_PDGID",forward_quark.pdgId());
  }
    
  // fill ttZZ system
  if(Z1.pt() > Z2.pt() && Z2.pt() > 0){
      vars.FillVar( "GenZ1_Pt",Z1.pt());
      vars.FillVar( "GenZ1_Eta",Z1.eta());
      vars.FillVar( "GenZ1_Phi",Z1.phi());
      vars.FillVar( "GenZ1_E",Z1.energy());
      vars.FillVar( "GenZ1_Y",Z1.rapidity());
      vars.FillVar( "GenZ2_Pt",Z2.pt());
      vars.FillVar( "GenZ2_Eta",Z2.eta());
      vars.FillVar( "GenZ2_Phi",Z2.phi());
      vars.FillVar( "GenZ2_E",Z2.energy());
      vars.FillVar( "GenZ2_Y",Z2.rapidity());
  }else if (Z1.pt() <= Z2.pt() && Z1.pt() > 0){
      vars.FillVar( "GenZ1_Pt",Z2.pt());
      vars.FillVar( "GenZ1_Eta",Z2.eta());
      vars.FillVar( "GenZ1_Phi",Z2.phi());
      vars.FillVar( "GenZ1_E",Z2.energy());
      vars.FillVar( "GenZ1_Y",Z2.rapidity());
      vars.FillVar( "GenZ2_Pt",Z1.pt());
      vars.FillVar( "GenZ2_Eta",Z1.eta());
      vars.FillVar( "GenZ2_Phi",Z1.phi());
      vars.FillVar( "GenZ2_E",Z1.energy());
      vars.FillVar( "GenZ2_Y",Z1.rapidity());
  }
    
    // fill in ttZH
    
  if(Z1_bs.size()==2 &&  Z2_bs.size()==0 && higgs1_bs.size()==2 &&  higgs2_bs.size()==0 && Z1.pt() > 0 && higgs1.pt() > 0){
      vars.FillVar( "GenZH_Z_Pt",Z1.pt() );
      vars.FillVar( "GenZH_Z_Eta",Z1.eta());
      vars.FillVar( "GenZH_Z_Phi",Z1.phi() );
      vars.FillVar( "GenZH_Z_E",Z1.energy() );
      vars.FillVar( "GenZH_Z_Y",Z1.rapidity() );
      vars.FillVar( "GenZH_H_Pt",higgs1.pt() );
      vars.FillVar( "GenZH_H_Eta",higgs1.eta() );
      vars.FillVar( "GenZH_H_Phi",higgs1.phi() );
      vars.FillVar( "GenZH_H_E",higgs1.energy());
      vars.FillVar( "GenZH_H_Y",higgs1.rapidity() );
  }
    
  // ttZZ
  if(higgs1_bs.size()==0 &&  higgs2_bs.size()==0 && Z1_bs.size()==2 &&  Z2_bs.size()==2 && Zb1.pt()>0. && Zb3.pt() > 0){
      vars.FillVar("GenZ1_B1_Pt",Zb1.pt());
      vars.FillVar("GenZ1_B2_Pt",Zb2.pt());
      vars.FillVar("GenZ1_B1_Eta",Zb1.eta());
      vars.FillVar("GenZ1_B2_Eta",Zb2.eta());
      vars.FillVar("GenZ1_B1_Phi",Zb1.phi());
      vars.FillVar("GenZ1_B2_Phi",Zb2.phi());
      vars.FillVar("GenZ1_B1_E",Zb1.energy());
      vars.FillVar("GenZ1_B2_E",Zb2.energy());
      vars.FillVar("GenZ2_B3_Pt",Zb3.pt());
      vars.FillVar("GenZ2_B4_Pt",Zb4.pt());
      vars.FillVar("GenZ2_B3_Eta",Zb3.eta());
      vars.FillVar("GenZ2_B4_Eta",Zb4.eta());
      vars.FillVar("GenZ2_B3_Phi",Zb3.phi());
      vars.FillVar("GenZ2_B4_Phi",Zb4.phi());
      vars.FillVar("GenZ2_B3_E",Zb3.energy());
      vars.FillVar("GenZ2_B4_E",Zb4.energy());
  }
  // ttZH
  if(Z1_bs.size()==2 &&  Z2_bs.size()==0 && higgs1_bs.size()==2 &&  higgs2_bs.size()==0 && ZHZb1.pt() > 0 && ZHHb3.pt() > 0){
      vars.FillVar("GenZH_Z_B1_Pt",ZHZb1.pt());
      vars.FillVar("GenZH_Z_B2_Pt",ZHZb2.pt());
      vars.FillVar("GenZH_Z_B1_Eta",ZHZb1.eta());
      vars.FillVar("GenZH_Z_B2_Eta",ZHZb2.eta());
      vars.FillVar("GenZH_Z_B1_Phi",ZHZb1.phi());
      vars.FillVar("GenZH_Z_B2_Phi",ZHZb2.phi());
      vars.FillVar("GenZH_Z_B1_E",ZHZb1.energy());
      vars.FillVar("GenZH_Z_B2_E",ZHZb2.energy());
      vars.FillVar("GenZH_H_B3_Pt",ZHHb3.pt());
      vars.FillVar("GenZH_H_B4_Pt",ZHHb4.pt());
      vars.FillVar("GenZH_H_B3_Eta",ZHHb3.eta());
      vars.FillVar("GenZH_H_B4_Eta",ZHHb4.eta());
      vars.FillVar("GenZH_H_B3_Phi",ZHHb3.phi());
      vars.FillVar("GenZH_H_B4_Phi",ZHHb4.phi());
      vars.FillVar("GenZH_H_B3_E",ZHHb3.energy());
      vars.FillVar("GenZH_H_B4_E",ZHHb4.energy());
  }

  // fill semileptonic gen top event stuff
  if(input.genTopEvt.IsFilled()&&input.genTopEvt.TTxIsFilled()&&input.genTopEvt.IsSemiLepton()){
//    if(input.genTopEvt.IsFilled()&&input.genTopEvt.TTxIsFilled()){
    std::vector<reco::GenJet> bhad_genjet=input.genTopEvt.GetAllTopHadBGenJets();
    std::vector<reco::GenJet> blep_genjet=input.genTopEvt.GetAllTopLepBGenJets();
    std::vector<reco::GenJet> bbar_genjet=input.genTopEvt.GetHiggsBBarGenJet();
    std::vector<reco::GenJet> b_genjet=input.genTopEvt.GetHiggsBGenJet();

      std::vector<reco::GenParticle> bhad_hadron=input.genTopEvt.GetAllTopHadBHadrons();
      std::vector<reco::GenParticle> blep_hadron=input.genTopEvt.GetAllTopLepBHadrons();
      std::vector<reco::GenParticle> bbar_hadron=input.genTopEvt.GetHiggsBBarHadron();
      std::vector<reco::GenParticle> b_hadron=input.genTopEvt.GetHiggsBHadron();
      
      vars.FillVar( "N_GenHiggs_BBar", bbar_genjet.size());
      vars.FillVar( "N_GenHiggs_B", b_genjet.size());

      for(uint i=0;i<bbar_genjet.size();i++){
          if(bbar_genjet[i].pt()>1){
              vars.FillVars( "GenHiggs_BBar_GenJet_Pt",i,bbar_genjet[i].pt() );
              vars.FillVars( "GenHiggs_BBar_GenJet_Eta",i,bbar_genjet[i].eta() );
              vars.FillVars( "GenHiggs_BBar_GenJet_Phi",i,bbar_genjet[i].phi() );
              vars.FillVars( "GenHiggs_BBar_GenJet_E",i,bbar_genjet[i].energy() );
          }
      }
     for(uint i=0;i<b_genjet.size();i++){
              if(b_genjet[i].pt()>1){
              vars.FillVars( "GenHiggs_B_GenJet_Pt",i,b_genjet[i].pt() );
              vars.FillVars( "GenHiggs_B_GenJet_Eta",i,b_genjet[i].eta() );
              vars.FillVars( "GenHiggs_B_GenJet_Phi",i,b_genjet[i].phi() );
              vars.FillVars( "GenHiggs_B_GenJet_E",i,b_genjet[i].energy() );
              }
          }
      
      math::XYZTLorentzVector Higgs1;
      math::XYZTLorentzVector Higgs2;
      double MassDif1, MassDif2;
      if (bbar_genjet.size() == 2 && b_genjet.size() == 2){
          math::XYZTLorentzVector bbar1 = bbar_genjet[0].p4();
          math::XYZTLorentzVector bbar2 = bbar_genjet[1].p4();
          math::XYZTLorentzVector b1 = b_genjet[0].p4();
          math::XYZTLorentzVector b2 = b_genjet[1].p4();
          
          MassDif1 = abs((bbar1 + b1).M() - (bbar2 + b2).M());
          MassDif2 = abs((bbar1 + b2).M() - (bbar2 + b1).M());
          
          if (MassDif1 < MassDif2) {
              if ((bbar1 + b1).pt() > (bbar2 + b2).pt()){
              Higgs1 = bbar1 + b1;
              Higgs2 = bbar2 + b2;
              }else{
                  Higgs1 = bbar2 + b2;
                  Higgs2 = bbar1 + b1;
              }
              vars.FillVar( "GenHiggs1_B_GenJet_M",Higgs1.M() );
              vars.FillVar( "GenHiggs2_B_GenJet_M",Higgs2.M() );
          }else{
              if ((bbar1 + b2).pt() > (bbar2 + b1).pt()){
              Higgs1 = bbar1 + b2;
              Higgs2 = bbar2 + b1;
              }else{
                  Higgs1 = bbar2 + b1;
                  Higgs2 = bbar1 + b2;
              }
              vars.FillVar( "GenHiggs1_B_GenJet_M",Higgs1.M() );
              vars.FillVar( "GenHiggs2_B_GenJet_M",Higgs2.M() );
          }
      }else if (bbar_genjet.size() == 2 && b_genjet.size() == 1){
              math::XYZTLorentzVector bbar1 = bbar_genjet[0].p4();
              math::XYZTLorentzVector bbar2 = bbar_genjet[1].p4();
              math::XYZTLorentzVector b1 = b_genjet[0].p4();
              
              MassDif1 = abs((bbar1 + b1).M() - bbar2.M());
              MassDif2 = abs((bbar2 + b1).M() - bbar1.M());
              
              if (MassDif1 < MassDif2) {
                  if ((bbar1 + b1).pt() > bbar2.pt()){
                  Higgs1 = bbar1 + b1;
                  Higgs2 = bbar2;
                  }else{
                      Higgs1 = bbar2;
                      Higgs2 = bbar1 + b1;
                  }
                  vars.FillVar( "GenHiggs1_B_GenJet_M",Higgs1.M() );
                  vars.FillVar( "GenHiggs2_B_GenJet_M",Higgs2.M() );
              }else{
                  if ((bbar2 + b1).pt() > bbar1.pt()){
                  Higgs1 = bbar2 + b1;
                  Higgs2 = bbar1;
                  }else{
                      Higgs1 = bbar1;
                      Higgs2 = bbar2 + b1;
                  }
                  vars.FillVar( "GenHiggs1_B_GenJet_M",Higgs1.M() );
                  vars.FillVar( "GenHiggs2_B_GenJet_M",Higgs2.M() );
              }

      }else if (bbar_genjet.size() == 1 && b_genjet.size() == 2){
          math::XYZTLorentzVector bbar1 = bbar_genjet[0].p4();
          math::XYZTLorentzVector b1 = b_genjet[0].p4();
          math::XYZTLorentzVector b2 = b_genjet[1].p4();
          
          MassDif1 = abs((bbar1 + b1).M() - b2.M());
          MassDif2 = abs(b1.M() - (bbar1 + b2).M());
          
          if (MassDif1 < MassDif2) {
              if ((bbar1 + b1).pt() > b2.pt()){
              Higgs1 = bbar1 + b1;
              Higgs2 = b2;
              }else{
                  Higgs1 = b2;
                  Higgs2 = bbar1 + b1;
              }
              vars.FillVar( "GenHiggs1_B_GenJet_M",Higgs1.M() );
              vars.FillVar( "GenHiggs2_B_GenJet_M",Higgs2.M() );
          }else{
              if ((bbar1 + b2).pt() > b1.pt()){
              Higgs1 = bbar1 + b2;
              Higgs2 = b1;
              }else{
                  Higgs1 = b1;
                  Higgs2 = bbar1 + b2;
              }
              vars.FillVar( "GenHiggs1_B_GenJet_M",Higgs1.M() );
              vars.FillVar( "GenHiggs2_B_GenJet_M",Higgs2.M() );
          }

  }
        
      if (Higgs1.M() > 1 && Higgs2.M() > 1){
      vars.FillVar( "N_GenHiggs", 2);
      vars.FillVars( "GenHiggs_B_GenJet_M",0, Higgs1.M() );
      vars.FillVars( "GenHiggs_B_GenJet_M",1, Higgs2.M() );
      }
      
      
      vars.FillVar( "N_GenHiggs_BBar_Hadron", bbar_hadron.size());
      vars.FillVar( "N_GenHiggs_B_Hadron", b_hadron.size());

      for(uint i=0;i<bbar_hadron.size();i++){
          if(bbar_hadron[i].pt()>1){
              vars.FillVars( "GenHiggs_BBar_Hadron_Pt",i,bbar_hadron[i].pt() );
              vars.FillVars( "GenHiggs_BBar_Hadron_Eta",i,bbar_hadron[i].eta() );
              vars.FillVars( "GenHiggs_BBar_Hadron_Phi",i,bbar_hadron[i].phi() );
              vars.FillVars( "GenHiggs_BBar_Hadron_E",i,bbar_hadron[i].energy() );
          }
      }
     for(uint i=0;i<b_hadron.size();i++){
              if(b_hadron[i].pt()>1){
                  vars.FillVars( "GenHiggs_B_Hadron_Pt",i,b_hadron[i].pt() );
                  vars.FillVars( "GenHiggs_B_Hadron_Eta",i,b_hadron[i].eta() );
                  vars.FillVars( "GenHiggs_B_Hadron_Phi",i,b_hadron[i].phi() );
                  vars.FillVars( "GenHiggs_B_Hadron_E",i,b_hadron[i].energy() );
              }
          }
      
      math::XYZTLorentzVector Higgs1_Hadron;
      math::XYZTLorentzVector Higgs2_Hadron;
      double MassDif1_Hadron, MassDif2_Hadron;
      if (bbar_hadron.size() == 2 && b_hadron.size() == 2){
          math::XYZTLorentzVector bbar1 = bbar_hadron[0].p4();
          math::XYZTLorentzVector bbar2 = bbar_hadron[1].p4();
          math::XYZTLorentzVector b1 = b_hadron[0].p4();
          math::XYZTLorentzVector b2 = b_hadron[1].p4();
          
          MassDif1_Hadron = abs((bbar1 + b1).M() - (bbar2 + b2).M());
          MassDif2_Hadron = abs((bbar1 + b2).M() - (bbar2 + b1).M());
          
          if (MassDif1_Hadron < MassDif2_Hadron) {
              if ((bbar1 + b1).pt() > (bbar2 + b2).pt()){
              Higgs1_Hadron = bbar1 + b1;
              Higgs2_Hadron = bbar2 + b2;
              }else{
                  Higgs1_Hadron = bbar2 + b2;
                  Higgs2_Hadron = bbar1 + b1;
              }
              vars.FillVar( "GenHiggs1_B_Hadron_M",Higgs1_Hadron.M() );
              vars.FillVar( "GenHiggs2_B_Hadron_M",Higgs2_Hadron.M() );
          }else{
              if ((bbar1 + b2).pt() > (bbar2 + b1).pt()){
              Higgs1_Hadron = bbar1 + b2;
              Higgs2_Hadron = bbar2 + b1;
              }else{
                  Higgs1_Hadron = bbar2 + b1;
                  Higgs2_Hadron = bbar1 + b2;
              }
              vars.FillVar( "GenHiggs1_B_Hadron_M",Higgs1_Hadron.M() );
              vars.FillVar( "GenHiggs2_B_Hadron_M",Higgs2_Hadron.M() );
          }
      }
      
      if (Higgs1_Hadron.M() > 1 && Higgs2_Hadron.M() > 1){
      vars.FillVar( "N_GenHiggs_Hadron", 2);
      vars.FillVars( "GenHiggs_B_Hadron_M",0, Higgs1_Hadron.M() );
      vars.FillVars( "GenHiggs_B_Hadron_M",1, Higgs2_Hadron.M() );
      }


    for(uint i=0;i<bhad_genjet.size();i++){
      if(bhad_genjet[i].pt()>1){
              vars.FillVars( "GenTopHad_B_GenJet_Pt",i,bhad_genjet[i].pt() );
              vars.FillVars( "GenTopHad_B_GenJet_Eta",i,bhad_genjet[i].eta() );
              vars.FillVars( "GenTopHad_B_GenJet_Phi",i,bhad_genjet[i].phi());
              vars.FillVars( "GenTopHad_B_GenJet_E",i,bhad_genjet[i].energy());
      }
      if(bhad_hadron[i].pt()>1){
              vars.FillVars( "GenTopHad_B_Hadron_Pt",i,bhad_hadron[i].pt() );
              vars.FillVars( "GenTopHad_B_Hadron_Eta",i,bhad_hadron[i].eta() );
              vars.FillVars( "GenTopHad_B_Hadron_Phi",i,bhad_hadron[i].phi());
              vars.FillVars( "GenTopHad_B_Hadron_E",i,bhad_hadron[i].energy());
      }
          }
    
    for(uint i=0;i<blep_genjet.size();i++){
      if(blep_genjet[i].pt()>1){
              vars.FillVars( "GenTopLep_B_GenJet_Pt",i,blep_genjet[i].pt() );
              vars.FillVars( "GenTopLep_B_GenJet_Eta",i,blep_genjet[i].eta());
              vars.FillVars( "GenTopLep_B_GenJet_Phi",i,blep_genjet[i].phi());
              vars.FillVars( "GenTopLep_B_GenJet_E",i,blep_genjet[i].energy());
      }
      if(blep_hadron[i].pt()>1){
              vars.FillVars( "GenTopLep_B_Hadron_Pt",i,blep_hadron[i].pt() );
              vars.FillVars( "GenTopLep_B_Hadron_Eta",i,blep_hadron[i].eta());
              vars.FillVars( "GenTopLep_B_Hadron_Phi",i,blep_hadron[i].phi());
              vars.FillVars( "GenTopLep_B_Hadron_E",i,blep_hadron[i].energy());
      }
    }
  }
  //fill m_ttH 
  vars.FillVar( "Gen_ttH_M",ttH.mass() );
  vars.FillVar( "Gen_ttH_Pt",ttH.pt() );

  //fill HT vars
  vars.FillVar( "Gen_Ht_ttH", ttH_HT );
  vars.FillVar( "Gen_Ht_Jets", Gen_Jets_HT );
}
