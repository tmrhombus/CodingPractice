
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

 doprint = True

 # Fill list of lists of primes
 primelists = []
 for i in range(b,t+1):
  if(doprint):
   print("Writing primes for {}".format(i))
  primelists.append( primefactors(i) )

 if(doprint):
  print("Original primelist")
  print(primelists)

  print("")
 
 minintersect = []

 for i in range(len(primelists)):
  if(doprint):
   print("Prime lists: {}".format(primelists))
   print("Min instersect: {}".format(minintersect))
   print(" Prime list i = {}:  {}".format(i,primelists[i])) 
  for j in range(len(primelists[i])):
   p = primelists[i][j]
   if(doprint):
    print("    {}".format(p))
   minintersect.append( p )
   for k in range(i,len(primelists)):
    if len(primelists[k])>0:
     if(doprint):
      print(" {}".format(primelists[k][0]) )
     if (primelists[k][0] == p):
      primelists[k].pop(0)
     
    
 product = 1
 for m in minintersect:
  product = product*m

 return minintersect, product



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

