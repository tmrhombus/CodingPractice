import math 

def solution( p ):
 """
 returns the list of all primes less than p
 as well as their sum

 method: incremental sieve as in problem 7
 """

 primes = [ [2, 2] ]
 
 x=3 
 while x < p:
  limit = int( math.sqrt(x) )
  isprime = True;
  for pm in primes :
   if pm[0] > limit:
    break
   while pm[1] < x : 
    pm[1] += pm[0]
   if pm[1] == x : 
    isprime = False;
    break
  if isprime :
   primes.append([x, x]);
  x = x+2 
 
 psum = 0
 for a in primes:
  psum = psum + a[0]

 return primes, psum

 
