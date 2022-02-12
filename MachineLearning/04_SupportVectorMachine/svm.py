import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import loadmat

# load data, set initial matrices
mat = loadmat("./data/ex6data1.mat")
X = mat["X"]
y = mat["y"]

# plot initial data
#m,n = X.shape

# make T/F lists of y values
pos,neg= (y==1), (y==0)

#print(pos)
#print("\n\n")
#print(neg)



plt.scatter(X[pos[:,0],0],X[pos[:,0],1],c="r",marker="+",s=50)
plt.scatter(X[neg[:,0],0],X[neg[:,0],1],c="y",marker="o",s=50)

plt.title("Initial Dataset")
plt.xlabel("X1")
plt.ylabel("X2")

plt.savefig("./output/ex6data1_initialdata.png", facecolor="w")

# ## import Support Vector Classification
# #from sklearn.svm import SVC
# #classifier = SVC(kernel="linear")
# #classifier.fit(X,np.ravel(y))
# #
# #
# #plt.figure(figsize=(8,6))
# #plt.scatter(X[pos[:,0],0],X[pos[:,0],1],c="r",marker="+",s=50)
# #plt.scatter(X[neg[:,0],0],X[neg[:,0],1],c="y",marker="o",s=50)
# #
# #plt.savefig("./output/ex6data1_SVMlinearkernel.png", facecolor="w")
# #
# ## plotting the decision boundary
# #X_1,X_2 = np.meshgrid(np.linspace(X[:,0].min(),X[:,1].max(),num=100),np.linspace(X[:,1].min(),X[:,1].max(),num=100))
# #plt.contour(X_1,X_2,classifier.predict(np.array([X_1.ravel(),X_2.ravel()]).T).reshape(X_1.shape),1,colors="b")
# #plt.xlim(0,4.5)
# #plt.ylim(1.5,5)
# #
# ## Test C = 100
# #classifier2 = SVC(C=100,kernel="linear")
# #classifier2.fit(X,np.ravel(y))
# #
# #plt.figure(figsize=(8,6))
# #plt.scatter(X[pos[:,0],0],X[pos[:,0],1],c="r",marker="+",s=50)
# #plt.scatter(X[neg[:,0],0],X[neg[:,0],1],c="y",marker="o",s=50)
# #
# #plt.savefig("./output/ex6data1_SVNlinearkernel_C100.png", facecolor="w")
# #
# ## plotting the decision boundary
# #X_3,X_4 = np.meshgrid(np.linspace(X[:,0].min(),X[:,1].max(),num=100),np.linspace(X[:,1].min(),X[:,1].max(),num=100))
# #plt.contour(X_3,X_4,classifier2.predict(np.array([X_3.ravel(),X_4.ravel()]).T).reshape(X_3.shape),1,colors="b")
# #plt.xlim(0,4.5)
# #plt.ylim(1.5,5)
# #
# #plt.savefig("./output/ex6data1_SVNlinearkernel_C100.png", facecolor="w")
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
