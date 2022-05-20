import solution as sol

b = 1
t = 20

s,p = sol.solution( b, t )
 
print("\n\nThe smallest number that is divisible by all integers in the range from {} to {} is {}".format(b, t, p))
 
print("It has a prime factorization of {}".format(s)) 


#l = sol.primefactors( 150 )
#print(l)
