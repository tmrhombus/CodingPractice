
#include <iostream>

int factorial( int n ){

 if (n <= 1) return 1;

 int m = n * factorial(n-1);

 return m;

}

int main(){

for (int i = 0; i < 6; i++){

 std::cout<<"Factorial of "<<i<<" : "<<
 factorial(i) << "\n";

}

return 1;

}

