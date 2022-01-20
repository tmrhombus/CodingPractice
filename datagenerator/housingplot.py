import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sb 

# Before clustering
# Simple script for plotting 2D data
  # in a scatter plot

infilebase = "./data/"
outfilebase = "./plots/"

datafilename = "ng_housing3d" 

infilename  = infilebase  + datafilename + ".csv"
outfilename = outfilebase + datafilename + ".png"

datafile = pd.read_csv(infilename)
#datafile = pd.read_csv(infilename, header=None)


xcolname = "House Size (sq ft)"
ycolname = "Nr. Bedrooms"
zcolname = "House Price"
datafile.columns = [xcolname, ycolname, zcolname]

# Creating figure
fig = plt.figure(figsize = (10, 7))
ax = plt.axes(projection ="3d")
 
# Creating plot
ax.scatter3D(datafile[xcolname],
             datafile[ycolname],
             datafile[zcolname], color = "green")

##sb.scatterplot(x=datafile.x, y=datafile.y)
#sb.scatterplot(x=datafile[xcolname], 
#               y=datafile[ycolname],
#               z=datafile[zcolname])

plt.title("Training Data: Housing Prices in Portland")


#plt.show()
plt.savefig(outfilename)

