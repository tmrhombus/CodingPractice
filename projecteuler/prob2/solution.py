

def solution( target ):
 """
 returns the sum of all even Fibonacci numbers
 below target
 """

 # initialize hashset
 s = set()

 twoback=0
 lastone=1
 thisone=1

 while thisone < target:
  nextone = thisone+lastone+twoback
  if nextone%2 == 0:
   s.add(nextone)

  twoback=lastone
  lastone=thisone
  thisone=nextone


 print (s)

 thesum = 0
 for a in s:
  thesum += a

 print( "Sum = {}".format(thesum))

 return s
