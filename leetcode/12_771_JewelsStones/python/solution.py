class Solution:
 def numJewelsInStones(self, jewels: str, stones: str) -> int:
  count = 0

  dict_jewelcount = {}
  for j in jewels:
   dict_jewelcount[j] = 0

  for s in stones:
   if s in dict_jewelcount:
    count += 1

  return count
