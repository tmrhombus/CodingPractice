
#include <iostream>   // for IO
#include <cmath>      // for pow
#include <vector>     // for vectors

std::vector<float> incrementinterest( int steps, float growthrate, float initbalance, 
                         float jeffspercent ){

 float compoundbalance = initbalance * pow( growthrate, steps );
 float compoundprofit  = compoundbalance - initbalance;

 float jeffscut     = compoundprofit * jeffspercent; 
 float finalbalance = compoundbalance - jeffscut;

 std::vector<float>  outputs;
 outputs.push_back( initbalance  ); 
 outputs.push_back( jeffscut     ); 
 outputs.push_back( finalbalance ); 

 return outputs ;

}


int main(){

 float initialbalance = 1000;
 int   steps = 20;
 float rate = 1.01;
 float jeffspercent = 0.00;

 std::vector<float> outputs = incrementinterest( steps, rate, initialbalance, jeffspercent );

 // print all elements
 std::cout << "vector elements are: ";
 for (int i = 0; i < outputs.size(); ++i) {
     std::cout << outputs[i] << ' ';
 }
 std::cout << "\n";

// std::cout<<"Initial Balance: "<<initialbalance<<"\n";
// std::cout<<"  steps: "<<steps<<"\n";
// std::cout<<"  rate:  "<<rate<<"\n";
// std::cout<<"Final Balance: "<<finalbalance<<"\n";
  
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
