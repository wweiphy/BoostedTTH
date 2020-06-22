#ifndef BOOSTEDTTH_BOOSTEDANALYZER_JETVARPROCESSOR_HPP
#define BOOSTEDTTH_BOOSTEDANALYZER_JETVARPROCESSOR_HPP

#include "BoostedTTH/BoostedAnalyzer/interface/TreeProcessor.hpp"
#include "BoostedTTH/BoostedAnalyzer/interface/BoostedUtils.hpp"
#include "MiniAOD/MiniAODHelper/interface/CSVHelper.h"

class JetVarProcessor : public TreeProcessor {
   public:
    JetVarProcessor();
    ~JetVarProcessor();

    void Init(const InputCollections& input, VariableContainer& var);
    void Process(const InputCollections& input, VariableContainer& var);

   private:
    std::string era;
    
    // fat jet matching
    std::vector< reco::GenParticle > LightQuarksFromWPlus;
    std::vector< reco::GenParticle > LightQuarksFromWMinus;
    std::vector< reco::GenParticle > CQuarksFromWPlus;
    std::vector< reco::GenParticle > CQuarksFromWMinus;
    std::vector< reco::GenParticle > BQuarksFromTop;
    std::vector< reco::GenParticle > BQuarksFromAntiTop;
    
    void RemoveParticlesOutsideOfJet(const pat::Jet& jet, float dR = 1.5);
    
    bool tbqqmatch();
    bool tbcqmatch();
    bool tqqmatch();
    bool tcqmatch();
    bool tbqmatch();
    bool tbcmatch();
};

#endif
