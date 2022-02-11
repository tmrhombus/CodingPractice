import matplotlib.pyplot as plt 
import matplotlib.cm as cm
import pandas as pd
from os.path import exists

# set parameters
infilebase = "./outfiles/"

# input array
fname_arr = infilebase + "input.csv"
f_arr = pd.read_csv(fname_arr, header=None)

fig, ax = plt.subplots()
i = ax.imshow(f_arr, cmap='Greys', interpolation='nearest')
#fig.colorbar(i)

xmin, xmax = ax.get_xlim()
ymin, ymax = ax.get_ylim()

#print("xmin: {} xmax: {}".format(xmin,xmax))
#print("ymin: {} ymax: {}".format(ymin,ymax))

#plt.show()
plt.title("Initial Maze")
plt.savefig(infilebase+"input.png")

maxit = 34
for itnr in range(1,maxit+1):
 fname_s1 = infilebase + "sp1_{:03d}.csv".format(itnr)
 fname_s2 = infilebase + "sp2_{:03d}.csv".format(itnr)

 if exists(fname_s1):
  f_s1 = pd.read_csv(fname_s1, header=None)
 if exists(fname_s2):
  f_s2 = pd.read_csv(fname_s2, header=None)

 xcol = "x"
 ycol = "y"
 f_s1.columns = [xcol, ycol]
 f_s2.columns = [xcol, ycol]

 plt.scatter(x=f_s1[ycol], y=f_s1[xcol], marker="s", s=100, color="#2C5F2D")
 plt.title("Iteration {}.1".format(itnr))
 plt.savefig(infilebase+"search_{:03d}_1".format(itnr))
 plt.scatter(x=f_s1[ycol], y=f_s1[xcol], marker="s", s=100, color="#97BC62FF")

 plt.title("Iteration {}.2".format(itnr))
 plt.scatter(x=f_s2[ycol], y=f_s2[xcol], marker="s", s=100, color="#0063B2FF")
 plt.savefig(infilebase+"search_{:03d}_2".format(itnr))
 plt.scatter(x=f_s2[ycol], y=f_s2[xcol], marker="s", s=100, color="#9CC3D5FF")



# get text from file
textline=[]
with open(infilebase+"convergence.txt") as file:
 for line in file:
  textline.append(line.rstrip())
        #print(line.rstrip())

#plt.clf()

t1 = plt.text(0.05,0.85,textline[0],transform=ax.transAxes)
t2 = plt.text(0.05,0.75,textline[1],transform=ax.transAxes)
t3 = plt.text(0.05,0.65,textline[2],transform=ax.transAxes)
t4 = plt.text(0.05,0.55,textline[3],transform=ax.transAxes)



t1.set_bbox(dict(facecolor='white', alpha=1, edgecolor='red'))
t2.set_bbox(dict(facecolor='white', alpha=1, edgecolor='red'))
t3.set_bbox(dict(facecolor='white', alpha=1, edgecolor='red'))
t4.set_bbox(dict(facecolor='white', alpha=1, edgecolor='red'))

plt.savefig(infilebase+"converged.png")
