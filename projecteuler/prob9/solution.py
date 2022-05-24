import math 

def solution( p ):
 """
 returns the list of pythagorean triplets which
  sum to p

 method: brute force 
  loop through a,b
  check if c=p-a-b completes the triplet
 """

 trips = []
 for a in range( 1,p ):
  for b in range( 1,p-a ):
   print(" {} + {} = {}".format(a,b,a+b))

 return trips
