
#include <iostream>

int getmax( int a[], int n ){

 int x; 
 if (n==1) return a[0];
 else x=getmax(a, n-1);

 if (x > a[n-1]) return x;
 else return a[n-1];

}


int printsubarray( int a[], int n ){

 int k = n-1;
 if(k < 0) return 1;

 printsubarray(a, k);
 std::cout<<a[k]<<" ";

 return 1;

}


int main(){

 int myarray[] = {4, 3, 7, 9, 2, 1};


 for(int i=1; i<=6; i++){

  std::cout<<"Subarray: ";
  printsubarray(myarray, i);
  std::cout<<"\n";
  std::cout<<"Max Value: "<<getmax(myarray, i)<<"\n\n";

 }

 return 1;
}
