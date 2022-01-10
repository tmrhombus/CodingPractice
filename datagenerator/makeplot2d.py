import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sb 

# Before clustering
# Simple script for plotting 2D data
  # in a scatter plot

infilebase = "./data/"
outfilebase = "./plots/"

#datafilename = "linear2d" 
#datafilename = "singlegauss" 
#datafilename = "doublegauss" 
#datafilename = "triplegauss" 
#datafilename = "quadgauss" 
#datafilename = "gauss"
#datafilename = "twogauss"
#datafilename = "threegauss"
#datafilename = "fourgauss"
datafilename = "fivegauss" 

infilename  = infilebase  + datafilename + ".csv"
outfilename = outfilebase + datafilename + ".png"

datafile = pd.read_csv(infilename)
#datafile = pd.read_csv(infilename, header=None)

sb.scatterplot(x=datafile.x, y=datafile.y)

plt.title("Scatterplot of X and Y")

plt.savefig(outfilename)

