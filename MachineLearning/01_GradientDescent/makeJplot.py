import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import seaborn as sb 

import batchgradientdescent as bgd

from matplotlib import cm

def drawSphere(xCenter, yCenter, zCenter, r):
    #draw sphere
    u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
    x=np.cos(u)*np.sin(v)
    y=np.sin(u)*np.sin(v)
    z=np.cos(v)
    # shift and scale sphere
    x = r*x + xCenter
    y = r*y + yCenter
    z = r*z + zCenter
    return (x,y,z)


# get datafile
dataloc = "./data/"
outfileloc = "./outfiles/"
datafile = bgd.importdata( dataloc+"linear2d.csv" )

xmatrix = datafile.x
ymatrix = datafile.y


theta0s = np.linspace(0,10,101)
theta1s = np.linspace(0,10,101)

Jscale = 1


#for t0 in theta0s:
# for t1 in theta1s:
#  print("({},{})".format(t0,t1))

theta0s, theta1s = np.meshgrid(theta0s, theta1s)

J = bgd.Jfunction(theta0s, theta1s, xmatrix, ymatrix)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Plot the surface.
surf = ax.plot_surface(theta0s, theta1s, J/Jscale, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)


#t0=2
#t1=2
#ax.scatter( t0, t1, bgd.Jfunction(t0, t1, xmatrix, ymatrix)/Jscale+0.1, marker="x", c="black", s=100) 
#
#xs,ys,zs = drawSphere(t0, t1, bgd.Jfunction(t0,t1,xmatrix,ymatrix)/Jscale+0.1, 1 )
#
#ax.plot_wireframe(xs, ys, zs, color="black")


plt.xlabel(r'$\Theta_0$')
plt.ylabel(r'$\Theta_1$')
#ax.set_zlabel("J(x) = (T0 + T1x[i]-y[i])^2")
#plt.title("J(x) = (T0 + T1x[i]-y[i])^2")
plt.title(r'$J(x) = \sum_i(\Theta_0 + \Theta_1 * x[i]-y[i])^2$')

plt.savefig(outfileloc+"Jplot.png")
#plt.show()

# 
