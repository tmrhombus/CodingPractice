from typing import List
from collections import Counter
import collections

class Solution:

 def threeSum(self, nums: List[int]) -> List[List[int]]:

  l = len(nums)
  if l<3:
   return [[]]

  nums.sort()
  out = []

  for i in range(l):
   # sorted, so if nums[i]>0, sum will be >0
   if nums[i] > 0:
    break
   # don't check a starting we've already checked
   elif i > 0 and nums[i]==nums[i-1]:
    continue

   ## set up 2-pointer starting at i+1, through end
   lo, hi = i+1, l-1

   while lo < hi:
    thesum = nums[i] + nums[lo] + nums[hi]
    print(f"summ: {thesum}")
    print(f"{nums[i]} + {nums[lo]} + {nums[hi]}")
    print(f"i:{i} lo:{lo} hi:{hi}")
    if thesum == 0:
     out.append([nums[i], nums[lo], nums[hi]])
     lo, hi = lo + 1, hi - 1
     while lo < hi and nums[lo] == nums[lo-1]:
      lo += 1
     while lo < hi and nums[hi] == nums[hi+1]:
      hi -= 1
    elif thesum < 0:
     lo += 1
    elif thesum > 0:
     hi -= 1  

  if len(out)==0:
   return [[]]
  else: return out 





# def threeSum(self, nums: List[int]) -> List[List[int]]:
#  l = len(nums)
#  if l<3:
#   return [[]]
#
#  out = []
#  s = sorted(nums)
#
#  i = 0
#  while i < l-2:
#   lo = i+1
#   hi = l-1
#   target = 0 - nums[i]
#   
#   while hi > lo:
#    thesum = nums[lo] + nums[hi]
#    if thesum == target:
#     out.append([nums[i], nums[lo], nums[hi]])
#     vlo = nums[lo]
#     vhi = nums[hi]
#     while nums[lo]==vlo:
#      lo += 1
#     while nums[hi]==vhi:
#      hi -= 1
#     
#    elif thesum < target:
#     lo += 1
#    elif thesum > target:
#     hi -= 1
#
#  #c = Counter(nums)
#  #print(c)
#
#  return out ## [[1,2,3],["a","b","c"]]


# def threeSum(self, nums: List[int]) -> List[List[int]]:
#  l = len(nums)
#  if l<3:
#   return [[]]
#
#  s = sorted(nums)
#  
#  i = 0
#  j = 1
#  k = l-1
#
#  out = []
#  z = 1
#  #print(s)
#  while j != k:
#   #print(f"iter: {z}, i={i}, j={j}, k={k}, out: {out}")
#   vi = s[i]
#   vj = s[j]
#   vk = s[k]
#   if vi + vj + vk == 0:
#    out.append([vi,vj,vk])
#    j += 1
#   elif vi + vj + vk > 0:
#    k -= 1
#   elif i+1==j:
#    j += 1
#   else:
#    i += 1
#   z += 1
#
#  return out

