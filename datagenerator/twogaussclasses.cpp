
/* make random numbers in a range */

#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <fstream>
#include <random>

int main()
{

 // double x;  // x variable to be filled
 // double y;  // y variable to be filled

 int npoints = 150;  //


 /* Create random engine with the help of seed */
 unsigned seed = std::chrono::steady_clock::now().time_since_epoch().count(); 
 //default_random_engine e (seed); 

 std::default_random_engine generatoraX(seed);
 std::normal_distribution<double> distributionaX(25,10.0);

 std::default_random_engine generatoraY(seed+1);
 std::normal_distribution<double> distributionaY(25,10.0);

 std::default_random_engine generatorbX(seed+2);
 std::normal_distribution<double> distributionbX(50,10.0);

 std::default_random_engine generatorbY(seed+3);
 std::normal_distribution<double> distributionbY(50,10.0);

 // distribution(mean,variance) 

 std::ofstream myfile("data/twogaussclasses.csv", std::ofstream::trunc);
 //std::ofstream myfile("data/gauss.csv", std::ios_base::app);
 if (myfile.is_open()){

  myfile << "x,y,z" << "\n" ;
  for (int i=0; i<npoints; ++i) {
   double x1 = distributionaX(generatoraX);
   double y1 = distributionaY(generatoraY);
   int    z1 = 0;
   myfile << x1 << "," << y1 << ","<< z1 << "\n" ;

   double x2 = distributionbX(generatorbX);
   double y2 = distributionbY(generatorbY);
   int    z2 = 1;
   myfile << x2 << "," << y2 << ","<< z2 << "\n" ;

   //std::cout<<x1<<","<<y1<<","<<z1<<std::endl;
   //std::cout<<x2<<","<<y2<<","<<z2<<std::endl;
  }
  myfile.close();
 }

}



// random points within some window
 //srand(time(NULL));
 
 //   
 //   std::ofstream myfile("twogauss.csv");
 //   if (myfile.is_open()){
 //  
 //    for( int i =1 ; i < npoints ; ++i ){
 //     x = rand() % 50 + offset;
 //     y = rand() % 50 + offset;
 //     myfile << x << "," << y << "\n" ;
 //    } 
 //    //std::cout<<x<<","<<y<<std::endl;
 //    myfile.close();
 //   }




 // // normal_distribution
 // #include <iostream>
 // #include <string>
 // #include <random>
 // 
 // int main()
 // {
 //   const int npoints=10000;  // number of experiments
 //   const int nstars=100;    // maximum number of stars to distribute
 // 
 //   std::default_random_engine generator;
 //   std::normal_distribution<double> distribution(5.0,2.0);
 // 
 //   int p[10]={};
 // 
 //   for (int i=0; i<npoints; ++i) {
 //     double number = distribution(generator);
 //     if ((number>=0.0)&&(number<10.0)) ++p[int(number)];
 //   }
 // 
 //   std::cout << "normal_distribution (5.0,2.0):" << std::endl;
 // 
 //   for (int i=0; i<10; ++i) {
 //     std::cout << i << "-" << (i+1) << ": ";
 //     std::cout << std::string(p[i]*nstars/npoints,'*') << std::endl;
 //   }
 // 
 //   return 0;
 // }

