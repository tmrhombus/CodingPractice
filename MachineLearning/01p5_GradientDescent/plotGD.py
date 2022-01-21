import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sb  
import numpy as np

# Before clustering
# Simple script for plotting 2D data
  # in a scatter plot

infilebase = "./data/"
outfilebase = "./output/"

datafilename = "ng_foodcarts2d" 

indatafilename  = infilebase + datafilename + ".csv"
inthetafilename = infilebase + "thetas.csv"

outfilename = outfilebase + datafilename + ".png"

xmin = 3
xmax = 25 
ymin = -5
ymax = 25 

datafile = pd.read_csv(indatafilename)
#datafile = pd.read_csv(indatafilename, header=None)

xcolname = "Population of City, in 10,000s"
ycolname = "Profit in $10,000s"
datafile.columns = [xcolname, ycolname]

plt.xlim([xmin, xmax])
plt.ylim([ymin, ymax])

#sb.scatterplot(x=datafile.x, y=datafile.y)
sb.scatterplot(x=datafile[xcolname], 
               y=datafile[ycolname])

plt.title("Training Data: Profit for Food Truck v. City Size")

plt.savefig(outfilename)



def theformula(t0, t1, x): 
 return t0+t1*x

thetafile = pd.read_csv(outfilebase+"thetas.csv")
t0   = thetafile["theta_0"]
t1   = thetafile["theta_1"]
itnr = thetafile["itnr"]

# print(t0)
# print(t1)
# print(itnr)

#print(itnr.size)
#print("\n\n\n")

for t0d, t1d, itnrd in zip(t0,t1,itnr):
 if(itnrd == 0 or itnrd%15==0 or itnrd == itnr.size-1): 
  #print("({},{}) {}".format(t0d,t1d,itnrd))

  #x = np.array(range(xmin,xmax))
  xline = np.linspace(xmin,xmax,100)
  yline = t0d+t1d*xline
  #y = theformula(t0, t1, x)


  sb.scatterplot(x=datafile[xcolname], 
               y=datafile[ycolname])

  plt.plot(xline,yline,'-r', label='my line')

  plt.xlim([xmin, xmax])
  plt.ylim([ymin, ymax])

  plt.title("Fitting: Iterative Gradient Descent")
  if(itnrd == itnr.size-1):
   plt.title("Fit Using Iterative Gradient Descent")
 
   plt.text(15,5,"Best Fit Line, Iteration {}".format(itnrd),
            bbox=dict(boxstyle="square",facecolor="none"))
   plt.text(15,3,"y = {0:.3f} x + {0:.3f} ".format(t1d, t0d),
            bbox=dict(boxstyle="square",facecolor="none"))
  else: 
   plt.text(15,5,"Best Fit Line, Iteration {}".format(itnrd))
   plt.text(15,3,"y = {0:.3f} x + {0:.3f} ".format(t1d, t0d))
 
  plt.savefig(outfilebase+"fitted{:04d}.png".format(itnrd))
  plt.close()


# J plot - how fast does it converge


alphas = ["0.01"]
for alpha in alphas:
 jfile = pd.read_csv(outfilebase+"Js_"+alpha+".csv")
 J    = jfile["J"]
 itnr = jfile["itnr"]
 
 for Jd, itnrd in zip(J, itnr):
  if(itnrd == 0 or itnrd%15==0 or itnrd == itnr.size-1): 
   #print("({},{}) {}".format(t0d,t1d,itnrd))
   print("{}, {}".format(Jd, itnrd))
  
   plt.close()
  
   fig = plt.figure()
   plt1 = fig.add_subplot()
   plt1.scatter(itnr, J, s=5)
  
   plt1.axvline(x=itnrd, color="red")
   plt1.set_ylabel(r"Cost Function $J(\theta)=1/2m(X\theta-y)^T(X\theta-y) $")
   plt1.set_xlabel("Iteration Number")

   plt.text(400,6.5,"Iteration {}".format(itnrd))

   plt.savefig(outfilebase+"J_"+alpha+"_{:04d}.png".format(itnrd))
