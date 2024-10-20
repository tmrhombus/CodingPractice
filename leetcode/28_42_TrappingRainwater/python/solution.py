from typing import List
from collections import Counter
import collections

class Solution:
 def trap(self, height: List[int]) -> int:
  l = len(height)

  if l < 3: return 0
  
  vol, i = 0, 0
  while i < l-1:
   print(f"TOP: i:{i}")
   ## initialize
   ## make sure next wall isn't higher
   hi = height[i]
   if hi <= height[i+1]:
    i += 1
    continue

   ## search
   ## loop through js to see if we find a far wall
   foundwall = False
   for j in range(i+1, l):
    hj = height[j]
    print(f" SEARCH: i:{i} j:{j}, hi:{hi}, hj:{hj}")

    if hj >= hi:
     print(f"  FOUND: hj >= hi, {hj} >= {hi}")
     foundwall = True
     break
    
   ## increment i up to j
   ## adding to volume each step
   if not foundwall:
    i += 1
    continue

   mh = min(hi, hj)
   i += 1
   while i < j:
    vol += ( mh - height[i] )
    i += 1

   i -= 1

  return vol




#   j = i+1
#   print(f"i:{i} j:{j}, vol:{vol}")
#
#   hj = height[j]
#   foundwall = False
#   while hj < hi and j < l-1:
#    print(f" i:{i} j:{j}, hi:{hi}, hj:{hj}")
#    j += 1
#    if j == l-1:
#     break
#    hj = height[j]
#   if not foundwall: 
#    i += 1
#    continue
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
