#!/bin/python

import gradDescFunctions as gdf
import sys # write file

import numpy as np

dataloc    = "./data/"
outfileloc = "./outfiles/"

datafile = gdf.importdata( dataloc+"ng_housing3d.csv" )
#datafile = gdf.importdata( dataloc+"ng_foodcarts2d.csv" )

## initialize matrices
# X = design matrix = each row is the set of input values
# m rows because there are m training examples
# easy in this case b/c there's only one x input 
x1matrix = datafile.x1
x2matrix = datafile.x2

x0matrix = np.ones(x1matrix.size)

xamatrix = np.vstack((x0matrix, x1matrix))
xmatrix = np.vstack((xamatrix, x2matrix)).T

#xmatrix = np.vstack((x0matrix, x1matrix)).T 

#print("xmatrix")
#print(xmatrix)

nXrows, nXcols = xmatrix.shape
#print("rows {}, cols {}".format(nXrows,nXcols))


# Y = matrix of output values
# m rows because there are m training examples
ymatrix = datafile.y.to_numpy()

#print("\n\nymatrix")
#print(ymatrix)

## Theta = matrix of parameters
thetamatrix = np.zeros(nXcols)
#print("\n\nthetamatrix")
#print(thetamatrix)

iterations = 2
alpha = 0.01

gdf.computeCost(xmatrix, ymatrix, thetamatrix)

thetamatrix, J_history = gdf.gradientDescent( xmatrix, ymatrix,
                  thetamatrix, alpha, iterations)


print("Theta's found by gradient descent: ({},{})".format(thetamatrix[0],thetamatrix[1]))

#print("J_history: ")
#print(J_history)



