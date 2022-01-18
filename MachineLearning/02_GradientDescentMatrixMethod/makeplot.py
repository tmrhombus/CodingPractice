import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd
import seaborn as sb 

filebase = "./outfiles/"
infilename = "linear2d"

xmin = -10
xmax = 100
ymin = -10
ymax = 450

t0 = 7.73603577 
t1 = 5.0723154 

# Input File
inputpointfile = pd.read_csv("./data/"+infilename+".csv")
inputpointfile.columns = ["Some Random X", "Some Random Y"]
sb.scatterplot(x=inputpointfile["Some Random X"], 
                y=inputpointfile["Some Random Y"])
plt.title("Initial Plot of X and Y")
plt.xlim([xmin, xmax])
plt.ylim([ymin, ymax])

plt.savefig(filebase+"initialdata.png")


# Now add line
sb.scatterplot(x=inputpointfile["Some Random X"], 
               y=inputpointfile["Some Random Y"])
plt.title("Batch Gradient Descent: Solved Analytically")


#eqlabel = "y = {} + {}x".format(t0,t1)
#x = np.array(range(xmin,xmax))
x = np.linspace(xmin,xmax,100)
y = t0+t1*x
#y = theformula(t0, t1, x)
plt.plot(x,y,'-r', label="y = {} + {}x".format(t0,t1))

plt.text(0,400,r"y= X$\Theta=\Theta_0 + \Theta_1 x$")
plt.text(0,375,r"Maximum Likelihood at $\Theta = (X^T X)^{-1} X^T y$")
plt.text(0,325,r"$\Theta_0 = 7.74,  \Theta_1 = 5.07$")

plt.xlim([xmin, xmax])
plt.ylim([ymin, ymax])

plt.savefig(filebase+"fitted.png")

