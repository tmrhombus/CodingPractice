from collections import Counter

class Solution:
 def maxNumberOfBalloons(self, text: str) -> int:

  counts_letters = Counter(text)
  #print(counts_letters)
  #print(counts_letters["b"]    )
  #print(counts_letters["a"]    )
  #print(counts_letters["l"]//2 )
  #print(counts_letters["o"]//2 )
  #print(counts_letters["n"]    )


  ## b
  out = counts_letters["b"]
  ## a
  out = min(out, counts_letters["a"] )
  ## ll
  out = min(out, counts_letters["l"]//2 )
  ## oo
  out = min(out, counts_letters["o"]//2 )
  ## n
  out = min(out, counts_letters["n"] )
   
  return out
