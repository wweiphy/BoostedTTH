#ifndef JABDTTHHPROCESSOR_HPP
#define JABDTTHHPROCESSOR_HPP
#include "BoostedTTH/BoostedAnalyzer/interface/JABDTBaseProcessor.hpp"
#include "BoostedTTH/BoostedAnalyzer/interface/TreeProcessor.hpp"
#include "BoostedTTH/BoostedAnalyzer/interface/BoostedUtils.hpp"
#include "TTH/CommonClassifier/interface/thhHypothesisCombinatorics.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"

class JABDTthhProcessor: public JABDTBaseProcessor{
    public:
      JABDTthhProcessor(const edm::ParameterSet& iConfig);
      ~JABDTthhProcessor();
    private:
};

#endif

