from typing import List
from collections import Counter
import collections

class Solution:
 def twoSum(self, numbers: List[int], target: int) -> List[int]:

  L = 0
  R = len(numbers)-1

  while True: 
   thesum = numbers[L] + numbers[R]
   if thesum == target:
    return [L+1,R+1]

   elif thesum > target:
    R -= 1
   elif thesum < target:
    L += 1

