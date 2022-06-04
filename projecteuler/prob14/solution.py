
def solution( maxn ):
 """
 returns the longest Collatz chain with seed < <maxn>

 method: check them all, save the longest
 """

 maxchain = [1,2,3,4]

 doprint=False

 for i in range(1,maxn):

  thischain = makechain(i)
  
  if len(thischain)>len(maxchain):
   maxchain = thischain

 return maxchain


def makechain(x):
 """
 if x is odd,   -> 3x+1
 if x is even,  -> x/2
 """
 thechain = []

 while True:
  
  if x==1:
   return thechain



 
