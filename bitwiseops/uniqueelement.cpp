
#include <iostream>
using namespace std;
  
// Function to return the only uniquely
// occurring element using XOR


int findUnique(int arr[], int n)
{
    int res = 0, i;
    for (i = 0; i < n; i++)
        res ^= arr[i];
    return res;
}
  
// Driver Method
int main(void)
{
    int arr[] = { 12, 12, 14, 90, 14, 14, 14 };
    int n = sizeof(arr) / sizeof(arr[0]);
    cout << "The uniquely occurring element is  "<< findUnique(arr, n);
    return 0;
}


