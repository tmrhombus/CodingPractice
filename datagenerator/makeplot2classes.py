import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sb 

# Before clustering
# Simple script for plotting 2D data
  # in a scatter plot

infilebase = "./data/"
outfilebase = "./plots/"

datafilename = "twogaussclasses" 

infilename  = infilebase  + datafilename + ".csv"
outfilename = outfilebase + datafilename + ".png"

datafile = pd.read_csv(infilename)
#datafile = pd.read_csv(infilename, header=None)

sb.scatterplot(x=datafile.x, y=datafile.y, hue=datafile.z)

plt.title("Scatterplot of X and Y")

plt.savefig(outfilename)

