import solution as sol

# p = the desired perimeter of the triangle
p = 12

trips = sol.solution( p )
  
print("\n\nThe Pythagorean triplets that sum to {} are:".format(p))
for t in trips:
 print(" {}".format(t))

