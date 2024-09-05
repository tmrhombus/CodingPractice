#include <iostream>
#include <vector>

class Solution {
public:
 std::vector<int> spiralOrder(std::vector<std::vector<int>>& matrix) {
     
  int nrows = matrix.size();
  if(nrows==0){
   std::vector<int> out = {};
   return out;
  }
  int ncols = matrix[0].size();

  int nentries = nrows * ncols;
  std::vector<int> out(nentries);
  std::cout<<"nrows: "<<nrows<<" ncols: "<<ncols<<" nentries: "<<nentries<<std::endl;

  // Specify Values for Directions
  int R = 1;
  int D = 2;
  int L = 3;
  int U = 4;

  // Specify Current Direction
  int direction = R; 

  // Specify "Walls" 
  int wall_L = -1;
  int wall_U = 0;
  int wall_R = ncols;
  int wall_D = nrows;

  // Specify Current Coordinates
  int i = 0; // row coordinate
  int j = 0; // column coordinate

  for(int k=0; k<nentries; k++){

   if(direction==R){
    while(j < wall_R){
     out[k] = matrix[i][j];
     //std::cout<<"k "<<k<<": "<<out[k]<<std::endl;
     j++;
     k++;
    }
    j--;
    k--;
    i++;
    wall_R--;
    direction = D;
   }
   else if(direction == D){
    while(i < wall_D ){
     out[k] = matrix[i][j];
     //std::cout<<"k "<<k<<": "<<out[k]<<std::endl;
     i++;
     k++;
    }
    i--;
    k--;
    j--; 
    wall_D--;
    direction = L;
   }
   else if(direction == L){
    while(j > wall_L ){
     out[k] = matrix[i][j];
     //std::cout<<"k "<<k<<": "<<out[k]<<std::endl;
     j--;
     k++;
    }
    j++;
    k--;
    i--; 
    wall_L++;
    direction = U;
   }
   else {
    while(i > wall_U ){
     out[k] = matrix[i][j];
     //std::cout<<"k "<<k<<": "<<out[k]<<std::endl;
     i--;
     k++;
    }
    i++;
    k--;
    j++; 
    wall_U++;
    direction = R;
   }

  }


  return out;
 }
};


int main(){

 std::vector<std::vector<int>> matrix = {{11,12,13,14,15,16},
                                         {21,22,23,24,25,26},
                                         {31,32,33,34,35,36},
                                         {41,42,43,44,45,46},
                                         {51,52,53,54,55,56}
};
 for(int i=0; i<matrix.size(); i++){
  for(int j=0; j<matrix[0].size(); j++){
   std::cout<<matrix[i][j]<<" ";
  }
  std::cout<<std::endl;
 }
 std::cout<<std::endl;

 Solution sol;

 std::vector<int> out = sol.spiralOrder( matrix );

 for(int i=0; i<out.size(); i++){
  std::cout<<out[i]<<" ";
 }
 std::cout<<std::endl;
 return 1;
}
