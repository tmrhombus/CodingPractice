from typing import List
from collections import Counter
import collections

class Solution:
 def trap(self, height: List[int]) -> int:
  l = len(height)

  if l < 3: return 0

  #height.append(0)
  
  vol, i, j = 0, 0, 1
  while i < l and j < l:
   j = i+1
   print(f"i:{i} j:{j}, vol:{vol}")

   hi = height[i]
   hj = height[j]
   while hj < hi and j < l:
    print(f" i:{i} j:{j}, hi:{hi}, hj:{hj}")
    j += 1
    hj = height[j]
   minh = min(hi,hj)
   print(f" hi:{hi}, hj:{hj}, minh:{minh}")
   print(f" i:{i} j:{j}, vol:{vol}")
   for k in range(i+1,j):
    print(k)
    vol += minh - height[k]

   i = j+1

  return vol

# def trap(self, height: List[int]) -> int:
#  l = len(height)
#
#  if l < 3: return 0
#
#  #height.append(0)
#  
#  vol = 0
#  i, j = 0, 1
#  while i < l and j < l:
#   j = i+1
#   print(f"i:{i} j:{j}, vol:{vol}")
#
#   hi = height[i]
#   hj = height[j]
#   while hj < hi and j < l:
#    print(f" i:{i} j:{j}, hi:{hi}, hj:{hj}")
#    j += 1
#    hj = height[j]
#   minh = min(hi,hj)
#   print(f" hi:{hi}, hj:{hj}, minh:{minh}")
#   print(f" i:{i} j:{j}, vol:{vol}")
#   for k in range(i+1,j):
#    print(k)
#    vol += minh - height[k]
#
#   i = j+1
#
#  return vol
