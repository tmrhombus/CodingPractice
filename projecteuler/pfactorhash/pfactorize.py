

def solution( target ):
 """
 returns all prime factors of target

 method:

 find A = lowest factor of target by checking 2,3,4,...
 split target into t = A*B 
  A is prime, add it to list of primes
  B becomes new target
   repeat iteraticely

  if we can not find any factors for target, we're done
 
 """

 pfactors = []

 while True:
  print("finding factor of {}".format(target))
  pfac = findminfactor( target )

  print("factor is: {}".format(pfac))

  print("list of pfactors: ")
  pfactors.append(int(pfac))
  print(pfactors)
  print("\n")
  
  if pfac != target:
   target = target/pfac
  else:
    break
 
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
   return i
  else:
    i = i+1  

 return x



