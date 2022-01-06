
#include <iostream>   // for IO
#include <cmath>      // for pow
#include <vector>     // for vectors

std::vector<float> incrementinterest( int steps, int groups, 
                         float growthrate, float initbalance, 
                         float jeffspercent ){

 std::cout<<"Start of incrementinterest(...)\n";
 std::cout<<" steps: "<<steps<<"\n";
 std::cout<<" groups: "<<groups<<"\n";
 std::cout<<" growthrate: "<<growthrate<<"\n";
 std::cout<<" initbalance: "<<initbalance<<"\n";
 std::cout<<" jeffspercent: "<<jeffspercent<<"\n";

 if( groups <= 0 ){
  std::vector<float>  outputs;
  //outputs.push_back( initbalance  ); 
  outputs.push_back( 0 ); 
  outputs.push_back( initbalance ); 
  return outputs;

 }

 float compoundbalance = initbalance * pow( growthrate, steps );
 float compoundprofit  = compoundbalance - initbalance;

 float jeffscut     = compoundprofit * jeffspercent; 
 float finalbalance = compoundbalance - jeffscut;
 
 std::cout<<" jeffscut: "<<jeffscut<<"\n";
 std::cout<<" finalbalance: "<<finalbalance<<"\n";

 std::vector<float>  outputs;
 outputs = incrementinterest( steps, groups-1, growthrate,
                              finalbalance,
                              jeffspercent );
// //outputs.push_back( initbalance  ); 
// outputs.push_back( jeffscut     ); 
// outputs.push_back( finalbalance ); 

 return outputs ;

}


int main(){

 float initialbalance = 1000;
 int   dayspergroup = 1;
 int   groups = 2; 
 float rate = 1.01;
 float jeffspercent = 0.01;

 std::vector<float> outputs = incrementinterest( dayspergroup, groups, 
   rate, initialbalance, jeffspercent );

 float jeffscut = outputs[0];
 float finalbalance = outputs[1];

 //  // print all elements
 //  std::cout << "vector elements are: ";
 //  for (int i = 0; i < outputs.size(); ++i) {
 //      std::cout << outputs[i] << ' ';
 //  }
 //  std::cout << "\n";

 std::cout<<"Initial Balance: "<<initialbalance<<"\n";
 std::cout<<"  days per group: "<<dayspergroup<<"\n";
 std::cout<<"  rate:  "<<rate<<"\n";
 std::cout<<"Jeffs Cut:     "<<jeffscut<<"\n";
 std::cout<<"Final Balance: "<<finalbalance<<"\n";
  
 return 1;

}


//
//
//
//void printsum( int k ){
//
// while(k>0){
//  std::cout<<std::to_string(k)<<"+";
//  k--; 
// }
// std::cout<<"0";
//
// //if (k <= 1) return 1; 
// //std::cout<<std::to_string(k)<<"+"<<printsum(k-1)<<"\n";
//
//}
//
//int printsum2( int startval ){
// if ( startval <= 1 ){
//   std::cout<<1;
//   return 1;
//
// }
// 
// std::cout<<startval<<"+";
// printsum2(startval-1);
//
// return 1;
// 
//}
//
//int sumtoN( int j ){
// 
// if (j <= 1) return 1;
// int m = j + sumtoN(j-1);
// return m;
//
//}
//
//void sumtoN2 (int n)
//
// int i = 0;
// if (n>1) sumtoN2(n-1);
// for (int i = 0; i < n; i++ ){
//  std::cout<<"*";
// }
//}
