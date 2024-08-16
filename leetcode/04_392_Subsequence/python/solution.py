class Solution(object):
 def isSubsequence(self, s, t):
  """
  :type s: str
  :type t: str
  :rtype: bool
  """
  
  len_s = len(s)
  if len(s)==0: return True
  #print(len_s)
  s_index = 0
  s_val = s[0]
  for i in range(len(t)):
   #print(  f"i: {i}, t[i]: {t[i]}"  )

   if t[i] == s_val:
    s_index += 1
    if s_index == len_s:
     return True
    s_val = s[s_index] 

  return False
        
