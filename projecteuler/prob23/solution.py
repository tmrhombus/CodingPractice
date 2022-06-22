
def solution(topnum):
 """
 returns the sum of all integers less
 than <topnum>  which can not be expressed
 as the sum of two abundant numbers

 method:
 1. make an array of the sum of divisors as in prob21
    divisorsum[j] corresponds to sum of divisors of j
 2. select from this an array of abundant numbers:
    if divisorsum[j] > j, j is abundant
 """
 
 # Compute sum of proper divisors for each number
 # make array of zeros of length <topnum>
 divisorsum = [0] * topnum
 # loop through i = 1 to <topnum>
 for i in range(1, topnum):
  # for each i, increment j as multiples of i
  # up to <topnum>. Don't include i itself
  # because i is not a "proper" divisor of i 
  for j in range(i * 2, topnum, i): 
   # j is a multiple of i, so i is a divisor of j
   # add i to the divisor sum at index j
   divisorsum[j] += i

 
 abundants = {}
 for i,j in enumerate(divisorsum):
  print("i = {},  j = {}".format(i,j))
 



 thesum = 0

 return thesum

