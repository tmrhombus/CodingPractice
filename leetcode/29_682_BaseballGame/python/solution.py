from typing import List
from collections import Counter
import collections

class Solution:
 def calPoints(self, operations: List[str]) -> int:
  ''' 
  An integer x.
      Record a new score of x.
  '+'.
      Record a new score that is the sum of the previous two scores.
  'D'.
      Record a new score that is the double of the previous score.
  'C'.
      Invalidate the previous score, removing it from the record.
  ''' 
  record = []
  for i in operations:
   print(f"i: {i}, record: {record}")
   if i=="+":
    record.append( record[-1] + record[-2]  )
   elif i=="D":
    record.append( 2*record[-1] )
   elif i=="C":
    record.pop()
   else:
    record.append(int(i))
    
  print(record)

  return sum(record)
