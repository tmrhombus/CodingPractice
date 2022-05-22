import solution as sol

 
# n = number of primes to list
n = 5

ans = sol.solution( n )
  
print("\n\nPrime number number  {} is {} \n\n".format(n, ans[-1]))

print("The full list of primes is:")
for p in ans:
 print(" {}".format(p))
  
