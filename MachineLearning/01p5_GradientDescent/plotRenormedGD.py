import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sb  
import numpy as np

# set up filenames
infilebase = "./data/"
outfilebase = "./output/"

rawdatafilename = "ng_foodcarts2d" 

inrawdatafilename  = infilebase + rawdatafilename + ".csv"
inscaleddatafilename = outfilebase + "data_renormed.csv"


markertype = "h"
markercolor =  "purple"


# Scatter plot of raw data
outfilename = outfilebase + "rawdata.png"

rawdatafile = pd.read_csv(inrawdatafilename, header=1)

xcolname = "Population of City, in 10,000s"
ycolname = "Profit in $10,000s"
rawdatafile.columns = [xcolname, ycolname]

sb.scatterplot(x=rawdatafile[xcolname], 
               y=rawdatafile[ycolname], marker=markertype, color = markercolor)

xmin, xmax = plt.xlim()
ymin, ymax = plt.ylim()
#print("{} {}".format(ymin,ymax))

plt.title("Training Data: Profit for Food Truck v. City Size")

plt.savefig(outfilename)
plt.clf()


# Scatter plot of renormalized data
outfilename = outfilebase + "scaleddata.png"

xcolname = r'$\eta$'
#xcolname = "Scaled X"
ycolname = "Profit in $10,000s"
scaleddatafile = pd.read_csv(inscaleddatafilename)
#scaleddatafile = pd.read_csv(inscaleddatafilename, header=1)
scaleddatafile.columns = [xcolname, ycolname]

sb.scatterplot(x=scaleddatafile[xcolname], 
               y=scaleddatafile[ycolname], marker=markertype, color = markercolor)

plt.title("Scaled Training Data")

#print("{} {}".format(ymin,ymax))
plt.ylim([ymin, ymax])

rxmin, rxmax = plt.xlim()

plt.text(-0.5,20,"X rescaled as", size="large")
plt.text(-0.5,18,r"$\eta = ( X - \langle X \rangle) / \sigma_X$ ", size="large")

plt.savefig(outfilename)
plt.clf()


# Renormed data with lines
def theformula(t0, t1, x): 
 return t0+t1*x

#alphas = [0.03,0.01,0.003,0.001]


thetafile_1 = pd.read_csv(outfilebase+"thetas_0.03.csv")
thetafile_2 = pd.read_csv(outfilebase+"thetas_0.01.csv")
thetafile_3 = pd.read_csv(outfilebase+"thetas_0.003.csv")
thetafile_4 = pd.read_csv(outfilebase+"thetas_0.001.csv")


itnr   = thetafile_1["itnr"]

t0_1   = thetafile_1["theta_0"]
t1_1   = thetafile_1["theta_1"]

t0_2   = thetafile_2["theta_0"]
t1_2   = thetafile_2["theta_1"]

t0_3   = thetafile_3["theta_0"]
t1_3   = thetafile_3["theta_1"]

t0_4   = thetafile_4["theta_0"]
t1_4   = thetafile_4["theta_1"]

#print(t0_1)
#print(t1_1)
#print(itnr)
#
#print(itnr.size)
#print("\n\n\n")


for t01,t11,t02,t12,t03,t13,t04,t14,itnrd in \
 zip(t0_1,t1_1,t0_2,t1_2,t0_3,t1_3,t0_4,t1_4, itnr):
 #print("{} {} {} {} {} {} {} {} {}".format(itnrd,t01,t11,t02,t12,t03,t13,t04,t14))

 #if(itnrd == itnr.size-1): 
 if(itnrd < 100 or (itnrd < 500 and itnrd%15==0) or (itnrd >= 500 and itnrd < 1500 and  itnrd%50==0) or (itnrd >= 1500 and itnrd%100==0) or itnrd == itnr.size-1): 

  xline = np.linspace(rxmin,rxmax,100)

  yline_1 = t01+t11*xline
  yline_2 = t02+t12*xline
  yline_3 = t03+t13*xline
  yline_4 = t04+t14*xline


  sb.scatterplot(x=scaleddatafile[xcolname], 
                 y=scaleddatafile[ycolname], marker=markertype, color = markercolor)

  plt.plot(xline,yline_1,c='tab:red',    label=r'$\alpha = 0.03$')
  plt.plot(xline,yline_2,c='tab:orange', label=r'$\alpha = 0.01$')
  plt.plot(xline,yline_3,c='tab:green',  label=r'$\alpha = 0.003$')
  plt.plot(xline,yline_4,c='tab:blue',   label=r'$\alpha = 0.001$')

  #print("{} {}".format(ymin,ymax))
  plt.xlim([rxmin, rxmax])
  plt.ylim([ymin, ymax])

  plt.title("Fitting: Iterative Gradient Descent")
  #if(itnrd == itnr.size-1):
  # plt.title("Fit Using Iterative Gradient Descent")
 
  # plt.text(15,5,"Best Fit Line, Iteration {}".format(itnrd),
  #          bbox=dict(boxstyle="square",facecolor="none"))
  # plt.text(15,3,"y = {0:.3f} x + {0:.3f} ".format(t1d, t0d),
  #          bbox=dict(boxstyle="square",facecolor="none"))
  #else: 
  # plt.text(15,5,"Best Fit Line, Iteration {}".format(itnrd))
  # plt.text(15,3,"y = {0:.3f} x + {0:.3f} ".format(t1d, t0d))

  plt.legend(loc='upper left', bbox_to_anchor=(0, 1))
  #plt.legend(loc='upper left', bbox_to_anchor=(-1, 25))

  plt.text(0.3,23,r'$J(\theta)=(1/2m)(\eta\theta-y)^T (\eta\theta-y)$')
  #plt.text(0.3,23,r'$J(\theta)=(1/2)(X\theta-y)^T (X\theta-y)$')
  plt.text(0.3,21,r'minimize $J(\theta)$ wrt. $\theta$')
  plt.text(0.3,19,r'$\theta := \theta - \alpha \nabla_\theta J(\theta) $')
 
  plt.savefig(outfilebase+"fitted{:04d}.png".format(itnrd))
  plt.clf()
  #plt.close()



 if(itnrd == itnr.size-1): 

  xline = np.linspace(xmin,xmax,100)
  sigma = 3.849884 
  mean  = 8.1598
  yline_1 = t01+t11/sigma*(xline-mean)
  yline_2 = t02+t12/sigma*(xline-mean)
  yline_3 = t03+t13/sigma*(xline-mean)
  yline_4 = t04+t14/sigma*(xline-mean)

  xcolname = "Population of City, in 10,000s"
  sb.scatterplot(x=rawdatafile[xcolname], 
                 y=rawdatafile[ycolname], marker=markertype, color = markercolor)


  plt.plot(xline,yline_1,c='tab:red',    label=r'$\alpha = 0.03$')
  plt.plot(xline,yline_2,c='tab:orange', label=r'$\alpha = 0.01$')
  plt.plot(xline,yline_3,c='tab:green',  label=r'$\alpha = 0.003$')
  plt.plot(xline,yline_4,c='tab:blue',   label=r'$\alpha = 0.001$')

  #print("{} {}".format(ymin,ymax))
  plt.xlim([xmin, xmax])
  plt.ylim([ymin, ymax])

  plt.title("Final Fit: Estimated Profit as Function of City Population")
  #if(itnrd == itnr.size-1):
  # plt.title("Fit Using Iterative Gradient Descent")
 
  # plt.text(15,5,"Best Fit Line, Iteration {}".format(itnrd),
  #          bbox=dict(boxstyle="square",facecolor="none"))
  # plt.text(15,3,"y = {0:.3f} x + {0:.3f} ".format(t1d, t0d),
  #          bbox=dict(boxstyle="square",facecolor="none"))
  #else: 
  # plt.text(15,5,"Best Fit Line, Iteration {}".format(itnrd))
  # plt.text(15,3,"y = {0:.3f} x + {0:.3f} ".format(t1d, t0d))

  plt.legend(loc='upper left', bbox_to_anchor=(0, 1))
  #plt.legend(loc='upper left', bbox_to_anchor=(-1, 25))

  plt.text(10,23,r'$y = \theta_0 + \theta_1 x$', size="large")
  plt.text(11,21,r'$\theta_0=5.84$', size="large")
  plt.text(11,19,r'$\theta_1=4.59$', size="large")
  #plt.text(10,23,r'$y = \theta_0 + \theta_1(\frac{x-\langle x \rangle}{\sigma_x})$', size="large")
  ##plt.text(0.3,23,r'$J(\theta)=(1/2)(X\theta-y)^T (X\theta-y)$')
  #plt.text(0.3,21,r'minimize $J(\theta)$ wrt. $\theta$')
  #plt.text(0.3,19,r'$\theta := \theta - \alpha \nabla_\theta J(\theta) $')
 
  plt.savefig(outfilebase+"finalfitted.png")
  plt.clf()
  #plt.close()



# J plot 
jfile_1 = pd.read_csv(outfilebase+"Js_0.03.csv")
jfile_2 = pd.read_csv(outfilebase+"Js_0.01.csv")
jfile_3 = pd.read_csv(outfilebase+"Js_0.003.csv")
jfile_4 = pd.read_csv(outfilebase+"Js_0.001.csv")

J_1    = jfile_1["J"]
J_2    = jfile_2["J"]
J_3    = jfile_3["J"]
J_4    = jfile_4["J"]

itnr   = jfile_1["itnr"]

#J    = jfile["J"]
#itnr = jfile["itnr"]
 
for J1, J2, J3, J4, itnrd in zip(J_1, J_2, J_3, J_4, itnr):
 #if(itnrd == 0 or itnrd == itnr.size-1): 
 if(itnrd < 100 or (itnrd < 500 and itnrd%15==0) or (itnrd >= 500 and itnrd < 1500 and  itnrd%50==0) or (itnrd >= 1500 and itnrd%100==0) or itnrd == itnr.size-1): 
 
  fig = plt.figure()
  plt1 = fig.add_subplot()
  plt1.scatter(itnr, J_1, s=3, c='tab:red',    label=r'$\alpha = 0.03$') 
  plt1.scatter(itnr, J_2, s=3, c='tab:orange', label=r'$\alpha = 0.01$') 
  plt1.scatter(itnr, J_3, s=3, c='tab:green',  label=r'$\alpha = 0.003$')
  plt1.scatter(itnr, J_4, s=3, c='tab:blue',   label=r'$\alpha = 0.001$')

  plt1.axvline(x=itnrd, color="black")
  plt1.set_ylabel(r"Cost Function $J(\theta)=(1/2m)(X\theta-y)^T(X\theta-y)$")
  plt1.set_xlabel("Iteration Number")
  plt1.set_xscale("log") 
  plt1.set_yscale("log")

  plt.title("Iteration {}".format(itnrd))
  #plt.text(1,5,"Iteration {}".format(itnrd))
  plt.legend(loc='upper right')
  #plt.legend(loc='upper left', bbox_to_anchor=(0, 1))
 
  plt.tight_layout()

  plt.savefig(outfilebase+"J_{:04d}.png".format(itnrd))
  plt.clf()
  plt.close()
 




# J plot - how fast does it converge

#
##alphas = ["0.01"]
#for alpha in alphas:
# jfile = pd.read_csv(outfilebase+"Js_"+alpha+".csv")
# J    = jfile["J"]
# itnr = jfile["itnr"]
# 
# for Jd, itnrd in zip(J, itnr):
#  if(itnrd == 0 or itnrd%15==0 or itnrd == itnr.size-1): 
#   #print("({},{}) {}".format(t0d,t1d,itnrd))
#   print("{}, {}".format(Jd, itnrd))
#  
#   plt.close()
#  
#   fig = plt.figure()
#   plt1 = fig.add_subplot()
#   plt1.scatter(itnr, J, s=5)
#  
#   plt1.axvline(x=itnrd, color="red")
#   plt1.set_ylabel(r"Cost Function $J(\theta)=1/2m(X\theta-y)^T(X\theta-y) $")
#   plt1.set_xlabel("Iteration Number")
#
#   plt.text(400,6.5,"Iteration {}".format(itnrd))
#
#   plt.savefig(outfilebase+"J_"+alpha+"_{:04d}.png".format(itnrd))
