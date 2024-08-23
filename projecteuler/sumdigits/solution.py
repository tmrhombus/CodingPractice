
def solution( base, exp ):
 """
 returns the numerical value of <base>^<exp> 
 as well as the sum of the digits

 method:
 do the calculation directly
 """

 prod = base ** exp

 thesum = sumdigits(prod)

 return prod, thesum


def sumdigits(n):
 s = 0
 while n:
  s += n % 10
  n //= 10
 return s
