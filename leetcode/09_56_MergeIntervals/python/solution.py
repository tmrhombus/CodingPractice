from typing import List

class Solution:
 def merge(self, intervals: List[List[int]]) -> List[List[int]]:
  n = len(intervals) 
  if n==1: return intervals
  out = []

  dict_in = {}
  for i in range(n):
   key = intervals[i][0]
   val = intervals[i][1]
   if not key in dict_in:
    dict_in[key] = val
   else:
    dict_in[key] = max(dict_in[key], val)

  i=0
  for key in sorted(dict_in):
   val = dict_in[key]
   if i==0:
    lo = key
    hi = val
    i+=1
    print(f"first iteration:")
    print(f"key:{key}, v:{val}, lo:{lo}, hi:{hi} ")
    continue
   print(f"key:{key}, v:{val}, lo:{lo}, hi:{hi}")
   if key <= hi:
    hi = max(hi,val)
    print(f"  key<=hi, set hi:: lo:{lo}, hi:{hi}")
   else:
    print(f"  writing [{lo},{hi}] to out")
    out.append([lo,hi])
    lo = key
    hi = max(hi,val)
    print(f"  setting lo:{lo}, hi:{hi}")

  out.append([lo,hi])
  
  return out
