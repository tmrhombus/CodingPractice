
def solution( vsteps, hsteps ):
 """
 returns the total number of possible routes
 on a grid of dimensions <vsteps> x <hsteps>

 method: 
 This is the total number of combinations of
 (identical) v and h steps.
 There are <vsteps>+<hsteps> choose <vsteps>
 such combinations.
 """

 
 nroutes = binomial( vsteps+hsteps, vsteps  )


 return nroutes

def binomial(n,k):

 tot = factorial(n) / ( factorial(k) * factorial(n-k) )
 
 return tot


def factorial(x):
 tot = 1
 for i in range(2,x+1):
  tot *= i

 return tot
