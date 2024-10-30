from typing import List
from collections import Counter
import collections

class Solution:
 def isValid(self, s: str) -> bool:

  l = []
  starts = [ "(", "[", "{" ]
  ends   = [ ")", "]", "}" ]
  for a in s:
   if a in starts:
    l.append(a)
   else:
    if len(l) < 1:
     return False
    val = l.pop()
    if a == ")":
     if val != "(":
      return False
    elif a == "]":
     if val != "[":
      return False
    elif a == "}":
     if val != "{":
      return False
  if len(l) > 0: return False
  else: return True
   
