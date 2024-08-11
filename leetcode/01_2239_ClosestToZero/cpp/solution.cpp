#include <iostream>
#include <vector>

class Solution {
public:
 int findClosestNumber(std::vector<int>& nums) {
  std::vector<int> pos;
  std::vector<int> neg;

  int min_pos, max_neg;
  
  for(auto i : nums){
   if(i>0){pos.push_back(i);}
   else if(i<0)  {neg.push_back(i);}
   else {return 0;}
  }  

  if(neg.size()>0){
   max_neg = neg[0];
   for(int i=1; i<neg.size(); i++){
    if(neg[i]>max_neg){
     max_neg = neg[i];
    }
   }
  }   

  if(pos.size()>0){
   min_pos = pos[0];
   for(int i=1; i<pos.size(); i++){
    if(pos[i]<min_pos){
     min_pos = pos[i];
    }
   }
  }   

  if (pos.size() == 0){
   return max_neg; 
  }
  if (neg.size() == 0){
   return min_pos;
  }
  if(min_pos<=std::abs(max_neg)){
   return min_pos;
  }
  else{ return max_neg; }


 }
};


int main() {

//std::vector<int> input_list = {-6,-4,-1,-3};
std::vector<int> input_list = {1,2,-5,5,-1};

Solution sol;

int val = sol.findClosestNumber(input_list);


std::cout<<"Input List: ";
for (auto i : input_list){
 std::cout<<i<<" ";
}
std::cout<<""<<std::endl;

std::cout<<"Min: "<<val<<std::endl;

return 1;

}
