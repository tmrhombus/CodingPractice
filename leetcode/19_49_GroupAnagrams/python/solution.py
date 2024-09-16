from typing import List
from collections import Counter

class Solution:
 def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

  dict_out = {}
  for s in strs:
   key = ''.join(sorted(s))
   if key not in dict_out:
    dict_out[key] = [s]
   else:
    dict_out[key].append(s)
    
  out = []
  for k in dict_out:
   out.append(dict_out[k])

  return out

