from typing import List
from collections import Counter
import collections

class Solution:
 def isPalindrome(self, s: str) -> bool:
  st = ''.join(e for e in s if e.isalnum())
  l = len(st)
  if l<2:
   return True
  else:
   for i in range(l//2):
    if st[i].lower() != st[l-1-i].lower():
     return False

  return True
