import solution as sol


ns = [10,100]

for n in ns: 
 
 ans1, ans2  = sol.solution( n )
  
 print("\n\nThe difference between the square of the sum and the sum of squares in the range from 1 to {} is {} = {} \n\n".format(n, ans1, ans2))
  
