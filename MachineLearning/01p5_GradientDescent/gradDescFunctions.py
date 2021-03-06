#!/bin/python

import pandas as pd
import numpy as np

# import file
def importdata( filename ):
 datafile = pd.read_csv( filename )
 return datafile

def hminusy(X, y, theta):
 hmy = (np.matmul(theta,X.T) - y) 
 return hmy

def computeCost( X, y, theta ):
 #m = length(y) # number of training examples

 m = y.size
 J = 0
 #print(m)

 #print(X.shape)
 #print(y.shape)
 #print(theta.shape)

 # h minus y
 hmy = hminusy(X,y,theta)
 #print( hmy )

 thesum =  np.matmul(hmy,hmy)
 J = 1/(2*m) * thesum
 #print(J)

 return J

def featureNormalize(X):
 #X_norm = X
 #nXrows, nXcols = X.shape

 # print("X")
 # print(X)
 # axis=0 for columns
 mu  = X.mean(axis=0)
 std = X.std(axis=0)
 # print("mu")
 # print(mu)
 # print("std")
 # print(std)
 mu[0]  = 0
 std[0] = 1
 # print("mu")
 # print(mu)
 # print("std")
 # print(std)
 # broadcasting, subtract mean from X
 X_norm = X - mu
 X_norm = X_norm/std
 # print("X_norm")
 # print(X_norm)
 return X_norm, mu, std


def makeDataMatrix(X,y):
 xdata = np.delete(X,0,1)
 print(xdata.shape)
 print(y.shape)
 combined = np.hstack((xdata,y.reshape(y.size,1)))
 #return xdata
 return combined

def gradientDescent( X, y, theta, alpha, num_iters ):
 m = y.size
 outfileloc = "./output/"

 J_history = np.zeros(num_iters)

 #for itnr in range(0, num_iters):
 itnr = 1
 #with open(outfileloc+"thetas{:04d}.csv".format(itnr), 'w') as f:
 with open(outfileloc+"thetas_{}.csv".format(alpha), 'w') as tfile:
  with open(outfileloc+"Js_{}.csv".format(alpha), 'w') as jfile: 
   tfile.write("theta_0,theta_1,itnr\n")
   tfile.write("0,0,0\n")
   jfile.write("J,itnr\n")
   jfile.write("0,0\n")
   while(True):
    if(itnr >= num_iters): break
    #print(itnr)

    hmy = hminusy(X,y,theta)

#    print("HminusY : ")
#    print(hmy)
#    print("\n\n")
#    print("X")
#    print(X)
#    print("\n\n")

    theta = theta - (alpha/m)*np.matmul(hmy,X)

    J_history[itnr] = computeCost(X,y,theta)

    tfile.write("{},{},{}\n".format(theta[0],theta[1],itnr))
    jfile.write("{},{}\n".format(J_history[itnr], itnr))
    #print("theta_0,theta_1")
    #print("{},{}".format(theta_0,theta_1))

    # convergence
    if(abs(J_history[itnr] - J_history[itnr-1]) < 0.0001): 
     print("Converged at iteration: {}".format(itnr))
     #break

    itnr += 1


 #return [1,1], [2,2]
 return theta, J_history
