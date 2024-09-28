from typing import List
from collections import Counter
import collections

class Solution:
 def reverseString(self, s: List[str]) -> None:
  """
  Do not return anything, modify s in-place instead.
  """

  l = len(s)
  for i in range(l//2):
   print(f"{i} : {i//2} ")
   s[i], s[l-1-i] = s[l-1-i], s[i]
