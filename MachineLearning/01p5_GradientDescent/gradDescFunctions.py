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

 #print(type(X)    ) 
 #print(type(y)    ) 
 #print(type(theta))  
 m = y.size
 J = 0
 #print(m)

 #print(X.shape)
 #print(y.shape)
 #print(theta.shape)

 # h minus y
 #hmy = (np.matmul(theta,X.T) - y) 
 #print( (np.matmul(theta,X.T) - y) )
 hmy = hminusy(X,y,theta)
 #print( hmy )

 thesum =  np.matmul(hmy,hmy)
 J = 1/(2*m) * thesum
 #print(J)

 return J

def gradientDescent( X, y, theta, alpha, num_iters ):
 m = y.size

 J_history = np.zeros(num_iters)

 for itnr in range(0, num_iters):
  print(itnr)
  hmy = hminusy(X,y,theta)

  theta = theta - (alpha/m)*np.matmul(hmy,X)

  J_history[itnr] = computeCost(X,y,theta)

 return theta, J_history
 # theta = theta - (alpha/m)*X''*(X*theta - y)

 #J_history(itnr) = computeCost(X, Y, theta)



