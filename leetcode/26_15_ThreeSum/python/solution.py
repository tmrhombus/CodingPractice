from typing import List
from collections import Counter
import collections

class Solution:
 def threeSum(self, nums: List[int]) -> List[List[int]]:
  l = len(nums)
  if l<3:
   return [[]]
  
  s = sorted(nums)
  
  i = 0
  j = 1
  k = l-1

  out = []
  z = 1
  print(s)
  while j != k:
   print(f"iter: {z}, i={i}, j={j}, k={k}, out: {out}")
   vi = s[i]
   vj = s[j]
   vk = s[k]
   if vi + vj + vk == 0:
    out.append([vi,vj,vk])
    j += 1
   elif vi + vj + vk > 0:
    k -= 1
   elif i+1==j:
    j += 1
   else:
    i += 1
   z += 1

  return out

