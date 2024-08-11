#include <iostream>

class Solution {
public:
 std::string mergeAlternately(std::string word1, std::string word2) {
  int len1 = word1.length();
  int len2 = word2.length();
  int len_min = std::min(len1, len2);
  //std::cout<<"L1: "<<len1<<std::endl;
  //std::cout<<"L2: "<<len2<<std::endl;
  //std::cout<<"Min: "<<len_min<<std::endl;

  std::string out="";
  for(int i=0; i<len_min; ++i){
   out += word1[i];
   out += word2[i];
  }
  if(len1 > len_min){
   for(int i=len_min; i<len1; ++i){
    out += word1[i];
   }
  }
  if(len2 > len_min){
   for(int i=len_min; i<len2; ++i){
    out += word2[i];
   }
  }
  
  return out;
 }
};


int main(){

 std::string word1 = "abcdefg";
 std::string word2 = "hij";

 Solution sol;
 
 std::string out = sol.mergeAlternately(word1, word2);

 std::cout<<"Word 1: "<<word1<<std::endl;
 std::cout<<"Word 2: "<<word2<<std::endl;

 std::cout<<"Output: "<<out<<std::endl;



return 1;
}
