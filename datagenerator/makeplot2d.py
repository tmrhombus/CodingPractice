import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sb 

# Before clustering
# Simple script for plotting 2D data
  # in a scatter plot

infilebase = "./data/"
outfilebase = "./plots/"

datafilename = "doublegauss" 

infilename  = infilebase  + datafilename + ".csv"
outfilename = outfilebase + datafilename + ".png"

datafile = pd.read_csv(infilename)
#datafile = pd.read_csv(infilename, header=None)

sb.scatterplot(x=datafile.x, y=datafile.y)

#  # datafile.columns = ["Some Random X", "Some Random Y"]
#  # sb.scatterplot(x=datafile["Some Random X"], 
#  #                 y=datafile["Some Random Y"])
#  # 

plt.title("Scatterplot of X and Y")

plt.savefig(outfilename)



#  #    # # After clustering
#  #    # for x in range(0, 5):
#  #    #  plt.figure()
#  #    #  filebase = "./plots/outfile_"
#  #    #  pointsfilename = filebase + "points"+str(x)
#  #    #  centersfilename = filebase + "centers"+str(x)
#  # 
#  #  pointsdatafile = pd.read_csv(pointsfilename+".csv")
#  #  centersdatafile = pd.read_csv(centersfilename+".csv")
#  #  sb.scatterplot(x=pointsdatafile.x, y=pointsdatafile.y, 
#  #                  hue=pointsdatafile.c, 
#  #                  palette=sb.color_palette("hls", n_colors=2))
#  #  plt.title("Clustered: X vs Y")
#  #  
#  # #plt.show()

