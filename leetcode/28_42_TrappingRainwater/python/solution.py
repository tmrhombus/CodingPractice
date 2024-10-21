from typing import List
from collections import Counter
import collections

class Solution:
 def trap(self, height: List[int]) -> int:
  l = len(height)

  if l < 3: return 0
  
  lwall = [0] * l
  rwall = [0] * l

  lw = 0
  rw = 0
  for i in range(l):
   j = l-i-1
   print(f"i:{i} j:{j}, lw:{lw}")
   lwall[i] = lw
   rwall[j] = rw

   lw = max(lwall[i], height[i])
   rw = max(rwall[j], height[j])

  print(f"lwall: {lwall}")
  print(f"rwall: {rwall}")
  vol = 0
  for i in range(l):
   vol += max(min(lwall[i], rwall[i]) - height[i], 0)

  return vol

