
def solution( n ):
 """

 returns a list of the first n prime numbers

 method:

 Incremental Sieve of Eratosthenes  

 store list of primes and multiple of primes
 loop over numbers [n]
  loop over primes [p]
   find first multiple of p that's larger than n
   if a multiple of p equals n, go to next n
  if you go through all primes and haven't found a multiple
   add n to list of primes

 """

 doprint = True

 primelist = []

 return primelist
