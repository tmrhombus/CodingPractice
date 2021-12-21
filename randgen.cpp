
/* make random numbers in a range */

#include <iostream>
#include <stdlib.h>
#include <time.h>
#include <fstream>

int main()
{

 double x;
 double y;
 double offset = 50;
 
 srand(time(NULL));
 
 std::ofstream myfile("oneblob.csv");
 if (myfile.is_open()){

  for( int i =1 ; i < 100 ; ++i ){
   x = rand() % 50 + offset;
   y = rand() % 50 + offset;
   myfile << x << "," << y << "\n" ;
  } 
  //std::cout<<x<<","<<y<<std::endl;
  myfile.close();
 }

}
