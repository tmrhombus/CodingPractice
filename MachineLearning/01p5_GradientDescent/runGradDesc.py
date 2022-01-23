#!/bin/python

import gradDescFunctions as gdf
import sys # write file

import numpy as np

dataloc    = "./data/"
outfileloc = "./outfiles/"

#datafile = gdf.importdata( dataloc+"ng_housing3d.csv" )
datafile = gdf.importdata( dataloc+"ng_foodcarts2d.csv" )

## initialize matrices
# X = design matrix = each row is the set of input values
# m rows because there are m training examples
# easy in this case b/c there's only one x input 
x1matrix = datafile.x1
#x2matrix = datafile.x2

x0matrix = np.ones(x1matrix.size)

#xamatrix = np.vstack((x0matrix, x1matrix))
#xmatrix = np.vstack((xamatrix, x2matrix)).T

xmatrix = np.vstack((x0matrix, x1matrix)).T 

#print("xmatrix")
#print(xmatrix)

nXrows, nXcols = xmatrix.shape
#print("rows {}, cols {}".format(nXrows,nXcols))

Xn, mu, std = gdf.featureNormalize(xmatrix)
print ("mu:    {}".format(mu))
print ("sigma: {}".format(std)) 

# Y = matrix of output values
# m rows because there are m training examples
ymatrix = datafile.y.to_numpy()

#print("\n\nymatrix")
#print(ymatrix)

## Theta = matrix of parameters
thetamatrix = np.zeros(nXcols)
#print("\n\nthetamatrix")
#print(thetamatrix)

scaleddata = gdf.makeDataMatrix(Xn, ymatrix)
np.savetxt("./output/data_renormed.csv",scaleddata,delimiter=',')




iterations = 6000
alpha = 0.003

gdf.computeCost(xmatrix, ymatrix, thetamatrix)

#print(xmatrix)
#print(Xn)
#print(mu)
#print(std)

#reconst = Xn * std
#reconst = reconst + mu
#
#print(reconst)

#thetamatrix, J_history = gdf.gradientDescent( xmatrix, ymatrix,
thetamatrix, J_history = gdf.gradientDescent( Xn, ymatrix,
                  thetamatrix, alpha, iterations)


print(thetamatrix)
#print("Theta's found by gradient descent: ({},{},{})".format(thetamatrix[0],thetamatrix[1],thetamatrix[2]))

#print("J_history: ")
#print(J_history)



