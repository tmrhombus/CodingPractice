
#include <iostream>

void binary(int n)
{

 if (n==0) return;

 binary(n/2);
 std::cout<< n%2 ;

}


int main(){

 for ( int i=1; i<20; i++){
 
  binary(i);
  std::cout<<"\n";

 }  

 return 1;

}
