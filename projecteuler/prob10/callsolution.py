import solution as sol

# m = max value for primes
p = 10

primes,psum = sol.solution( p )
  
print("\n\nThe sum of all primes less than {} is {}".format(p, psum))

print("The primes themselves are:")
for a in primes:
 print(" {}".format(a))
