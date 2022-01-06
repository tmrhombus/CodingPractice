
#include <iostream>   // for IO
#include <cmath>      // for pow
#include <vector>     // for vectors

std::vector<float> incrementinterest( int steps, int groups, 
                         float growthrate, float initbalance, 
                         float jeffsnetcut, float jeffspercent ){

 std::cout<<"Start of incrementinterest(...)\n";
 std::cout<<" steps: "<<steps<<"\n";
 std::cout<<" groups: "<<groups<<"\n";
 std::cout<<" growthrate: "<<growthrate<<"\n";
 std::cout<<" initbalance: "<<initbalance<<"\n";
 std::cout<<" jeffsnetcut: "<<jeffsnetcut<<"\n";
 std::cout<<" jeffspercent: "<<jeffspercent<<"\n";

 if( groups <= 0 ){
  std::vector<float>  outputs;
  //outputs.push_back( initbalance  ); 
  outputs.push_back( jeffsnetcut ); 
  outputs.push_back( initbalance ); 
  return outputs;

 }

 float compoundbalance = initbalance * pow( growthrate, steps );
 float compoundprofit  = compoundbalance - initbalance;

 float jeffscut     = compoundprofit * jeffspercent; 
 float finalbalance = compoundbalance - jeffscut;
 jeffsnetcut += jeffscut; 
 
 std::cout<<" compundbalance: "<<compoundbalance<<"\n";
 std::cout<<" jeffscut:       "<<jeffscut<<"\n";
 std::cout<<" jeffsnetcut:    "<<jeffsnetcut<<"\n";
 std::cout<<" finalbalance:   "<<finalbalance<<"\n";

 std::vector<float>  outputs;
 outputs = incrementinterest( steps, groups-1, 
                              growthrate, finalbalance,
                              jeffsnetcut, jeffspercent );
// //outputs.push_back( initbalance  ); 
// outputs.push_back( jeffscut     ); 
// outputs.push_back( finalbalance ); 

 return outputs ;

}


int main(){

 float initialbalance = 2000;
 int   dayspergroup = 60;
 int   groups = 2; 
 float rate = 1.02;
 float jeffspercent = 0.05;

 std::vector<float> outputs = incrementinterest( dayspergroup, groups, 
   rate, initialbalance, 0, jeffspercent );

 float jeffscut = outputs[0];
 float finalbalance = outputs[1];

 std::vector<float> nojoutputs = incrementinterest( dayspergroup*groups, 1,
   rate, initialbalance, 0, 0.0 );

 float nojjeffscut = nojoutputs[0];
 float nojfinalbalance = nojoutputs[1];

 //  // print all elements
 //  std::cout << "vector elements are: ";
 //  for (int i = 0; i < outputs.size(); ++i) {
 //      std::cout << outputs[i] << ' ';
 //  }
 //  std::cout << "\n";

 std::cout<<"\n\n";
 std::cout<<"-------------------------------\n";
 std::cout<<"Initial Balance: "<<initialbalance<<"\n";
 std::cout<<"  days per group:   "<<dayspergroup<<"\n";
 std::cout<<"  number of groups: "<<groups<<"\n";
 std::cout<<"  daily growth rate:  "<<rate<<"\n";
 std::cout<<"  Jeff's percent:     "<<jeffspercent<<"\n";
 std::cout<<"Tom's Final Balance: "<<finalbalance<<"\n";
 std::cout<<"Jeffs Cut:           "<<jeffscut<<"\n";
 std::cout<<"-------------------------------\n";
 std::cout<<" w/o including Jeff \n";
 std::cout<<" Tom's Final Balance: "<<nojfinalbalance<<"\n";
 //std::cout<<"Jeffs Cut:           "<<nojjeffscut<<"\n";
 std::cout<<"-------------------------------\n";
 std::cout<<"\n";
  
 return 1;

}

