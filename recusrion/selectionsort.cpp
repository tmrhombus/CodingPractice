
#include <iostream>


// find the minimum index
int minIndex(int arr[], int s, int e){

 int sml = INT32_MAX;
 int mindex;

 for (int i = s; i<e; i++){

  if (sml > arr[i]){
   sml = arr[i];
   mindex = i;
  }

 }

 return mindex;

}


void selectionsort( int arr[], int start_index, int end_index){

 if ( start_index >= end_index ){
  for(int i=0; i<7; i++){
   std::cout<<arr[i]<<" ";
  }
  std::cout<<"\n";
  return;
 }

 int min_index;

 min_index = minIndex(arr, start_index, end_index);

 std::swap(arr[start_index], arr[min_index]);

 selectionsort(arr, start_index+1, end_index);

}


int main(){

 int myarray[] = {6, 8, 3, 4, 1, 7, 2};

 for(int i=0; i<7; i++){
  std::cout<<myarray[i]<<" ";
 }
 std::cout<<"\n";
 selectionsort(myarray, 3, 7);

}
