
def solution( topnum ):
 """
 returns the set of amicable numbers less than <topnum>
 as well as their sum

 method:
 make an array of the sums of divisors
 search that array for amicable pairs
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

 #print("divisor sums: ")
 #for k in range(topnum):
  #print(" k={}, sum={}".format(k,divisorsum[k]))

 # Find all amicable pairs within range
 ans = []
 thesum = 0
 for i in range(1, topnum):
  j = divisorsum[i]
  if j != i and j < topnum and divisorsum[j] == i:
   thesum += i
   ans.append([i,j])

 return ans, thesum
