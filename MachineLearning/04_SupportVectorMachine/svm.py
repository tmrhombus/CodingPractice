import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import loadmat


datasets = ["ex6data1", "ex6data2", "ex6data3"]

for dataset in datasets:
 
 # load data, set initial matrices
 mat = loadmat("./data/{}.mat".format(dataset))
 X = mat["X"]
 y = mat["y"]
 
 ## Plot Initial Data
 # set plotting values
 
 # not accepted
 marker0_type  = "o" 
 marker0_color = "yellow"
 marker0_face  = "yellow"
 marker0_edge  = "black"
 marker0_size  = 18
 
 # accepted 
 marker1_type  = "+" 
 marker1_color = "black"
 marker1_face  = "black"
 marker1_edge  = "black"
 marker1_size  = 18
 
 xmaxs = np.amax(X, axis=0)
 xmins = np.amin(X, axis=0)

 x1max = xmaxs[0]+0.01*(xmaxs[0]-xmins[0])
 x2max = xmaxs[1]+0.01*(xmaxs[1]-xmins[1])
 x1min = xmins[0]-0.01*(xmaxs[0]-xmins[0])
 x2min = xmins[1]-0.01*(xmaxs[1]-xmins[1])

 #x1min = -0.2
 #x1max = 4.2
 #x2min = 1.5
 #x2max = 5.0
 
 # make ndarray of [T, F, F, ...] based on y values
 accept,reject = (y==1).ravel(), (y==0).ravel()
 
 plt.scatter(X[accept,0],X[accept,1],
             c=marker1_color,
             marker=marker1_type,
             s=marker1_size,
             label="Passed"
             )
 
 plt.scatter(X[reject,0],X[reject,1],
             marker=marker0_type,
             color=marker0_color,
             facecolors=marker0_face,
             edgecolors=marker0_edge,
             s=marker0_size,
             label="Failed"
             )
 
 plt.xlim([x1min,x1max])
 plt.ylim([x2min,x2max])
 
 plt.title("Initial Dataset")
 plt.xlabel("Test 1")
 plt.ylabel("Test 2")
 plt.legend(loc="upper right")
 
 plt.savefig("./output/{}_initialdata.png".format(dataset), facecolor="w")
 plt.close("all")
 
 ## Make SVM Classifier
 # import Support Vector Classification
 from sklearn.svm import SVC
 
 # various values of C in L1 Soft Margin SVM
 Cs = [1,5]
 #Cs = [1,5,10,25,50,75,100]
 for C in Cs:
  #plt.close("all")
  # clear plot
  #plt.close()
  fig, ax = plt.subplots()
 
  # make linear classifier and do fit
  svm_linear = SVC(C=C, kernel="linear")
  svm_linear.fit(X, np.ravel(y))
 
  # plot the data
  plt.scatter(X[accept,0],X[accept,1],
              c=marker1_color,
              marker=marker1_type,
              s=marker1_size,
              label="Passed"
              )
  
  plt.scatter(X[reject,0],X[reject,1],
              marker=marker0_type,
              color=marker0_color,
              facecolors=marker0_face,
              edgecolors=marker0_edge,
              s=marker0_size,
              label="Failed"
              )
  
  plt.xlim([x1min,x1max])
  plt.ylim([x2min,x2max])
 
  plt.xlabel("Test 1")
  plt.ylabel("Test 2")
  plt.legend(loc="upper right")
 
  # add SVM decision boundry line to plot
  # make grid of input x1s and x2s
  x1linspace=np.linspace(x1min,x1max,100)
  x2linspace=np.linspace(x2min,x2max,100)
  x1grid,x2grid = np.meshgrid(x1linspace, x2linspace)
  
  # SVM takes (x1, x2) values so unravel and combine xs
  inputx1s = x1grid.ravel()
  inputx2s = x2grid.ravel()
  inputx = np.vstack([inputx1s,inputx2s]).T
  
  # zs for contour must match dimension of grid, hence reshape again
  plt.contour(x1grid,x2grid,svm_linear.predict(inputx).reshape(x1grid.shape),1,colors="b")
  
  plt.title("Linear Kernel Decision Boundry, C = {}".format(C))
 
  t1 = plt.text(0.05,0.05,"C = {}".format(C),transform=ax.transAxes)
  t1.set_bbox(dict(facecolor='white', alpha=1, edgecolor='red'))
 
  plt.savefig("./output/{}_SVMlinearkernel_C{:03d}.png".format(dataset,C), facecolor="w")
  plt.close("all")
 
 
 
  # various values of C in L1 Soft Margin SVM
  Gs = [1,100]
  #Gs = [1,5,10,25,50,75,100]
  for G in Gs:
   fig, ax = plt.subplots()
  
   # make rbf classifier and do fit
   svm_rbf = SVC(C=C, gamma=G, kernel="rbf")
   svm_rbf.fit(X, np.ravel(y))
  
   # plot the data
   plt.scatter(X[accept,0],X[accept,1],
               c=marker1_color,
               marker=marker1_type,
               s=marker1_size,
               label="Passed"
               )
   
   plt.scatter(X[reject,0],X[reject,1],
               marker=marker0_type,
               color=marker0_color,
               facecolors=marker0_face,
               edgecolors=marker0_edge,
               s=marker0_size,
               label="Failed"
               )
   
   plt.xlim([x1min,x1max])
   plt.ylim([x2min,x2max])
  
   plt.xlabel("Test 1")
   plt.ylabel("Test 2")
   plt.legend(loc="upper right")
  
   # add SVM decision boundry line to plot
   # make grid of input x1s and x2s
   x1linspace=np.linspace(x1min,x1max,100)
   x2linspace=np.linspace(x2min,x2max,100)
   x1grid,x2grid = np.meshgrid(x1linspace, x2linspace)
   
   # SVM takes (x1, x2) values so unravel and combine xs
   inputx1s = x1grid.ravel()
   inputx2s = x2grid.ravel()
   inputx = np.vstack([inputx1s,inputx2s]).T
   
   # zs for contour must match dimension of grid, hence reshape again
   plt.contour(x1grid,x2grid,svm_rbf.predict(inputx).reshape(x1grid.shape),1,colors="b")
   
   plt.title("RBF (Gaussian)  Kernel Decision Boundry")
  
   t1 = plt.text(0.05,0.05,"C = {}".format(C),transform=ax.transAxes)
   t2 = plt.text(0.05,0.15,"$\gamma$ = {}".format(G),transform=ax.transAxes)
   t1.set_bbox(dict(facecolor='white', alpha=1, edgecolor='red'))
   t2.set_bbox(dict(facecolor='white', alpha=1, edgecolor='red'))
  
   plt.savefig("./output/{}_SVMrbfkernel_C{:03d}_gamma{:03d}_v2.png".format(dataset,C,G), facecolor="w")
   plt.close("all")



# New Dataset, Scan over C/Gamma for best values
# relative to training dataset

# Load Data/Matrices
# load data, set initial matrices
dataset="ex6data3"
mat = loadmat("./data/{}.mat".format(dataset))
X = mat["X"]
y = mat["y"]
Xval = mat["Xval"]
yval = mat["yval"]

## Plot Initial Data
xmaxs = np.amax(X, axis=0)
xmins = np.amin(X, axis=0)

x1max = xmaxs[0]+0.01*(xmaxs[0]-xmins[0])
x2max = xmaxs[1]+0.01*(xmaxs[1]-xmins[1])
x1min = xmins[0]-0.01*(xmaxs[0]-xmins[0])
x2min = xmins[1]-0.01*(xmaxs[1]-xmins[1])

#x1min = -0.2
#x1max = 4.2
#x2min = 1.5
#x2max = 5.0

# make ndarray of [T, F, F, ...] based on y values
accept,reject = (y==1).ravel(), (y==0).ravel()

plt.scatter(X[accept,0],X[accept,1],
            c=marker1_color,
            marker=marker1_type,
            s=marker1_size,
            label="Passed"
            )

plt.scatter(X[reject,0],X[reject,1],
            marker=marker0_type,
            color=marker0_color,
            facecolors=marker0_face,
            edgecolors=marker0_edge,
            s=marker0_size,
            label="Failed"
            )

plt.xlim([x1min,x1max])
plt.ylim([x2min,x2max])

plt.title("Initial Dataset")
plt.xlabel("Test 1")
plt.ylabel("Test 2")
plt.legend(loc="upper right")

plt.savefig("./output/{}_initialdata.png".format(dataset), facecolor="w")
plt.close("all")



def findBestParams(X,y,Xval,yval,values):
 bestscore = 0
 bestC     = 0
 bestG     = 0
 for C in values:
  for Ginv in values:
   G = 1/Ginv
   
   # make/train/score classifier
   classifier = SVC(C=C, gamma=G, kernel="rbf")
   classifier.fit(X,y)
   prediction = classifier.predict(Xval)
   score = classifier.score(Xval,yval)
  
   # plot the original data

   # make ndarray of [T, F, F, ...] based on y values
   accept,reject = (y==1).ravel(), (y==0).ravel()

   plt.scatter(X[accept,0],X[accept,1],
               c=marker1_color,
               marker=marker1_type,
               s=marker1_size,
               label="Passed"
               )
   
   plt.scatter(X[reject,0],X[reject,1],
               marker=marker0_type,
               color=marker0_color,
               facecolors=marker0_face,
               edgecolors=marker0_edge,
               s=marker0_size,
               label="Failed"
               )
   
   plt.xlim([x1min,x1max])
   plt.ylim([x2min,x2max])
  
   plt.xlabel("Test 1")
   plt.ylabel("Test 2")
   plt.legend(loc="upper right")
  
   # add SVM decision boundry line to plot
   # make grid of input x1s and x2s
   x1linspace=np.linspace(x1min,x1max,100)
   x2linspace=np.linspace(x2min,x2max,100)
   x1grid,x2grid = np.meshgrid(x1linspace, x2linspace)
   
   # SVM takes (x1, x2) values so unravel and combine xs
   inputx1s = x1grid.ravel()
   inputx2s = x2grid.ravel()
   inputx = np.vstack([inputx1s,inputx2s]).T
   
   # zs for contour must match dimension of grid, hence reshape again
   plt.contour(x1grid,x2grid,classifier.predict(inputx).reshape(x1grid.shape),1,colors="b")
   
   plt.title("RBF Kernel - Training Dataset")
  
   t1 = plt.text(0.05,0.05,"C = {}".format(C),transform=ax.transAxes)
   t2 = plt.text(0.05,0.15,"$\gamma$ = {:03.2f}".format(G),transform=ax.transAxes)
   #t1 = plt.text(0.05,0.05,"C = {}".format(C),transform=ax.transAxes)
   #t2 = plt.text(0.05,0.15,"$\gamma$ = {03.2f}".format(G),transform=ax.transAxes)
   t1.set_bbox(dict(facecolor='white', alpha=1, edgecolor='red'))
   t2.set_bbox(dict(facecolor='white', alpha=1, edgecolor='red'))
  
   plt.savefig("./output/{}_scan_C{:03.2f}_gamma{:03.2f}_train.png".format(dataset,C,G), facecolor="w")
   plt.close("all")

   # plot validation dataset

   # make ndarray of [T, F, F, ...] based on y values
   accept,reject = (yval==1).ravel(), (yval==0).ravel()

   plt.scatter(Xval[accept,0],Xval[accept,1],
               c=marker1_color,
               marker=marker1_type,
               s=marker1_size,
               label="Passed"
               )
   
   plt.scatter(Xval[reject,0],Xval[reject,1],
               marker=marker0_type,
               color=marker0_color,
               facecolors=marker0_face,
               edgecolors=marker0_edge,
               s=marker0_size,
               label="Failed"
               )
   
   plt.xlim([x1min,x1max])
   plt.ylim([x2min,x2max])
  
   plt.xlabel("Test 1")
   plt.ylabel("Test 2")
   plt.legend(loc="upper right")

   plt.contour(x1grid,x2grid,classifier.predict(inputx).reshape(x1grid.shape),1,colors="b")
   
   plt.title("RBF Kernel - Validation Dataset")
  
   t1 = plt.text(0.05,0.05,"C = {}".format(C),transform=ax.transAxes)
   t2 = plt.text(0.05,0.15,"$\gamma$ = {:03.2f}".format(G),transform=ax.transAxes)
   t3 = plt.text(0.05,0.25,"Score = {}".format(score),transform=ax.transAxes)
   #t2 = plt.text(0.05,0.15,"$\gamma$ = {3.2f}".format(G),transform=ax.transAxes)
   #t3 = plt.text(0.05,0.25,"Score = {3.2f}".format(score),transform=ax.transAxes)
   t1.set_bbox(dict(facecolor='white', alpha=1, edgecolor='red'))
   t2.set_bbox(dict(facecolor='white', alpha=1, edgecolor='red'))
   t3.set_bbox(dict(facecolor='white', alpha=1, edgecolor='red'))
  
   plt.savefig("./output/{}_scan_C{:03.2f}_gamma{:03.2f}_validate.png".format(dataset,C,G), facecolor="w")
   plt.close("all")
   
   if ( score > bestscore ):
    bestscore = score
    bestC     = C
    bestG     = G

 return bestC, bestG, bestscore


values = [0.01,0.03,0.1,0.3,1,3,10,30]
C,G,score = findBestParams(X,y.ravel(),Xval,yval.ravel(),values)

bestclassifier = SVC(C=C, gamma=G, kernel="rbf")
bestclassifier.fit(X,y.ravel())

# plot it

# make ndarray of [T, F, F, ...] based on y values
accept,reject = (y==1).ravel(), (y==0).ravel()

plt.scatter(X[accept,0],X[accept,1],
            c=marker1_color,
            marker=marker1_type,
            s=marker1_size,
            label="Passed"
            )

plt.scatter(X[reject,0],X[reject,1],
            marker=marker0_type,
            color=marker0_color,
            facecolors=marker0_face,
            edgecolors=marker0_edge,
            s=marker0_size,
            label="Failed"
            )

plt.xlim([x1min,x1max])
plt.ylim([x2min,x2max])

plt.xlabel("Test 1")
plt.ylabel("Test 2")
plt.legend(loc="upper right")

# add SVM decision boundry line to plot
# make grid of input x1s and x2s
x1linspace=np.linspace(x1min,x1max,100)
x2linspace=np.linspace(x2min,x2max,100)
x1grid,x2grid = np.meshgrid(x1linspace, x2linspace)

# SVM takes (x1, x2) values so unravel and combine xs
inputx1s = x1grid.ravel()
inputx2s = x2grid.ravel()
inputx = np.vstack([inputx1s,inputx2s]).T

# zs for contour must match dimension of grid, hence reshape again
plt.contour(x1grid,x2grid,bestclassifier.predict(inputx).reshape(x1grid.shape),1,colors="b")

plt.title("Best Classifier on Training Dataset")

t1 = plt.text(0.05,0.05,"C = {}".format(C),transform=ax.transAxes)
t2 = plt.text(0.05,0.15,"$\gamma$ = {:03.2f}".format(G),transform=ax.transAxes)
t3 = plt.text(0.05,0.25,"Score = {}".format(score),transform=ax.transAxes)
t1.set_bbox(dict(facecolor='white', alpha=1, edgecolor='red'))
t2.set_bbox(dict(facecolor='white', alpha=1, edgecolor='red'))
t3.set_bbox(dict(facecolor='white', alpha=1, edgecolor='red'))

plt.savefig("./output/{}_best_train.png".format(dataset), facecolor="w")
plt.close("all")



# Plot best validation

# make ndarray of [T, F, F, ...] based on y values
accept,reject = (yval==1).ravel(), (yval==0).ravel()

plt.scatter(Xval[accept,0],Xval[accept,1],
            c=marker1_color,
            marker=marker1_type,
            s=marker1_size,
            label="Passed"
            )

plt.scatter(Xval[reject,0],Xval[reject,1],
            marker=marker0_type,
            color=marker0_color,
            facecolors=marker0_face,
            edgecolors=marker0_edge,
            s=marker0_size,
            label="Failed"
            )

plt.xlim([x1min,x1max])
plt.ylim([x2min,x2max])

plt.xlabel("Test 1")
plt.ylabel("Test 2")
plt.legend(loc="upper right")

# add SVM decision boundry line to plot
# make grid of input x1s and x2s
x1linspace=np.linspace(x1min,x1max,100)
x2linspace=np.linspace(x2min,x2max,100)
x1grid,x2grid = np.meshgrid(x1linspace, x2linspace)

# SVM takes (x1, x2) values so unravel and combine xs
inputx1s = x1grid.ravel()
inputx2s = x2grid.ravel()
inputx = np.vstack([inputx1s,inputx2s]).T

# zs for contour must match dimension of grid, hence reshape again
plt.contour(x1grid,x2grid,bestclassifier.predict(inputx).reshape(x1grid.shape),1,colors="b")

plt.title("Best Classifier on Validation Dataset")

t1 = plt.text(0.05,0.05,"C = {}".format(C),transform=ax.transAxes)
t2 = plt.text(0.05,0.15,"$\gamma$ = {:03.2f}".format(G),transform=ax.transAxes)
t3 = plt.text(0.05,0.25,"Score = {}".format(score),transform=ax.transAxes)
t1.set_bbox(dict(facecolor='white', alpha=1, edgecolor='red'))
t2.set_bbox(dict(facecolor='white', alpha=1, edgecolor='red'))
t3.set_bbox(dict(facecolor='white', alpha=1, edgecolor='red'))

plt.savefig("./output/{}_best_validate.png".format(dataset), facecolor="w")
plt.close("all")





