
def solution( topnum ):
 """
 returns the set of amicable numbers less than <topnum>
 as well as their sum

 """

 i=60
# for i in range(2,topnum+1):
#  pfacs = pfactorize(i)
#  print(" i={}, facs={}".format(i,pfacs))

 pfacs = pfactorize(i)
 print(" i={}, facs={}".format(i,pfacs))
 
 prelist = [1]
 for j in pfacs:
  print("  j: {}".format(j))
  for k in range(1,pfacs.get(j)+1):

   fac = j**k
   print("   k={}, pfacs[{}]={},  fac={}".format( k, j, pfacs[j], fac ))
   prelist.append(j**k)

 print("prelist = {}".format(prelist))



 ans = []

 thesum = 0
 for an in ans:
  thesum += an

 return ans, thesum




def pfactorize( target ):
 """
 returns all prime factors of target in a hashset

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




