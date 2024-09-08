from collections import Counter

class Solution:
 def isAnagram(self, s: str, t: str) -> bool:

  if len(s)!=len(t):
   return False

  counts_s = Counter(s)
  counts_t = Counter(t)

  for k in counts_s:
   if counts_s[k] != counts_t[k]:
    return False

  return True
