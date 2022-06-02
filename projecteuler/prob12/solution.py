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

 doprint = True

 lastdigit = 3
 solnum = 3 #triangle number 
 primefactors = []
 divisors = []
 
 solfound = False

 while True:

  if (solfound):
   break

  print("solnum = {}".format(solnum))


  solnum += lastdigit


 return lastdigit,solnum,primefactors,divisors

