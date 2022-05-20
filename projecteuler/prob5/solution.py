
def solution( b, t ):
 """

 returns the smallest number evenly divisible
 by all numbers from b to t (inclusive)

 method:

 Avoid double counting!

 Put all prime factors of i (b <= i <= t) in sets s_i
 Union of sets U(s_i) is evenly divisible by each i
 Smallest because no extra primes (smallest factors)
 
 """

 primelists = []
 for i in range(b,t+1):
  primelists.append( primefactors(i) )

 print(primelists)


 return [-1,-1,-1,-1]



def primefactors( x ):
 """
 returns a list of all prime factors of x
 """
 
 pfactors = []

 while True:
  pfac = findminfactor( x )

  pfactors.append(int(pfac))
  
  if pfac != x:
   x = x/pfac
  else:
    break
 
 return pfactors



def findminfactor( x ):
 """ 
 find first (prime) factor of x
 """

 i=2 
 while i<x:
  if x%i == 0:  
   return i
  else:
    i = i+1  

 return x






