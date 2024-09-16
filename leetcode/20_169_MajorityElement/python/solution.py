from typing import List
from collections import Counter
import collections

class Solution:
 def majorityElement(self, nums: List[int]) -> int:

  c = Counter(nums)
  print(c)

  maxind = 0
  maxval = c[0]

  for key in c:
   print(f"---------------")
   print(f"maxind {maxind}")
   print(f"maxval {maxval}")
   print(f"key    {key   }")
   print(f"c[key] {c[key]}")
   if c[key] > maxval:
    maxval = c[key]
    maxind = key
  
  return maxind
