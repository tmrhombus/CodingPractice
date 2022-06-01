import math 

def solution( ndivreq ):
 """
 For triangle number, tn = sum(1,2,...,n),
 finds the smallest tn which has more
 than <ndivreq> divisors

 method:
 check each next triangle number individually
 do this by finding prime factorization of tn
 the total number of primes (including duplicates)
  multiplies to tn, so every product of primes
  on the list is necessarily smaller than tn
 The each product of ps gives a unique number
  which is a factor of tn and this list of
  products is exhaustive
 Therefore the total number of factors of tn equals
  the total number of combinations of ps
 Check this against <ndivreq> 


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

  if (

  solnum += lastdigit


 return lastdigit,solnum,primefactors,divisors

