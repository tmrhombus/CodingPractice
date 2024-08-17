#include <iostream>
#include <vector>

class Solution {
 public:
  int maxProfit(std::vector<int>& prices) {

   int max_to_right = -1;
   int profit = 0;

   for(int i=prices.size()-2; i>-1; i--){
    max_to_right = std::max(prices[i+1], max_to_right);
    profit = std::max( profit, max_to_right-prices[i] );
    std::cout<<"i: "<<i<<
     " v: "<<prices[i]<<
     " m: "<<max_to_right<<
     " p: "<<profit<<
     std::endl;
   }

   return profit; 
  }
};

int main(){

  //{3, 4, 1, 3}

  //i=3, v=3, m=DNE
  //i=2, v=1, m=m(3,DNE)=3
  //i=1, v=4, m=m(1,3)=3
  //i=0, v=3, m=m(4,3)=4


 std::vector<int> prices = {6, 4, 1, 5, 4, 3, 12, 8, 2};

 //std::vector<int> prices = {3, 4, 1, 3};
 Solution sol;
 
 int out = sol.maxProfit(prices);

 std::cout<<"Price List: "<<std::endl;
 for(int i=0; i<prices.size(); i++){
  std::cout<<" "<<prices[i];
 }
 std::cout<<std::endl;
 std::cout<<"Max Profit: "<<out<<std::endl;

 return 1;
}
