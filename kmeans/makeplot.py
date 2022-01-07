import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sb 

# Before clustering
datafile = pd.read_csv("twoblobs.csv", header=None)
datafile.columns = ["Some Random X", "Some Random Y"]
sb.scatterplot(x=datafile["Some Random X"], 
                y=datafile["Some Random Y"])
plt.title("Scatterplot of X and Y")

# After clustering
for x in range(0, 4):
 plt.figure()
 filebase = "./plots/outfile_"
 pointsfilename = filebase + "points"+str(x)
 centersfilename = filebase + "centers"+str(x)
 outfilename = filebase + "plot_" + str(x) + ".png"

 pointsdatafile = pd.read_csv(pointsfilename+".csv")
 centersdatafile = pd.read_csv(centersfilename+".csv")
 sb.scatterplot(x=pointsdatafile.x, y=pointsdatafile.y, 
                 hue=pointsdatafile.c, 
                 palette=sb.color_palette("hls", n_colors=2))
 sb.scatterplot(x=centersdatafile.x, y=centersdatafile.y, 
                 color="black")
 plt.xlabel("Some Random X")
 plt.ylabel("Some Random Y")
 plt.title("Clustered: X vs Y")
 plt.savefig(outfilename)
 
#plt.show()

