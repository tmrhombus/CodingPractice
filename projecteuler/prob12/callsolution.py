import solution as sol

# nd = minimum number of divisors solution must have
ndivreq = 4

lastdigit,solnum,primefactors,ndiv   = sol.solution( ndivreq )
  
print("\n\nThe sum 1+2+...+{} = {}, and has {} (> {})  divisors".format(lastdigit,solnum,ndiv,ndivreq))


print("\nThe prime factors are:")
for pf in primefactors:
 print("  {}^{}".format(pf,primefactors[pf]))

