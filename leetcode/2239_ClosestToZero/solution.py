
from typing import List

class Solution:
 def findClosestNumber(self, nums: List[int]) -> int:
  val  = nums[0]
  dist = abs(nums[0])
  for i in range(len(nums)):
   if abs(nums[i]) < dist:
    val = nums[i]
    dist = abs(nums[i])

   if abs(nums[i]) == dist:
    if nums[i] > val:
     val = nums[i]

  return val

