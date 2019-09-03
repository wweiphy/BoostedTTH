#include "BoostedTTH/BoostedAnalyzer/interface/JetVarProcessor.hpp"

using namespace std;

JetVarProcessor::JetVarProcessor() {}
JetVarProcessor::~JetVarProcessor() {}

void JetVarProcessor::Init(const InputCollections& input, VariableContainer& vars)
{
    // load dataEra
    era = input.era;

    vars.InitVar("N_AK8Jets", "I");
    vars.InitVars("AK8Jet_Pt", "N_AK8Jets");
    vars.InitVars("AK8Jet_Eta", "N_AK8Jets");
    vars.InitVars("AK8Jet_Phi", "N_AK8Jets");
    vars.InitVars("AK8Jet_E", "N_AK8Jets");
    vars.InitVars("AK8Jet_M", "N_AK8Jets");
    vars.InitVars("AK8Jet_Njettiness_tau1", "N_AK8Jets");
    vars.InitVars("AK8Jet_Njettiness_tau2", "N_AK8Jets");
    vars.InitVars("AK8Jet_Njettiness_tau3", "N_AK8Jets");
    vars.InitVars("AK8Jet_Njettiness_tau4", "N_AK8Jets");
    vars.InitVars("AK8Jet_PuppiSoftDropMass", "N_AK8Jets");
    vars.InitVars("AK8Jet_DeepAK8_TvsQCD", "N_AK8Jets");
    vars.InitVars("AK8Jet_DeepAK8_probTbcq", "N_AK8Jets");
    vars.InitVars("AK8Jet_DeepAK8_probTbqq", "N_AK8Jets");
    vars.InitVars("AK8Jet_DeepAK8_probTbc", "N_AK8Jets");
    vars.InitVars("AK8Jet_DeepAK8_probTbq", "N_AK8Jets");

    vars.InitVars("AK8Jet_N_SoftDropSubjets", "N_AK8Jets");

    vars.InitVars("AK8Jet_SoftDropJet1_Pt", "N_AK8Jets");
    vars.InitVars("AK8Jet_SoftDropJet1_Eta", "N_AK8Jets");
    vars.InitVars("AK8Jet_SoftDropJet1_Phi", "N_AK8Jets");
    vars.InitVars("AK8Jet_SoftDropJet1_E", "N_AK8Jets");
    vars.InitVars("AK8Jet_SoftDropJet1_M", "N_AK8Jets");
    vars.InitVars("AK8Jet_SoftDropJet1_DeepJetCSV", "N_AK8Jets");

    vars.InitVars("AK8Jet_SoftDropJet2_Pt", "N_AK8Jets");
    vars.InitVars("AK8Jet_SoftDropJet2_Eta", "N_AK8Jets");
    vars.InitVars("AK8Jet_SoftDropJet2_Phi", "N_AK8Jets");
    vars.InitVars("AK8Jet_SoftDropJet2_E", "N_AK8Jets");
    vars.InitVars("AK8Jet_SoftDropJet2_M", "N_AK8Jets");
    vars.InitVars("AK8Jet_SoftDropJet2_DeepJetCSV", "N_AK8Jets");

    vars.InitVars("AK8Jet_SoftDropJet3_Pt", "N_AK8Jets");
    vars.InitVars("AK8Jet_SoftDropJet3_Eta", "N_AK8Jets");
    vars.InitVars("AK8Jet_SoftDropJet3_Phi", "N_AK8Jets");
    vars.InitVars("AK8Jet_SoftDropJet3_E", "N_AK8Jets");
    vars.InitVars("AK8Jet_SoftDropJet3_M", "N_AK8Jets");
    vars.InitVars("AK8Jet_SoftDropJet3_DeepJetCSV", "N_AK8Jets");

    vars.InitVar("N_AK8Jets_x_N_Jets", "I");
    vars.InitVar("N_AK8Jets_x_N_JetsTagged", "I");
    vars.InitVars("DeltaR_AK8Jet_AK4Jet", "N_AK8Jets_x_N_Jets");
    vars.InitVars("DeltaR_AK8Jet_AK4JetTagged", "N_AK8Jets_x_N_JetsTagged");

    vars.InitVar("N_AK15Jets", "I");
    vars.InitVars("AK15Jet_Pt", "N_AK15Jets");
    vars.InitVars("AK15Jet_Eta", "N_AK15Jets");
    vars.InitVars("AK15Jet_Phi", "N_AK15Jets");
    vars.InitVars("AK15Jet_E", "N_AK15Jets");
    vars.InitVars("AK15Jet_M", "N_AK15Jets");
    vars.InitVars("AK15Jet_Njettiness_tau1", "N_AK15Jets");
    vars.InitVars("AK15Jet_Njettiness_tau2", "N_AK15Jets");
    vars.InitVars("AK15Jet_Njettiness_tau3", "N_AK15Jets");
    vars.InitVars("AK15Jet_Njettiness_tau4", "N_AK15Jets");
    vars.InitVars("AK15Jet_PuppiSoftDropMass", "N_AK15Jets");
    vars.InitVars("AK15Jet_DeepAK15_TvsQCD", "N_AK15Jets");
    vars.InitVars("AK15Jet_DeepAK15_probTbcq", "N_AK15Jets");
    vars.InitVars("AK15Jet_DeepAK15_probTbqq", "N_AK15Jets");
    vars.InitVars("AK15Jet_DeepAK15_probTbc", "N_AK15Jets");
    vars.InitVars("AK15Jet_DeepAK15_probTbq", "N_AK15Jets");

    vars.InitVars("AK15Jet_N_SoftDropSubjets", "N_AK15Jets");

    vars.InitVars("AK15Jet_SoftDropJet1_Pt", "N_AK15Jets");
    vars.InitVars("AK15Jet_SoftDropJet1_Eta", "N_AK15Jets");
    vars.InitVars("AK15Jet_SoftDropJet1_Phi", "N_AK15Jets");
    vars.InitVars("AK15Jet_SoftDropJet1_E", "N_AK15Jets");
    vars.InitVars("AK15Jet_SoftDropJet1_M", "N_AK15Jets");
    vars.InitVars("AK15Jet_SoftDropJet1_DeepJetCSV", "N_AK15Jets");

    vars.InitVars("AK15Jet_SoftDropJet2_Pt", "N_AK15Jets");
    vars.InitVars("AK15Jet_SoftDropJet2_Eta", "N_AK15Jets");
    vars.InitVars("AK15Jet_SoftDropJet2_Phi", "N_AK15Jets");
    vars.InitVars("AK15Jet_SoftDropJet2_E", "N_AK15Jets");
    vars.InitVars("AK15Jet_SoftDropJet2_M", "N_AK15Jets");
    vars.InitVars("AK15Jet_SoftDropJet2_DeepJetCSV", "N_AK15Jets");

    vars.InitVars("AK15Jet_SoftDropJet3_Pt", "N_AK15Jets");
    vars.InitVars("AK15Jet_SoftDropJet3_Eta", "N_AK15Jets");
    vars.InitVars("AK15Jet_SoftDropJet3_Phi", "N_AK15Jets");
    vars.InitVars("AK15Jet_SoftDropJet3_E", "N_AK15Jets");
    vars.InitVars("AK15Jet_SoftDropJet3_M", "N_AK15Jets");
    vars.InitVars("AK15Jet_SoftDropJet3_DeepJetCSV", "N_AK15Jets");

    vars.InitVar("N_AK15Jets_x_N_Jets", "I");
    vars.InitVar("N_AK15Jets_x_N_JetsTagged", "I");
    vars.InitVar("N_AK4JetsTagged_outside_AK15Jets", "I");
    vars.InitVars("DeltaR_AK15Jet_AK4Jet", "N_AK15Jets_x_N_Jets");
    vars.InitVars("DeltaR_AK15Jet_AK4JetTagged", "N_AK15Jets_x_N_JetsTagged");

    initialized = true;
}

void JetVarProcessor::Process(const InputCollections& input, VariableContainer& vars)
{
    if (!initialized) cerr << "JetVarProcessor not initialized" << endl;

    const auto& ak4jets = input.selectedJets;

    std::vector< pat::Jet > ak4jets_tagged;
    for (const auto& ak4jet : ak4jets) {
        if (CSVHelper::PassesCSV(ak4jet, "DeepJet", CSVHelper::CSVwp::Medium, era)) ak4jets_tagged.push_back(ak4jet);
    }

    const auto& ak8jets = input.selectedJetsAK8;

    vars.FillVar("N_AK8Jets", ak8jets.size());
    vars.FillVar("N_AK8Jets_x_N_Jets", ak8jets.size() * ak4jets.size());
    vars.FillVar("N_AK8Jets_x_N_JetsTagged", ak8jets.size() * ak4jets_tagged.size());
    for (size_t i = 0; i < ak8jets.size(); i++) {
        const auto& ak8jet = ak8jets.at(i);
        vars.FillVars("AK8Jet_Pt", i, ak8jet.pt());
        vars.FillVars("AK8Jet_Eta", i, ak8jet.eta());
        vars.FillVars("AK8Jet_Phi", i, ak8jet.phi());
        vars.FillVars("AK8Jet_E", i, ak8jet.energy());
        vars.FillVars("AK8Jet_M", i, ak8jet.mass());
        if (ak8jet.hasUserFloat("NjettinessAK8Puppi:tau1")) { vars.FillVars("AK8Jet_Njettiness_tau1", i, ak8jet.userFloat("NjettinessAK8Puppi:tau1")); }
        if (ak8jet.hasUserFloat("NjettinessAK8Puppi:tau2")) { vars.FillVars("AK8Jet_Njettiness_tau2", i, ak8jet.userFloat("NjettinessAK8Puppi:tau2")); }
        if (ak8jet.hasUserFloat("NjettinessAK8Puppi:tau3")) { vars.FillVars("AK8Jet_Njettiness_tau3", i, ak8jet.userFloat("NjettinessAK8Puppi:tau3")); }
        if (ak8jet.hasUserFloat("NjettinessAK8Puppi:tau4")) { vars.FillVars("AK8Jet_Njettiness_tau4", i, ak8jet.userFloat("NjettinessAK8Puppi:tau4")); }
        if (ak8jet.hasUserFloat("ak8PFJetsPuppiSoftDropMass")) { vars.FillVars("AK8Jet_PuppiSoftDropMass", i, ak8jet.userFloat("ak8PFJetsPuppiSoftDropMass")); }
        vars.FillVars("AK8Jet_DeepAK8_TvsQCD", i, ak8jet.bDiscriminator("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:TvsQCD"));
        vars.FillVars("AK8Jet_DeepAK8_probTbcq", i, ak8jet.bDiscriminator("pfMassDecorrelatedDeepBoostedJetTags:probTbcq"));
        vars.FillVars("AK8Jet_DeepAK8_probTbqq", i, ak8jet.bDiscriminator("pfMassDecorrelatedDeepBoostedJetTags:probTbqq"));
        vars.FillVars("AK8Jet_DeepAK8_probTbc", i, ak8jet.bDiscriminator("pfMassDecorrelatedDeepBoostedJetTags:probTbc"));
        vars.FillVars("AK8Jet_DeepAK8_probTbq", i, ak8jet.bDiscriminator("pfMassDecorrelatedDeepBoostedJetTags:probTbq"));

        const auto& ak8jet_subjets = ak8jet.subjets("SoftDropWithBtagInfo");

        vars.FillVars("AK8Jet_N_SoftDropSubjets", i, ak8jet_subjets.size());

        for (size_t j = 0; j < ak8jet_subjets.size() && j < 3; j++) {
            const auto& ak8jet_subjet = *ak8jet_subjets.at(j);
            vars.FillVars("AK8Jet_SoftDropJet" + std::to_string(j + 1) + "_Pt", i, ak8jet_subjet.pt());
            vars.FillVars("AK8Jet_SoftDropJet" + std::to_string(j + 1) + "_Eta", i, ak8jet_subjet.eta());
            vars.FillVars("AK8Jet_SoftDropJet" + std::to_string(j + 1) + "_Phi", i, ak8jet_subjet.phi());
            vars.FillVars("AK8Jet_SoftDropJet" + std::to_string(j + 1) + "_E", i, ak8jet_subjet.energy());
            vars.FillVars("AK8Jet_SoftDropJet" + std::to_string(j + 1) + "_M", i, ak8jet_subjet.mass());
            vars.FillVars("AK8Jet_SoftDropJet" + std::to_string(j + 1) + "_DeepJetCSV", i, CSVHelper::GetJetCSV_DNN(ak8jet_subjet, "DeepJet"));
        }

        for (size_t k = 0; k < ak4jets.size(); k++) {
            const auto& ak4jet = ak4jets.at(k);
            vars.FillVars("DeltaR_AK8Jet_AK4Jet", i * ak4jets.size() + k, BoostedUtils::DeltaR(ak8jet.p4(), ak4jet.p4()));
        }

        for (size_t k = 0; k < ak4jets_tagged.size(); k++) {
            const auto& ak4jet_tagged = ak4jets_tagged.at(k);
            vars.FillVars("DeltaR_AK8Jet_AK4JetTagged", i * ak4jets_tagged.size() + k, BoostedUtils::DeltaR(ak8jet.p4(), ak4jet_tagged.p4()));
        }
    }

    int n_AK4JetsTagged_outside_AK15Jets = 0;

    const auto& ak15jets = input.selectedJetsAK15;

    vars.FillVar("N_AK15Jets", ak15jets.size());
    vars.FillVar("N_AK15Jets_x_N_Jets", ak15jets.size() * ak4jets.size());
    vars.FillVar("N_AK15Jets_x_N_JetsTagged", ak15jets.size() * ak4jets_tagged.size());
    for (size_t i = 0; i < ak15jets.size(); i++) {
        const auto& ak15jet = ak15jets.at(i);
        vars.FillVars("AK15Jet_Pt", i, ak15jet.pt());
        vars.FillVars("AK15Jet_Eta", i, ak15jet.eta());
        vars.FillVars("AK15Jet_Phi", i, ak15jet.phi());
        vars.FillVars("AK15Jet_E", i, ak15jet.energy());
        vars.FillVars("AK15Jet_M", i, ak15jet.mass());
        if (ak15jet.hasUserFloat("NjettinessAK15Puppi:tau1")) { vars.FillVars("AK15Jet_Njettiness_tau1", i, ak15jet.userFloat("NjettinessAK15Puppi:tau1")); }
        if (ak15jet.hasUserFloat("NjettinessAK15Puppi:tau2")) { vars.FillVars("AK15Jet_Njettiness_tau2", i, ak15jet.userFloat("NjettinessAK15Puppi:tau2")); }
        if (ak15jet.hasUserFloat("NjettinessAK15Puppi:tau3")) { vars.FillVars("AK15Jet_Njettiness_tau3", i, ak15jet.userFloat("NjettinessAK15Puppi:tau3")); }
        if (ak15jet.hasUserFloat("NjettinessAK15Puppi:tau4")) { vars.FillVars("AK15Jet_Njettiness_tau4", i, ak15jet.userFloat("NjettinessAK15Puppi:tau4")); }
        if (ak15jet.hasUserFloat("ak15PFJetsPuppiSoftDropMass")) {
            vars.FillVars("AK15Jet_PuppiSoftDropMass", i, ak15jet.userFloat("ak15PFJetsPuppiSoftDropMass"));
        }
        vars.FillVars("AK15Jet_DeepAK15_TvsQCD", i, ak15jet.bDiscriminator("pfMassDecorrelatedDeepBoostedDiscriminatorsJetTags:TvsQCD"));
        vars.FillVars("AK15Jet_DeepAK15_probTbcq", i, ak15jet.bDiscriminator("pfMassDecorrelatedDeepBoostedJetTags:probTbcq"));
        vars.FillVars("AK15Jet_DeepAK15_probTbqq", i, ak15jet.bDiscriminator("pfMassDecorrelatedDeepBoostedJetTags:probTbqq"));
        vars.FillVars("AK15Jet_DeepAK15_probTbc", i, ak15jet.bDiscriminator("pfMassDecorrelatedDeepBoostedJetTags:probTbc"));
        vars.FillVars("AK15Jet_DeepAK15_probTbq", i, ak15jet.bDiscriminator("pfMassDecorrelatedDeepBoostedJetTags:probTbq"));

        const auto& ak15jet_subjets = ak15jet.subjets("SoftDropWithBtagInfo");

        vars.FillVars("AK15Jet_N_SoftDropSubjets", i, ak15jet_subjets.size());

        for (size_t j = 0; j < ak15jet_subjets.size() && j < 3; j++) {
            const auto& ak15jet_subjet = *ak15jet_subjets.at(j);
            vars.FillVars("AK15Jet_SoftDropJet" + std::to_string(j + 1) + "_Pt", i, ak15jet_subjet.pt());
            vars.FillVars("AK15Jet_SoftDropJet" + std::to_string(j + 1) + "_Eta", i, ak15jet_subjet.eta());
            vars.FillVars("AK15Jet_SoftDropJet" + std::to_string(j + 1) + "_Phi", i, ak15jet_subjet.phi());
            vars.FillVars("AK15Jet_SoftDropJet" + std::to_string(j + 1) + "_E", i, ak15jet_subjet.energy());
            vars.FillVars("AK15Jet_SoftDropJet" + std::to_string(j + 1) + "_M", i, ak15jet_subjet.mass());
            vars.FillVars("AK15Jet_SoftDropJet" + std::to_string(j + 1) + "_DeepJetCSV", i, CSVHelper::GetJetCSV_DNN(ak15jet_subjet, "DeepJet"));
        }

        for (size_t k = 0; k < ak4jets.size(); k++) {
            const auto& ak4jet = ak4jets.at(k);
            vars.FillVars("DeltaR_AK15Jet_AK4Jet", i * ak4jets.size() + k, BoostedUtils::DeltaR(ak15jet.p4(), ak4jet.p4()));
        }

        for (size_t k = 0; k < ak4jets_tagged.size(); k++) {
            const auto& ak4jet_tagged            = ak4jets_tagged.at(k);
            const auto  dR_ak15jet_ak4jet_tagged = BoostedUtils::DeltaR(ak15jet.p4(), ak4jet_tagged.p4());
            vars.FillVars("DeltaR_AK15Jet_AK4JetTagged", i * ak4jets_tagged.size() + k, dR_ak15jet_ak4jet_tagged);
            if (dR_ak15jet_ak4jet_tagged > 1.5) n_AK4JetsTagged_outside_AK15Jets += 1;
        }
    }
    vars.FillVar("N_AK4JetsTagged_outside_AK15Jets", n_AK4JetsTagged_outside_AK15Jets);
}
