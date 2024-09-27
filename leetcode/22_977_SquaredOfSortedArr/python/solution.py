from typing import List
from collections import Counter
import collections

class Solution:
 def sortedSquares(self, nums: List[int]) -> List[int]:

  if len(nums)==1: return [nums[0]**2]

  s = len(nums)
  out = s*[0]

  for i in range(s):
   out[i] = nums[i]**2

  return sorted(out)


# def sortedSquares(self, nums: List[int]) -> List[int]:
#
#  if len(nums)==1: return [nums[0]**2]
#
#  s = len(nums)
#  out = s*[0]
#  R = s-1
#  L = 0
#
#  for i in range(s):
#   print(f"R: {R}, L: {L}")
#   val_r = nums[R]**2
#   val_l = nums[L]**2
#   if val_r > val_l:
#    out[s-i-1] = val_r
#    R -= 1
#   else:
#    out[s-i-1] = val_l
#    L += 1
#
#  return out

   
    
