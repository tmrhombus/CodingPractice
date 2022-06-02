import math 

def solution( ndivreq ):
 """
 For triangle number, tn = sum(1,2,...,n),
 finds the smallest tn which has more
 than <ndivreq> divisors

 Overall Method:
 Check each next triangle number individually
 Do this by finding prime factorization of tn
 The total number of primes (including duplicates)
  multiplies to tn, so every product of primes
  on the list is necessarily smaller than tn
 The each product of ps gives a unique number
  which is a factor of tn and this list of
  products is exhaustive
 Therefore the total number of factors of tn equals
  the total number of combinations of ps
 Check this against <ndivreq> 

 Counting number of factors:
 Each unique prime factor can appear in the 
  overall product with 0,1,...,m copies
  where m is the multiplicity of that p-factor
 This gives m+1 options for each prime
 Total number of unique factors will be 
  Product(m+1) for each m in the list
 

 """

 doprint = False

 lastdigit = 2
 solnum = 3 #triangle number 
 
 while True:

  if(doprint):
   print("\nlast digit: {}, solnum: {}".format(lastdigit,solnum))

  primefactors = pfactorize( solnum )
  
  if(doprint):
   print(" prime factors: {}".format(primefactors))

  ndiv = 1
  for prime in primefactors:
   ndiv *= ( primefactors[prime] + 1 )

  if(doprint):
   print("  number divisors: {}".format(ndiv))

  if(ndiv>ndivreq):
   break

  lastdigit += 1
  solnum += lastdigit

 return lastdigit,solnum,primefactors,ndiv


def pfactorize( target ):
 """ 
 returns all prime factors of target
 in a hashset

 method:

 find A = lowest prime factor of target by checking 2,3,4,...
 split target into t = A*B 
  A is prime, add it to list of primes
  B becomes new target
   repeat iteraticely

  if we can not find any factors for target, we're done
 
 """

 doprint = False

 pfactors = {}

 while True:
  if(doprint):
   print("finding factor of {}".format(target))
  pfac = findminfactor( target )

  if(doprint):
   print("factor is: {}".format(pfac))

  if pfac in pfactors: 
   pfactors[pfac] += 1
  else :
   pfactors.update({pfac:1})

  if(doprint):
   print("list of pfactors: ")
   #pfactors.append(int(pfac))
   print(pfactors)
   print("\n")
  
  if pfac != target:
   target = target/pfac
  else:
    break

 
 if(doprint):
  print("Done!")
  print("List of factors: ")
  print(pfactors)
  print("\n")

 return pfactors


def findminfactor( x ):
 """
 find first factor of x
 """

 i=2
 while i<x:
  if x%i == 0:
   return int(i)
  else:
   if i==2:
    i = i+1
   else:
    i = i+2

 return int(x)


