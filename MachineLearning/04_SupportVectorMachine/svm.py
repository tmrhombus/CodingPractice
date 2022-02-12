import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import loadmat

# load data, set initial matrices
mat = loadmat("./data/ex6data1.mat")
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

x1min = -0.2
x1max = 4.2
x2min = 1.5
x2max = 5.0

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

plt.savefig("./output/ex6data1_initialdata.png", facecolor="w")
plt.close("all")

## Make SVM Classifier
# import Support Vector Classification
from sklearn.svm import SVC

# various values of C in L1 Soft Margin SVM
Cs = [1,5,25,100]
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

 plt.savefig("./output/ex6data1_SVMlinearkernel_C{:03d}.png".format(C), facecolor="w")
 plt.close("all")



 # various values of C in L1 Soft Margin SVM
 Gs = [1,5,25,100]
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
  
  plt.title("Linear Kernel Decision Boundry")
 
  t1 = plt.text(0.05,0.05,"C = {}".format(C),transform=ax.transAxes)
  t2 = plt.text(0.05,0.15,"$\gamma$ = {}".format(G),transform=ax.transAxes)
  t1.set_bbox(dict(facecolor='white', alpha=1, edgecolor='red'))
  t2.set_bbox(dict(facecolor='white', alpha=1, edgecolor='red'))
 
  plt.savefig("./output/ex6data1_SVMrbfkernel_C{:03d}_gamma{:03d}_v2.png".format(C,G), facecolor="w")
  plt.close("all")






# #
# #
# ### SVM with Gaussian Kernel
# #mat2 = loadmat("./data/ex6data2.mat")
# #X2 = mat2["X"]
# #y2 = mat2["y"]
# #
# #
# #m2,n2 = X2.shape[0],X2.shape[1]
# #pos2,neg2= (y2==1).reshape(m2,1), (y2==0).reshape(m2,1)
# #plt.figure(figsize=(8,6))
# #plt.scatter(X2[pos2[:,0],0],X2[pos2[:,0],1],c="r",marker="+")
# #plt.scatter(X2[neg2[:,0],0],X2[neg2[:,0],1],c="y",marker="o")
# #plt.xlim(0,1)
# #plt.ylim(0.4,1)
# #
# #
# #
# #classifier3 = SVC(kernel="rbf",gamma=30)
# #classifier3.fit(X2,y2.ravel())
# #
# #
# #plt.figure(figsize=(8,6))
# #plt.scatter(X2[pos2[:,0],0],X2[pos2[:,0],1],c="r",marker="+")
# #plt.scatter(X2[neg2[:,0],0],X2[neg2[:,0],1],c="y",marker="o")
# #
# #
# ## plotting the decision boundary
# #X_5,X_6 = np.meshgrid(np.linspace(X2[:,0].min(),X2[:,1].max(),num=100),np.linspace(X2[:,1].min(),X2[:,1].max(),num=100))
# #plt.contour(X_5,X_6,classifier3.predict(np.array([X_5.ravel(),X_6.ravel()]).T).reshape(X_5.shape),1,colors="b")
# #plt.xlim(0,1)
# #plt.ylim(0.4,1)
# #
# #
# #
# #mat3 = loadmat("./data/ex6data3.mat")
# #X3 = mat3["X"]
# #y3 = mat3["y"]
# #Xval = mat3["Xval"]
# #yval = mat3["yval"]
# #
# #m3,n3 = X3.shape[0],X3.shape[1]
# #pos3,neg3= (y3==1).reshape(m3,1), (y3==0).reshape(m3,1)
# #plt.figure(figsize=(8,6))
# #plt.scatter(X3[pos3[:,0],0],X3[pos3[:,0],1],c="r",marker="+",s=50)
# #plt.scatter(X3[neg3[:,0],0],X3[neg3[:,0],1],c="y",marker="o",s=50)
# #
# #
# #def dataset3Params(X, y, Xval, yval,vals):
# #    """
# #    Returns your choice of C and sigma. You should complete this function to return the optimal C and 
# #    sigma based on a cross-validation set.
# #    """
# #    acc = 0
# #    best_c=0
# #    best_gamma=0
# #    for i in vals:
# #        C= i
# #        for j in vals:
# #            gamma = 1/j
# #            classifier = SVC(C=C,gamma=gamma)
# #            classifier.fit(X,y)
# #            prediction = classifier.predict(Xval)
# #            score = classifier.score(Xval,yval)
# #            if score>acc:
# #                acc =score
# #                best_c =C
# #                best_gamma=gamma
# #    return best_c, best_gamma
# #
# #
# #vals = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30]
# #C, gamma = dataset3Params(X3, y3.ravel(), Xval, yval.ravel(),vals)
# #classifier4 = SVC(C=C,gamma=gamma)
# #classifier4.fit(X3,y3.ravel())
# #
# #
# #
# #plt.figure(figsize=(8,6))
# #plt.scatter(X3[pos3[:,0],0],X3[pos3[:,0],1],c="r",marker="+",s=50)
# #plt.scatter(X3[neg3[:,0],0],X3[neg3[:,0],1],c="y",marker="o",s=50)
# #
# ## plotting the decision boundary
# #X_7,X_8 = np.meshgrid(np.linspace(X3[:,0].min(),X3[:,1].max(),num=100),np.linspace(X3[:,1].min(),X3[:,1].max(),num=100))
# #plt.contour(X_7,X_8,classifier4.predict(np.array([X_7.ravel(),X_8.ravel()]).T).reshape(X_7.shape),1,colors="b")
# #plt.xlim(-0.6,0.3)
# #plt.ylim(-0.7,0.5)
# #
# #
# #
