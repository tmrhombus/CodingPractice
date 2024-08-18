#include <iostream>
#include <vector>

class Solution {
public:
 std::vector<int> productExceptSelf(std::vector<int>& nums) {

  int n = nums.size();
  std::vector<int> out(n,1);

  std::vector<int> pL(n, 1);
  std::vector<int> pR(n, 1);
  for(int i=1; i<n; i++){
   pL[i]     = pL[i-1] * nums[i-1] ;
   pR[n-i-1] = pR[n-i] * nums[n-i] ;
  }
 
  for(int i=0; i<pL.size(); i++){
   std::cout<<" pL["<<i<<"]: "<<pL[i]<<std::endl;
   std::cout<<" pR["<<i<<"]: "<<pR[i]<<std::endl;
  }

  for(int i=0; i<n; i++){
   out[i] = pR[i]* pL[i] ;
  }

  return out;       
 }
};


int main(){

 //std::vector<int> nums = {1,2,3,4};
 //std::vector<int> nums = {2,3,5,7};
 std::vector<int> nums = {-1,1,0,-3,3};

 Solution sol;
 
 std::vector<int> out = sol.productExceptSelf(nums);

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
