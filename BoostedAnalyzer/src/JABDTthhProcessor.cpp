#include "BoostedTTH/BoostedAnalyzer/interface/JABDTthhProcessor.hpp"
using namespace std;

JABDTthhProcessor::JABDTthhProcessor(const edm::ParameterSet& iConfig)
{
  if( iConfig.existsAs<edm::ParameterSet>("JetAssignmentOptions",true) ){
      const edm::ParameterSet jaoptions = iConfig.getParameter<edm::ParameterSet>("JetAssignmentOptions");
      //load input variables
      std::string bdt_input_vars = loadVariables(jaoptions, "tHH_varlist"); // JABDTBaseProcessor.hpp/cpp
//      https://github.com/wweiphy/BoostedTTH/blob/Legacy_2016_2017_2018_Devel/BoostedAnalyzer/data/bdtweights/2017/even_ttH/variables.csv
//      Given in JetAssignment_cff.py
      
      //load weightpath to even JA BDT
//      https://github.com/wweiphy/BoostedTTH/blob/Legacy_2016_2017_2018_Devel/BoostedAnalyzer/data/bdtweights/2017/even_ttH/JAreco_expert_BDT.weights.xml
      std::string weightpath = loadWeightPath(jaoptions, "tHH_even_weightpath");
      if(weightpath != ""){
        pointerToEvenHypothesisCombinatorics.reset(new thhHypothesisCombinatorics(weightpath, bdt_input_vars));
      }
      else{
        std::cerr << "ERROR: unable to load 'tHH_even_weightpath'";
        pointerToEvenHypothesisCombinatorics.reset(nullptr);
      }

      weightpath = loadWeightPath(jaoptions, "tHH_odd_weightpath");
      if(weightpath != ""){
        pointerToOddHypothesisCombinatorics.reset(new thhHypothesisCombinatorics(weightpath, bdt_input_vars));
      }
      else{
        std::cerr << "ERROR: unable to load 'tHH_odd_weightpath'";
        pointerToOddHypothesisCombinatorics.reset(nullptr);
      }
      
      // std::cout << "TYPE: " << typeid(pointerToHypothesisCombinatorics).name << std::endl;
      if( iConfig.existsAs<std::string>("tHH_prefix",true) ) hypothesis = iConfig.getParameter<std::string>("tHH_prefix");
      else hypothesis = "tHH";
  }
  else{
    std::cerr << "ERROR: Could not find JetAssignmentOptions in global config! ";
    std::cerr << "Unable to find best permutation for tHH hypothesis!\n";
    pointerToEvenHypothesisCombinatorics.reset(nullptr);
    pointerToOddHypothesisCombinatorics.reset(nullptr);
    hypothesis = "NONE";
  }
}

JABDTthhProcessor::~JABDTthhProcessor(){

}

