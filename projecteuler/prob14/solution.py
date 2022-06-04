
def solution( maxn ):
 """
 returns the longest Collatz chain with seed < <maxn>

 method: check them all, save the longest
 """

 maxchain = []

 doprint=True

 for i in range(1,maxn):

  thischain = makechain(i,doprint)
  
  if len(thischain)>len(maxchain):
   maxchain = thischain

 return maxchain


def makechain(x,doprint):
 """
 if x is odd,   -> 3x+1
 if x is even,  -> x/2
 """
 if(doprint):
  print("\n\n Making chain for {}".format(x))

 thechain = [x]

 while True:

  if(doprint):
   print("x = {}".format(x))
  
  if x==1:
   return thechain

  if x%2 == 0:
   x = x/2

  else:
   x = 3*x+1

 
