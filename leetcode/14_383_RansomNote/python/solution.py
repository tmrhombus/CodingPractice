class Solution:
 def canConstruct(self, ransomNote: str, magazine: str) -> bool:

  dict_mag = {}
  for m in magazine:
   if m in dict_mag:
    dict_mag[m] += 1
   else:
    dict_mag[m] = 1

  for n in ransomNote:
   if n in dict_mag:
    if dict_mag[n]==0:
     return False
    else:
     dict_mag[n] -= 1
   else:
    return False

  return True
