
def solution( topnum ):
 """
 returns the sum of the digits in the factorial <topnum>!

 method:
 calculate the factorial
 then sum the digits
 """

 prod = -1
 sumdig = -1

 return prod, sumdig


def factorial( n ):
 prod = 1
 for i in range(2,n+1):
  prod = prod*i

 return prod
