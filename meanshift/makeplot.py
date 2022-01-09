import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sb 

filebase = "./plots/outfile_"

# Before clustering
inputpointfile = pd.read_csv("./data/triplegauss.csv", header=None)
inputpointfile.columns = ["Some Random X", "Some Random Y"]
sb.scatterplot(x=inputpointfile["Some Random X"], 
                y=inputpointfile["Some Random Y"])
plt.title("Scatterplot of X and Y")
plt.xlim([-20, 130])
plt.ylim([-20, 100])
plt.savefig(filebase+"initialdata.png")

# Now add centers
for x in range(0, 12):
 plt.figure()
 # print()"{:02d}".format(1)
 pointsfilename = filebase + "points0"
 centersfilename = filebase + "centers"+str(x)
 outfilename = filebase + "plot_" + "{:02d}".format(x) + ".png"
 
 
 pointsdatafile = pd.read_csv(pointsfilename+".csv")
 centersdatafile = pd.read_csv(centersfilename+".csv")
 # sb.scatterplot(x=pointsdatafile.x, y=pointsdatafile.y, 
 #                 hue=pointsdatafile.c, 
 #                 palette=sb.color_palette("hls", n_colors=2))
 sb.scatterplot(x=pointsdatafile.x, y=pointsdatafile.y, 
                color="black")
 sb.scatterplot(x=centersdatafile.x, y=centersdatafile.y, 
                 color="red")


 # put circles around center points  
 df = pd.read_csv(centersfilename+".csv")
 for i in range(len(df)):
  # print(df.values[i][0]) 
  # print(df.values[i][1]) 
  #mycirc = plt.Circle((20, 20), 5, color='g', fill=False)
  mycirc = plt.Circle((df.values[i][0], df.values[i][1]), 15, color='r', fill=False)
  plt.gca().add_patch(mycirc)

 plt.xlabel("Some Random X")
 plt.ylabel("Some Random Y")
 plt.title("Clustered: X vs Y")
 plt.xlim([-20, 130])
 plt.ylim([-20, 100])
 plt.savefig(outfilename)
 plt.clf()
 plt.close()


# now a colored plot with centers
x=12
plt.figure()
# print()"{:02d}".format(1)
pointsfilename = filebase + "points0"
centersfilename = filebase + "centers"+str(x)
outfilename = filebase + "plot_" + "{:02d}".format(x) + "_color.png"


pointsdatafile = pd.read_csv(pointsfilename+".csv")
centersdatafile = pd.read_csv(centersfilename+".csv")
sb.scatterplot(x=pointsdatafile.x, y=pointsdatafile.y, 
                hue=pointsdatafile.c, 
                palette=sb.color_palette("hls", n_colors=3))
# sb.scatterplot(x=pointsdatafile.x, y=pointsdatafile.y, 
#                color="black")
sb.scatterplot(x=centersdatafile.x, y=centersdatafile.y, 
                color="red")


# put circles around center points  
df = pd.read_csv(centersfilename+".csv")
for i in range(len(df)):
 # print(df.values[i][0]) 
 # print(df.values[i][1]) 
 #mycirc = plt.Circle((20, 20), 5, color='g', fill=False)
 mycirc = plt.Circle((df.values[i][0], df.values[i][1]), 15, color='r', fill=False)
 plt.gca().add_patch(mycirc)

plt.xlabel("Some Random X")
plt.ylabel("Some Random Y")
plt.title("Clustered: X vs Y")
plt.xlim([-20, 130])
plt.ylim([-20, 100])
plt.savefig(outfilename)
plt.close()


# now a colored plot with no centers
x=12
plt.figure()
# print()"{:02d}".format(1)
pointsfilename = filebase + "points0"
outfilename = filebase + "plot_" + "{:02d}".format(x) + "_colorNOC.png"


pointsdatafile = pd.read_csv(pointsfilename+".csv")
sb.scatterplot(x=pointsdatafile.x, y=pointsdatafile.y, 
                hue=pointsdatafile.c, 
                palette=sb.color_palette("hls", n_colors=3))

plt.xlabel("Some Random X")
plt.ylabel("Some Random Y")
plt.title("Clustered: X vs Y")
plt.xlim([-20, 130])
plt.ylim([-20, 100])
plt.savefig(outfilename)
plt.close()

  
 #plt.show()

