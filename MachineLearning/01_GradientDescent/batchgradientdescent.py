
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sb


def importdata( filename ):
 datafile = pd.read_csv( filename )
 return datafile

def hfunction( theta0, theta1, x ):
 return theta0 + theta1*x

def Jfunction( t0, t1, x, y):
 J = 0
 for i in range(len(x)):
  J += ( t0 + t1*x[i] - y[i] )**2
 return J

def gradientdescent(alpha, x, y, convergencecond=0.01, maxiter=10000, outfileloc="./outfiles/"):
 converged = False
 iterationnr = 0
 m = len(x) # number of samples
 # print(m)

 # initialize thetas
 theta_0 = 0 
 theta_1 = 0  

 J = Jfunction( theta_0, theta_1, x, y)
 # print(J)

 while True:
  if iterationnr > maxiter: break
  print("Iteration: "+str(iterationnr))
  print("theta_0: "+str(theta_0))
  print("theta_1: "+str(theta_1))

  # # for each training sample, compute the gradient (d/d_theta j(theta))
  derivativeJ_0 = 1.0/m * sum([ (hfunction(theta_0, theta_1, x[i]) - y[i] ) for i in range(m) ])
  derivativeJ_1 = 1.0/m * sum([ (hfunction(theta_0, theta_1, x[i]) - y[i] )*x[i] for i in range(m) ])

  update_0 = alpha*derivativeJ_0
  update_1 = alpha*derivativeJ_1
 
  print("update_0: "+str(update_0))
  print("update_1: "+str(update_1))
 
  newtheta_0 = theta_0 - update_0
  newtheta_1 = theta_1 - update_1
 
  print("newtheta_0: "+str(newtheta_0))
  print("newtheta_1: "+str(newtheta_1))

  difftheta_0 = newtheta_0 - theta_0
  difftheta_1 = newtheta_1 - theta_1

  theta_0 = newtheta_0
  theta_1 = newtheta_1

  with open(outfileloc+"thetas{:04d}.csv".format(iterationnr), 'w') as f:
   f.write("theta_0,theta_1\n")
   f.write("{},{}".format(theta_0,theta_1))
   #print("theta_0,theta_1")
   #print("{},{}".format(theta_0,theta_1))


  if ( abs(difftheta_0) < 0.01 and  abs(difftheta_1) < 0.01 ):
   break 


  # mean squared error
  error = Jfunction( theta_0, theta_1, x, y )

  if abs(J-error) <= convergencecond:
   break

  J = error   # update error 

  iterationnr += 1 

 return theta_0, theta_1








