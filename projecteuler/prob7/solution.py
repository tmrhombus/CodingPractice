import math 

def solution( n ):
 """

 returns a list of the first n prime numbers

 method:

 Incremental Sieve of Eratosthenes  

 store list of primes and multiple of primes
 loop over numbers [x]
  loop over primes [p]
   find first multiple of p that's larger than x
   if a multiple of p equals x, go to next x
  if you go through all primes and haven't found a multiple
   add x to list of primes

 """

 primes = [ [2, 2] ]
 
 x=3
 while len(primes) < n:
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
 
 return primes
