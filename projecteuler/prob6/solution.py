
def solution( n ):
 """
 returns the difference between the sum of the squares
 and the square of the sum of all numbers in range
 from b to t
 method:
 A: 
 just compute them, nothing special
 B: Faulhaber's formula
    Sum (k)   from 1 to n = n(n+1)/2
    Sum (k^2) from 1 to n = n(n+1)(2n+1)/6
 
 """

 doprint = False

 # Method A
 a = 0
 a2 = 0
 for i in range(1,n+1):
  a  = a + i
  a2 = a2 + i**2

 sum2a = a**2
 if(doprint):
  print(sum2a)
  print(a2)
 diff1 = sum2a - a2

 # Method B
 sumk  = n*(n+1) / 2
 sum2k = sumk**2
 sumk2 = n*(n+1)*(2*n+1)/6

 diff2 = sum2k - sumk2

 return diff1, diff2
