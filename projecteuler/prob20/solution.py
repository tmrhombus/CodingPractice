
def solution( topnum ):
 """
 returns the sum of the digits in the factorial <topnum>!

 method:
 calculate the factorial
 then sum the digits
 """

 prod = factorial( topnum )
 sumdig = sumdigits( prod )

 return prod, sumdig


def factorial( n ):
 prod = 1
 for i in range(2,n+1):
  prod = prod*i

 return prod

def sumdigits(n):
 s = 0 
 while n:
  s += n % 10
  n //= 10
 return s
