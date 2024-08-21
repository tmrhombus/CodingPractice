from typing import List

class Solution:
 def productExceptSelf(self, nums: List[int]) -> List[int]:
 
  n = len(nums)
 
  out = n * [1]

  prod  = 1
  for i in range(1,n):
   print(f" nums[{i}]: {nums[i]}")
   out[i] *= out[i-1]*nums[i-1]

  for i in range(1,n):
   print(f" nums[{i}]: {nums[i]}")

   prod *= nums[n-i]
   out[n-i-1] *= prod 
  
 
  return out
