#ifndef MONOJETSELECTION_HPP
#define MONOJETSELECTION_HPP

#include <vector>

#include "BoostedTTH/BoostedAnalyzer/interface/Selection.hpp"

class MonoTopSelection : public Selection {
   public:
    MonoTopSelection(const edm::ParameterSet& iConfig);
    MonoTopSelection(double pt_min_, double eta_max_, double chf_min_, double nhf_max_, double min_MET_, double max_MET_, double deltaR_MET_AK15Jet_, double min_Recoil_);
    ~MonoTopSelection();
    void InitCutflow(Cutflow& cutflow);
    bool IsSelected(const InputCollections& input, Cutflow& cutflow);

   private:
    double pt_min;
    double eta_max;
    double charged_hadron_fraction_min;
    double neutral_hadron_fraction_max;
    double minMET;
    double maxMET;
    double deltaR_MET_AK15Jet;
    double minRecoil;
};

#endif