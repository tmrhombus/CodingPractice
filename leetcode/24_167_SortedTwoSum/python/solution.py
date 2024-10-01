from typing import List
from collections import Counter
import collections


class Solution:
 def twoSum(self, numbers: List[int], target: int) -> List[int]:

  if len(numbers)==2:
   return [1,2]

  L = 0
  R = len(numbers)-1

  while True: 
   thesum = numbers[L] + numbers[R]
   if thesum > target:
    R -= 1
    continue
   elif thesum < target:
    L += 1
    continue
   return [L+1,R+1]

#class Solution:
# def twoSum(self, numbers: List[int], target: int) -> List[int]:
#
#  if len(numbers)==2:
#   return [1,2]
#
#  L = 0
#  R = len(numbers)-1
#
#  while True: 
#   thesum = numbers[L] + numbers[R]
#   if thesum == target:
#    return [L+1,R+1]
#
#   elif thesum > target:
#    R -= 1
#   elif thesum < target:
#    L += 1


#class Solution:
# def twoSum(self, numbers: List[int], target: int) -> List[int]:
#
#  L = 0
#  R = len(numbers)-1
#
#  while True: 
#   thesum = numbers[L] + numbers[R]
#   if thesum == target:
#    return [L+1,R+1]
#
#   elif thesum > target:
#    R -= 1
#   elif thesum < target:
#    L += 1

