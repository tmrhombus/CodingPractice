
/* make random numbers in a range */

#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <fstream>
#include <random>

int main()
{

 double x;  // x variable to be filled
 double y;  // y variable to be filled

 int npoints = 300;  //

 int xmin = 10;
 int xmax = 40;


 // y = mx + b
  double m = 4;
  double b = 12;

 /* Create random engine with the help of seed */
 unsigned seed = std::chrono::steady_clock::now().time_since_epoch().count(); 

 // x's are uniformly distributed along an interval
  // plus gaussian jitter
 std::default_random_engine generatorX(seed);
 std::normal_distribution<double> distributionX(0,0.5);

 srand(seed);

 // y's vary like gaussian wrt the line
 std::default_random_engine generatorY(seed+1);
 std::normal_distribution<double> distributionY(0,4.0);

  // distribution(mean,variance) 

 std::ofstream myfile("data/linear2d.csv", std::ofstream::trunc);
 //std::ofstream myfile("data/gauss.csv", std::ios_base::app);
 if (myfile.is_open()){

  myfile << "x,y" << "\n" ;
  for (int i=0; i<npoints; ++i) {
   // x is random int along interval
   x = rand() % (xmax-xmin) + xmin;
   // add the jitter
   x += distributionX(generatorX);

   // y falls along the line
   y = m*x + b;
   // plus jitter
   y += distributionY(generatorY);

   myfile << x << "," << y << "\n" ;
   //std::cout<<x<<","<<y<<std::endl;
  }
  myfile.close();
 }

}




