
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb



def doit():
 print(" hi ")


 # # Define a function `plus()`
 # def plus(a,b):
 #   return a + b
 #   
 # # Create a `Summation` class
 # class Summation(object):
 #   def sum(self, a, b):
 #     self.contents = a + b
 #     return self.contents 




def importdata( filename ):
 datafile = pd.read_csv( filename )
 return datafile
