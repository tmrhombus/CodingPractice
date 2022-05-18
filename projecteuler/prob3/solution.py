

def solution( target ):
 """
 returns the largest prime factor of target

 method:

 find A = lowest factor of target by checking 2,3,4,...
 split target into t = A*B 
  A is prime, add it to set of primes
  B becomes new target
   repeat iteraticely

  if we can not find any factors for target, we're done
 
 """

 #factors = set( target )
 pfactors = set()

 
 
 

def findminfactor( x ):
 """
 find first factor of x
 """

 i=2
 while i<x:
  if x%i == 0: 
   return i
  else:
    i = i+1  

 return -1



