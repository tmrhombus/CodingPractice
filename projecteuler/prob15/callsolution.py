import solution as sol

vsteps = 2
hsteps = 2

nroutes = sol.solution( vsteps, hsteps )

print("The total number of routes for a {} by {} grid is {}".format(vsteps,hsteps,nroutes))
