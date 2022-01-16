import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import seaborn as sb 

filebase = "./outfiles/"
infilename = "linear2d"
#infilename = "threepoints"

niterations = 500
#xmin = -3
#xmax = 15
#ymin = -3
#ymax = 15

xmin = 0
xmax = 60
ymin = 0
ymax = 200

# Before clustering
#inputpointfile = pd.read_csv("./data/triplegauss.csv", header=None)
#inputpointfile = pd.read_csv("./data/twopoints.csv")
inputpointfile = pd.read_csv("./data/"+infilename+".csv")
inputpointfile.columns = ["Some Random X", "Some Random Y"]
sb.scatterplot(x=inputpointfile["Some Random X"], 
                y=inputpointfile["Some Random Y"])
plt.title("Initial Plot of X and Y")
plt.xlim([xmin, xmax])
plt.ylim([ymin, ymax])

plt.savefig(filebase+"initialdata.png")


def theformula(t0, t1, x):
 return t0+t1*x

# Now add lines
for i in range(0, niterations+1):
 thetafilename = filebase+"thetas{:04d}.csv".format(i)
 thetafile = pd.read_csv(thetafilename)
 t0 = thetafile.theta_0[0]
 t1 = thetafile.theta_1[0]
 #print(thetafile.theta_0)
 #print(t0+t1)
 #print(" thetas: {}   {} ".format(t0,t1))

 plt.close()
 
 sb.scatterplot(x=inputpointfile["Some Random X"], 
                y=inputpointfile["Some Random Y"])
 plt.title("Finding best parameters - gradient descent")
 plt.xlim([xmin, xmax])
 plt.ylim([ymin, ymax])


 #x = np.array(range(xmin,xmax))
 x = np.linspace(xmin,xmax,100)
 y = t0+t1*x
 #y = theformula(t0, t1, x)
 plt.plot(x,y,'-r', label='my line')

 plt.savefig(filebase+"fitted{:04d}.png".format(i))

# # Now add centers
# for x in range(0, niterations):
#  plt.figure()
#  # print()"{:04d}".format(1)
#  pointsfilename = filebase + "points0"
#  centersfilename = filebase + "centers"+str(x)
#  outfilename = filebase + "plot_" + "{:04d}".format(x) + ".png"
#  
#  
#  pointsdatafile = pd.read_csv(pointsfilename+".csv")
#  centersdatafile = pd.read_csv(centersfilename+".csv")
#  # sb.scatterplot(x=pointsdatafile.x, y=pointsdatafile.y, 
#  #                 hue=pointsdatafile.c, 
#  #                 palette=sb.color_palette("hls", n_colors=2))
#  sb.scatterplot(x=pointsdatafile.x, y=pointsdatafile.y, 
#                 color="black")
#  sb.scatterplot(x=centersdatafile.x, y=centersdatafile.y, 
#                  color="red")
# 
# 
#  # put circles around center points  
#  df = pd.read_csv(centersfilename+".csv")
#  for i in range(len(df)):
#   # print(df.values[i][0]) 
#   # print(df.values[i][1]) 
#   #mycirc = plt.Circle((20, 20), 5, color='g', fill=False)
#   mycirc = plt.Circle((df.values[i][0], df.values[i][1]), 15, color='r', fill=False)
#   plt.gca().add_patch(mycirc)
# 
#  plt.xlabel("Some Random X")
#  plt.ylabel("Some Random Y")
#  plt.title("Clustering - Mean Shift")
#  plt.xlim([xmin, xmax])
#  plt.ylim([ymin, ymax])
#  plt.savefig(outfilename)
#  plt.clf()
#  plt.close()
# 
# 
# # now a colored plot with centers
# x=niterations-1
# plt.figure()
# # print()"{:04d}".format(1)
# pointsfilename = filebase + "points0"
# centersfilename = filebase + "centers"+str(x)
# outfilename = filebase + "plot_" + "{:04d}".format(x) + "_color.png"
# 
# 
# pointsdatafile = pd.read_csv(pointsfilename+".csv")
# centersdatafile = pd.read_csv(centersfilename+".csv")
# sb.scatterplot(x=pointsdatafile.x, y=pointsdatafile.y, 
#                 hue=pointsdatafile.c, 
#                 palette=sb.color_palette("hls", n_colors=ncolors))
# # sb.scatterplot(x=pointsdatafile.x, y=pointsdatafile.y, 
# #                color="black")
# sb.scatterplot(x=centersdatafile.x, y=centersdatafile.y, 
#                 color="red")
# 
# 
# # put circles around center points  
# df = pd.read_csv(centersfilename+".csv")
# for i in range(len(df)):
#  # print(df.values[i][0]) 
#  # print(df.values[i][1]) 
#  #mycirc = plt.Circle((20, 20), 5, color='g', fill=False)
#  mycirc = plt.Circle((df.values[i][0], df.values[i][1]), 15, color='r', fill=False)
#  plt.gca().add_patch(mycirc)
# 
# plt.xlabel("Some Random X")
# plt.ylabel("Some Random Y")
# plt.title("Clustering - Mean Shift")
# plt.xlim([xmin, xmax])
# plt.ylim([ymin, ymax])
# plt.savefig(outfilename)
# plt.close()
# 
# 
# # now a colored plot with no centers
# x=niterations-1
# plt.figure()
# # print()"{:04d}".format(1)
# pointsfilename = filebase + "points0"
# outfilename = filebase + "plot_" + "{:04d}".format(x) + "_colorNOC.png"
# 
# 
# pointsdatafile = pd.read_csv(pointsfilename+".csv")
# sb.scatterplot(x=pointsdatafile.x, y=pointsdatafile.y, 
#                 hue=pointsdatafile.c, 
#                 palette=sb.color_palette("hls", n_colors=ncolors))
# 
# plt.xlabel("Some Random X")
# plt.ylabel("Some Random Y")
# plt.title("Clustered via Mean Shift")
# plt.xlim([xmin, xmax])
# plt.ylim([ymin, ymax])
# plt.savefig(outfilename)
# plt.close()
# 
#   
#  #plt.show()
# 
