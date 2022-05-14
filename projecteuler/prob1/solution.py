

def solution( target ):
 """
 returns the sum of all multiples of 3 or 5 
 below target
 """

 # initialize hashset
 s = set()

 i=1
 while True:
  if 3*i < target:
   s.add(3*i)
   i += 1
  else:
   break

 j=1
 while True:
  if 5*j < target:
   s.add(5*j)
   j += 1
  else:
   break


 print (s)

 thesum = 0
 for a in s:
  thesum += a

 print( "Sum = {}".format(thesum))
