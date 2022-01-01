
#include <iostream>

int countupdown( int startval, int endval ){

 if(startval <= 0) return 1; 
 if(startval >= endval) return 1;


 std::cout<< startval << " ";
 countupdown(startval+1, endval);
 std::cout<< startval << " ";

 return 1;

}



int main( ){

 int max = 6;

 countupdown(2,max);
 std::cout<<"\n";

 return 1;

}
