import math 

def solution( n, x ):
 """

 finds and returns the string of n digits in x
 which multiply to give the greatest product

 method:
 brute force: sliding window 15 wide, check them all

 """

 # cast x to a string for easy indexing
 strx = str(x) 

 bestdig = []
 bestprod = -1
 for i in range( len(strx)-n+1 ):
  digits = []
  prod = 1
  for j in range( n ):
   digits.append(int(strx[i+j]))
   prod = prod * int(strx[i+j])
  
  #print("------------")
  #print(digits)
  #print(prod)
  #print(bestprod)
  if prod > bestprod:
   bestprod = prod
   bestdig = digits

 return bestdig, bestprod
