class Solution(object):
 def mergeAlternately(self, word1, word2):
  """
  :type word1: str
  :type word2: str
  :rtype: str
  """
  len1 = len(word1)
  len2 = len(word2)
  len_min = min(len1, len2)

  out = ""
  for a,b in zip(word1, word2):
   out += a
   out += b

  if(len1>len_min):
   out += word1[len_min:len1]
  if(len2>len_min):
   out += word2[len_min:len2]

  return out
