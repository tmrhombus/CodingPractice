import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sb  
import numpy as np

# set up filenames
infilebase = "./data/"
outfilebase = "./output/"

datafilename = "ng_testscores" 

infilename_data  = infilebase + datafilename + ".csv"

# not admitted
marker0_type  = "o"
marker0_color = "yellow"
marker0_face  = "yellow"
marker0_edge  = "black"
marker0_size  = 18

# admitted 
marker1_type  = "+"
marker1_color = "black"
marker1_face  = "black"
marker1_edge  = "black"
marker1_size  = 18

xmin=20
xmax=110
ymin=20
ymax=110


######## # Scatter plot of raw data
rawoutfilename = outfilebase + "rawdata.png"
fitoutfilename = outfilebase + "fitted.png"

data = pd.read_csv(infilename_data)
#data = pd.read_csv(infilename_data, header=1)

x1colname = "Exam 1 Score"
x2colname = "Exam 2 Score"
ycolname = "Admitted"
data.columns = [x1colname, x2colname, ycolname]

yadmitted = data.loc[data[ycolname] == 1]
nadmitted = data.loc[data[ycolname] == 0]

fig = plt.figure()
plt1 = fig.add_subplot()

plt1.scatter(x=yadmitted[x1colname], y=yadmitted[x2colname],
 marker=marker1_type,
 color=marker1_color,
 facecolors=marker1_face,
 edgecolors=marker1_edge,
 s=marker1_size,
 label="Admitted"
)

plt1.scatter(x=nadmitted[x1colname], y=nadmitted[x2colname],
 marker=marker0_type,
 color=marker0_color,
 facecolors=marker0_face,
 edgecolors=marker0_edge,
 s=marker0_size,
 label="Not Admitted"
)

plt.title("Admittance Based on Test Scores")

#xmin, xmax = plt.xlim()
#ymin, ymax = plt.ylim()
#print("{} {}".format(xmin,xmax))
#print("{} {}".format(ymin,ymax))

plt1.set_xlabel(x1colname)
plt1.set_ylabel(x2colname)

plt.xlim([xmin,xmax])
plt.ylim([ymin,ymax])

plt1.legend(loc='lower left')
plt.title("Admittance Based on Test Scores")

plt.savefig(rawoutfilename)


## draw fitted line on the same plot
theta0 = -25.16131857
theta1 = 0.20623159
theta2 = 0.20147149

def calcx2(x1, t0, t1, t2, y):
 return (-1/t2)*(-y + t1*x1 + t0)

linexs = [xmin, xmax]
lineys0 = []
lineysp5 = []
lineys1 = []
for linex in linexs:
 lineys0.append( calcx2(linex, theta0, theta1, theta2, 0) )
for linex in linexs:
 lineysp5.append( calcx2(linex, theta0, theta1, theta2, .5) )
for linex in linexs:
 lineys1.append( calcx2(linex, theta0, theta1, theta2, 1) )

#plt.axline( (linexs[0],lineys0[0]), (linexs[1], lineys0[1]), label="y=0", color="r" )
#plt.axline( (linexs[0],lineysp5[0]), (linexs[1], lineysp5[1]), label="y=1/2", color="b" )
#plt.axline( (linexs[0],lineys1[0]), (linexs[1], lineys1[1]), label="y=1", color="g" )
plt.axline( (linexs[0],lineysp5[0]), (linexs[1], lineysp5[1]), label="decision boundry", color="b" )

plt1.legend(loc='lower left')

plt.savefig(fitoutfilename)

plt.clf()

