import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sb 

# Before clustering
# Simple script for plotting 2D data
  # in a scatter plot

infilebase = "./data/"
outfilebase = "./plots/"

datafilename = "ng_foodcarts2d" 

infilename  = infilebase  + datafilename + ".csv"
outfilename = outfilebase + datafilename + ".png"

datafile = pd.read_csv(infilename)
#datafile = pd.read_csv(infilename, header=None)


xcolname = "Population of City, in 10,000s"
ycolname = "Profit in $10,000s"
datafile.columns = [xcolname, ycolname]

#sb.scatterplot(x=datafile.x, y=datafile.y)
sb.scatterplot(x=datafile[xcolname], 
               y=datafile[ycolname])

plt.title("Training Data: Profit for Food Truck v. City Size")


plt.savefig(outfilename)

