
/* make random numbers in a range */

#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <fstream>
#include <random>

int main()
{

 double x;
 double y;
 double offset = 50;

 int nrolls = 300;

 std::default_random_engine generator;
 std::normal_distribution<double> distribution(25,10.0);
 
// srand(time(NULL));
 
// std::ofstream myfile("oneblob.csv");
// if (myfile.is_open()){
//
//  for( int i =1 ; i < nrolls ; ++i ){
//   x = rand() % 50 + offset;
//   y = rand() % 50 + offset;
//   myfile << x << "," << y << "\n" ;
//  } 
//  //std::cout<<x<<","<<y<<std::endl;
//  myfile.close();
// }

 std::ofstream myfile("twogauss.csv", std::ios_base::app);
 if (myfile.is_open()){

  for (int i=0; i<nrolls; ++i) {
   double x = distribution(generator);
   double y = distribution(generator);
   myfile << x << "," << y << "\n" ;
   //std::cout<<x<<","<<y<<std::endl;
  }
  myfile.close();
 }

}


 // // normal_distribution
 // #include <iostream>
 // #include <string>
 // #include <random>
 // 
 // int main()
 // {
 //   const int nrolls=10000;  // number of experiments
 //   const int nstars=100;    // maximum number of stars to distribute
 // 
 //   std::default_random_engine generator;
 //   std::normal_distribution<double> distribution(5.0,2.0);
 // 
 //   int p[10]={};
 // 
 //   for (int i=0; i<nrolls; ++i) {
 //     double number = distribution(generator);
 //     if ((number>=0.0)&&(number<10.0)) ++p[int(number)];
 //   }
 // 
 //   std::cout << "normal_distribution (5.0,2.0):" << std::endl;
 // 
 //   for (int i=0; i<10; ++i) {
 //     std::cout << i << "-" << (i+1) << ": ";
 //     std::cout << std::string(p[i]*nstars/nrolls,'*') << std::endl;
 //   }
 // 
 //   return 0;
 // }

