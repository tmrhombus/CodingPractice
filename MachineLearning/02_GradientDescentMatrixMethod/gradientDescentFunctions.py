
import pandas as pd
import numpy as np


# import file
def importdata( filename ):
 datafile = pd.read_csv( filename )
 return datafile


def solvefortheta(X, Y):
 # analyically we can solve for theta
 # as TH = (Xt X)^-1 Xt y
 #print(X)
 #print(X.shape)
 #print("\n")
 #print(Y)
 #print(Y.shape)
 return np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)),X.T),Y)

 # print(np.dot(X.T, X))
 # print(np.dot(X.T, X).shape)

 
 
 #print(np.linalg.inv(np.dot(X, X.T)))

 #return 1

 
