#include <iostream>
#include <vector>

class Solution {
public:

 std::string makeString(int a, int b){
  if(a==b){return std::to_string(a);}
  else{return std::to_string(a)+"->"+std::to_string(b);}
 }

 std::vector<std::string> summaryRanges(std::vector<int>& nums) {
  std::vector<std::string> out;

  int nsize = nums.size();
  if(nsize==0){
   out = {};
   return out;
  }
  else if(nsize==1){
   out.push_back(std::to_string(nums[0]));
   return out;
  }

  int start = nums[0];
  int next = start + 1;
  for(int i=1; i<nsize; i++){

   //std::cout<<"nums["<<i<<"]: "<<nums[i];
   //std::cout<<" start: "<<start<<" next: "<<next<<std::endl;

   if(nums[i]!=next){
    out.push_back( makeString(start,nums[i-1]) );
    start = nums[i];
   }

   if(i==nsize-1){
    out.push_back( makeString(start,nums[i]) );
    return out;
   }

   next = nums[i] + 1;
  }

  return out;

 }
};


int main(){

 //std::vector<int> nums = {0,1,2,4,5,7};
 //std::vector<int> nums = {-3,1,2,4,5,6};
 //std::vector<int> nums = {-200,-143,2,4,5,7,8};
 //std::vector<int> nums = {};
 std::vector<int> nums = {-1};

 Solution sol;
 
 std::vector<std::string> out = sol.summaryRanges(nums);

 std::cout<<"Input: "<<std::endl;
 for(int i=0; i<nums.size(); i++){
  std::cout<<" "<<nums[i];
 }
 std::cout<<std::endl;
 std::cout<<"Summary: ";
 for(int i=0; i<out.size(); i++){
  std::cout<<" "<<out[i];
 }
 std::cout<<std::endl;

 return 1;
}
