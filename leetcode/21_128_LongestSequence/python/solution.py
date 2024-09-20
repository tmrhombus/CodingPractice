from typing import List
from collections import Counter
import collections

class Solution:
 def longestConsecutive(self, nums: List[int]) -> int:

  s = set(nums)
  longest = 0

  for n in s:
   thislen = 1
   if (n-1) not in s:
    np = n+1
    while np in s:
     thislen += 1
     np += 1
    longest = max(thislen, longest)

  return longest
