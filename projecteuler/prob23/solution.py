
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
 3. loop through all combinations of abundants and 
    see what they add up to. 
 4. make list of bools, length <topnum>
 5. loop through pairs i,j of abundant numbers, set
    element i+j to true because it's a sum
 """
 
 # compute sum of proper divisors for each number
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

 
 # compute list of abundant numbers from divisorsum
 abundants = []
 # i = index (number)
 # j = value (sum of divisors for number i)
 for num,sumdiv in enumerate(divisorsum):
  # abundance definition
  if (num < sumdiv):
   #print("abundant i = {},  j = {}".format(num,sumdiv))
   abundants.append(num)

 #print(abundants)


 # make list of bools length topnum,
 # iniitlize as False, set element
 # i+j to true, for all pairs i,j in abundants
 isasum = [False]*topnum
 # loop through pairs of abundants
 for i in abundants:
  for j in abundants:

   if i+j<topnum:
    isasum[i+j]=True
  
 #print(isasum)

 # 
 nonexpressable = []
 for i in range(len(isasum)):
  print("i={}:  {}".format(i,isasum[i]))
  if not (isasum[i]):
   nonexpressable.append(i)

 #print(nonexpressable) 

 thesum = 0
 for ne in nonexpressable:
  thesum += ne

 return thesum,abundants,nonexpressable

