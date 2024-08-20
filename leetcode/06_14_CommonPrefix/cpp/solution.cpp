#include <iostream>
#include <vector>

class Solution {
public:
 std::string longestCommonPrefix(std::vector<std::string>& strs) {

  if(strs.size()==1){return strs[0];}

  std::string lcp = "";

  int minl = strs[0].size();
  for(int i=1; i<strs.size(); i++){
   if(strs[i].size() < minl){
    if(strs[i].size()==0){return "";}
    minl = strs[i].size();
   }
  }

  std::cout<<minl<<std::endl;

  for(int i=0; i<minl; i++){
   char let = strs[0][i];
   for(int j=1; j<strs.size(); j++){
    if(strs[j][i] != let){return lcp;}
   }
   lcp += let;
  }
  return lcp;
 }
};


int main(){

 std::vector<std::string> strs = {"avv",  "avoijijt", "av", "avoi", "ba" };
 //std::vector<std::string> strs = {"avv",  "avoijijt", "av", "", "avoi" };
 //std::vector<std::string> strs = { "avoijijt" };

 Solution sol;
 
 std::string out = sol.longestCommonPrefix(strs);;

 std::cout<<"Strings: "<<std::endl;
 for(int i=0; i<strs.size(); i++){
  std::cout<<" "<<strs[i];
 }
 std::cout<<std::endl;
 std::cout<<"Longest Prefix: "<<out<<std::endl;

 return 1;
}
