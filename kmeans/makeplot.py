import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sb 

filebase = "./plots/outfile_"

nplots=10
ncolors=4

# Before clustering
datafile = pd.read_csv("fourgauss.csv", header=None)
datafile.columns = ["Some Random X", "Some Random Y"]
sb.scatterplot(x=datafile["Some Random X"], 
                y=datafile["Some Random Y"])
plt.title("Initial Plot of X and Y")
plt.xlim([-80, 120])
plt.ylim([-40, 80])
plt.savefig(filebase+"initialdata.png")

# After clustering
for x in range(0, nplots):
 plt.figure()
 pointsfilename = filebase + "points"+str(x)
 centersfilename = filebase + "centers"+str(x)
 #outfilename = filebase + "plot_" + str(x) + ".png"
 outfilename = filebase + "plot_" + "{:02d}".format(x) + ".png"

 pointsdatafile = pd.read_csv(pointsfilename+".csv")
 centersdatafile = pd.read_csv(centersfilename+".csv")
 sb.scatterplot(x=pointsdatafile.x, y=pointsdatafile.y, 
                 hue=pointsdatafile.c, 
                 palette=sb.color_palette("hls", n_colors=ncolors))
 sb.scatterplot(x=centersdatafile.x, y=centersdatafile.y, 
                 color="black")
 plt.xlabel("Some Random X")
 plt.ylabel("Some Random Y")
 plt.xlim([-80, 120])
 plt.ylim([-40, 80])
 plt.title("Clustering - k Means")
 plt.savefig(outfilename)
 
#plt.show()

# colored plot with no centers
x=nplots
plt.figure()
pointsfilename = filebase + "points"+str(x)
outfilename = filebase + "plot_" + str(x) + ".png"

pointsdatafile = pd.read_csv(pointsfilename+".csv")
sb.scatterplot(x=pointsdatafile.x, y=pointsdatafile.y, 
                hue=pointsdatafile.c, 
                palette=sb.color_palette("hls", n_colors=ncolors))
plt.xlabel("Some Random X")
plt.ylabel("Some Random Y")
plt.xlim([-80, 120])
plt.ylim([-40, 80])
plt.title("Clustered - k Means")
plt.savefig(outfilename)
 

