class Solution(object):
 def romanToInt(self, s) -> int :
  """
  :type s: str
  :rtype: int
  """

  dict_numerals = {
   "I":  1,   
   "V":  5,  
   "X":  10,  
   "L":  50,  
   "C":  100, 
   "D":  500, 
   "M":  1000
  }

  out = 0
  for a in range(len(s)-1):
   #print(f"a {a}, s[a] {s[a]}, dict[s[a]] {dict_numerals[s[a]]}")
   out += dict_numerals[s[a]]

   if s[a]=="I" and (s[a+1] =="V" or s[a+1]=="X"):
    out -= 2
   elif s[a]=="X" and (s[a+1] =="L" or s[a+1]=="C"):
    out -= 20
   elif s[a]=="C" and (s[a+1] =="D" or s[a+1]=="M"):
    out -= 200

  out += dict_numerals[s[-1]]

  return out

        
