from typing import List

class Solution:
 def maxProfit(self, prices: List[int]) -> int:


  profit = 0
  val = prices[0]
  for i in range(1, len(prices)):
   print(f"{i} {prices[i]}")

   if prices[i] < val:
    val = prices[i]
   elif (prices[i] - val) > profit:
    profit = prices[i] - val

  return profit

