#!/bin/python

import numpy as np

def sigmoid(z):
 return 1./(1+np.exp(-z))

def h_t_x(X, theta):
 return sigmoid( np.matmul(X,theta) )

def costFunction(theta, X, y):
 m = y.size

 # get theta into column matrix form
 arr_theta = np.array(theta)[np.newaxis]
 theta = arr_theta.T

 h = h_t_x(X, theta)

 J = float( (1/m) * \
            ( -np.matmul( y.T, np.log( h ) ) - \
              np.matmul( (1-y).T, np.log( 1-h ) ) ) )

 delJ = (1/m) * ( np.matmul ( X.T, (h-y) ) )

 return J,delJ

