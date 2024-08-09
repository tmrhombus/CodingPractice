#!/bin/python

import logRegFunctions as lrf
import sys # write file
import pandas as pd

import numpy as np

import scipy.optimize as opt

dataloc    = "./data/"
outfileloc = "./outfiles/"

data = pd.read_csv(dataloc+"ng_microchips.csv", header=None)

## initialize matrices 
######################
X = data.iloc[:,:2].to_numpy()  #(100,2)
y = data.iloc[:,2:3].to_numpy() #(100,1)

## other ways that work
#X1 = data.values[:,:2]
#y1 = data.values[:,2:3]
#X2,y2 = np.split(data, [2], axis=1)
#X2 = X2.to_numpy()
#y2 = y2.to_numpy()

## test mapfeatures function--------
#a1 = np.array((2,2,2,2))
#a2 = np.array((3,3,3,3))
##print(a1)
##print(a2)
#test = lrf.mapfeatures(6, a1, a2)

X = lrf.mapfeatures(6, X[:,0], X[:,1])

# get dimensions of X matrix
nXrows, nXcols = X.shape

# add ones column for X_0 - already done in mapfeatures
#onescolforX = np.ones((nXrows,1))
#X = np.append(onescolforX, X, axis=1) #(100,3)
#print(X)
#print(X.shape)

# initialize theta matrix as zeros
theta = np.zeros((nXcols)) # [0, 0, 0], shape (3,)
print(theta)
print(theta.shape)

#### test that cost/gradient function is working
########################
J,delJ = lrf.costFunctionReg(theta, X, y, 1)
print('Cost at initial theta (zeros):', J)
print('Expected cost (approx): 0.693\n')

##test_theta = [-24,0.2,0.2] #
##J,delJ = lrf.costFunction(test_theta, X, y)
##print('\nCost at test theta: \n', J)
##print('Expected cost (approx): 0.218\n')
##print('Gradient at test theta: \n',delJ);
##print('Expected gradients (approx):\n 0.043\n 2.566\n 2.647\n')
##
##test_theta1 = [-25.161, 0.206, 0.201]
##J,delJ = lrf.costFunction(test_theta1, X, y)
##print('\nCost at test theta: \n', J)
##print('Expected cost (approx): 0.203\n')
#
#
#
## do the optimization to find the best thetas
######################
lam = 1
result = opt.fmin_tnc(func=lrf.costFunctionReg, x0=theta, args=(X, y, lam))

print("\n\n")
print("Result: ")
print(result)
print("\n")

print('theta: \n',result[0]);
print("finished in {} steps\n\n".format(result[1]))

finalthetas = result[0]


### Predict if a given test score combo is accepted
#######################
#exam1 = 45
#exam2 = 85
#
#studentX = np.array((1, exam1, exam2))
#prediction = lrf.h_t_x(studentX, finalthetas)
#print("For a student with a")
#print(" {} on Exam 1".format(exam1))
#print(" {} on Exam 2".format(exam2))
#print("Likelihood of admittance is: {}".format(prediction))
#print("[[ should be 0.776 ]]\n\n")
#
#
### How well does the model predict our data
#######################
#fulldatasetprediction = lrf.h_t_x(X, finalthetas)
#roundedfullprediction = np.round(fulldatasetprediction,0)
#
#ngood = 0
#nbad  = 0
#ntot  = 0
#for p,a in zip(roundedfullprediction,y):
# #print(" P: {}, A: {}".format(int(p),int(a)))
# ntot += 1
# if(int(p) == int(a)):
#  ngood += 1
# else:
#  nbad += 1
#
#print("Good: {}, Bad: {}, Tot: {}".format(ngood, nbad, ntot))
#print("Training accuracy = {}%".format(100.*ngood/ntot))
#
#




