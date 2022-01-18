import sys # write file
import gradientDescentFunctions as gdf
import numpy as np


# bgd.doit()

# get datafile
dataloc = "./data/"
outfileloc = "./outfiles/"
#datafile = bgd.importdata( dataloc+"twopoints.csv" )
#datafile = bgd.importdata( dataloc+"threepoints.csv" )
datafile = gdf.importdata( dataloc+"linear2d.csv" )


## initialize matrices
# X = design matrix = each row is the set of input values
# m rows because there are m training examples
# easy in this case b/c there's only one x input 
x1matrix = datafile.x
#x1matrix = np.asarray(datafile.x)

x0matrix = np.ones(x1matrix.size)
#xmatrix = np.array(datafile.x).T

xmatrix = np.vstack((x0matrix, x1matrix)).T 

# bmatrix = np.hstack((x0matrix.T, x1matrix.T))

#print(x1matrix.shape)
#print(" ")
#print(x1matrix)
#print(" ")
#
#print(x0matrix.shape)
#print(" ")
#print(x0matrix)
#print(" ")
## print(x1matrix.T)
#
#print("xmatrix")
#print(xmatrix.shape)
#print(" ")
#print(xmatrix)
#print(" ")

# 
# print("bmatrix")
# print(bmatrix.shape)
# print(" ")
# print(bmatrix)
# print(" ")

# Y = matrix of output values
# m rows because there are m training examples
ymatrix = datafile.y


tmatrix = gdf.solvefortheta(xmatrix, ymatrix)

print(tmatrix)

#  with open(outfileloc+"thetas{:02d}.csv".format(iterationnr), 'w') as f:
#   f.write("theta_0,theta_1\n")
#   f.write("{},{}".format(theta_0,theta_1))
#   #print("theta_0,theta_1")
#   #print("{},{}".format(theta_0,theta_1))
# 
# 
#  if ( abs(difftheta_0) < 0.01 and  abs(difftheta_1) < 0.01 ):
#   break 
# 
#  theta_0 = newtheta_0
#  theta_1 = newtheta_1
# 
#  iterationnr += 1
#  print("------------------")


