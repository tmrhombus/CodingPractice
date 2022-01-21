#!/bin/python

import gradDescFunctions as gdf
import sys # write file

import numpy as np

dataloc    = "./data/"
outfileloc = "./outfiles/"

datafile = gdf.importdata( dataloc+"ng_foodcarts2d.csv" )

## initialize matrices
# X = design matrix = each row is the set of input values
# m rows because there are m training examples
# easy in this case b/c there's only one x input 
x1matrix = datafile.x
#x1matrix = np.asarray(datafile.x)

x0matrix = np.ones(x1matrix.size)
#xmatrix = np.array(datafile.x).T

xmatrix = np.vstack((x0matrix, x1matrix)).T 

#print("xmatrix")
#print(xmatrix)


# Y = matrix of output values
# m rows because there are m training examples
ymatrix = datafile.y.to_numpy()

#print("\n\nymatrix")
#print(ymatrix)

## Theta = matrix of parameters
thetamatrix = np.zeros(2)
#print("\n\nthetamatrix")
#print(thetamatrix)

iterations = 15
#iterations = 1500
alpha = 0.01

gdf.computeCost(xmatrix, ymatrix, thetamatrix)

thetamatrix, J_history = gdf.gradientDescent( xmatrix, ymatrix,
                  thetamatrix, alpha, iterations)



