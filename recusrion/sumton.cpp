
#include <iostream>


void printsum( int k ){

 while(k>0){
  std::cout<<std::to_string(k)<<"+";
  k--; 
 }
 std::cout<<"0";

 //if (k <= 1) return 1; 
 //std::cout<<std::to_string(k)<<"+"<<printsum(k-1)<<"\n";

}

int printsum2( int startval ){
 if ( startval <= 1 ){
   std::cout<<1;
   return 1;

 }
 
 std::cout<<startval<<"+";
 printsum2(startval-1);

 return 1;
 
}

int sumtoN( int j ){
 
 if (j <= 1) return 1;
 int m = j + sumtoN(j-1);
 return m;

}

void sumtoN2 (int n)
{
 int i = 0;
 if (n>1) sumtoN2(n-1);
 for (int i = 0; i < n; i++ ){
  std::cout<<"*";
 }
}

int main(){

 for ( int i = 2; i < 7; i++ ){

  printsum(i);
  //std::cout<<i<<"\n";
  std::cout<<" = ";
  std::cout<<sumtoN(i)<<"\n";
  sumtoN2(i);
  std::cout<<"\n";
  printsum2(i);
  std::cout<<"\n\n";

 }
 
 return 1;

}
