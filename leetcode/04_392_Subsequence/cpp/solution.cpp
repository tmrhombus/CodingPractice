#include <iostream>


class Solution {
public:
 bool isSubsequence(std::string s, std::string t) {
  int index_s, index_t = 0;

  while (index_t < t.length() ){
   //std::cout<<index_t<<std::endl;
   if(s[index_s]==t[index_t]){
    index_s++;
   }
   index_t ++;
  }

  return index_s==s.length();
 }
};


int main(){

 std::string s = "adg";
 std::string t = "agbcdefg";

 Solution sol;
 
 bool  out = sol.isSubsequence(s, t);

 std::cout<<"Word 1: "<<s<<std::endl;
 std::cout<<"Word 2: "<<t<<std::endl;
 std::cout<<"Is Subsequence: "<<out<<std::endl;

 return 1;
}
