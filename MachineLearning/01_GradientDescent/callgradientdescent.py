import batchgradientdescent as bgd
import sys # write file

# bgd.doit()

# get datafile
dataloc = "./data/"
outfileloc = "./outfiles/"
datafile = bgd.importdata( dataloc+"twopoints.csv" )
#datafile = bgd.importdata( dataloc+"linear2d.csv" )

#print(datafile)

xmatrix = datafile.x
ymatrix = datafile.y

 #  print(xmatrix)
 #  print(ymatrix)
 #  print(len(xmatrix))
 #  print(len(ymatrix))

 
# initialize thetas
theta_0 = 0
theta_1 = 0
 
# start iterating
stepsize = 0.01
iterationnr = 0
while True:
 if iterationnr > 20: break
 print("Iteration: "+str(iterationnr))
 print("theta_0: "+str(theta_0))
 print("theta_1: "+str(theta_1))

 derivativeJ_0 = 0
 derivativeJ_1 = 0
 for i in range(len(xmatrix)):
  # print(i)
  # print( "("+str(xmatrix[i]) + "," + str(ymatrix[i]) + ")" )
  diff = bgd.hfunction( theta_0, theta_1, xmatrix[i] ) - ymatrix[i]
  print(" diff: "+str(diff))
  # print(diff) 
  derivativeJ_0 += diff
  derivativeJ_1 += diff*xmatrix[i]
 print("derivJ_0: "+str(derivativeJ_0))
 print("derivJ_1: "+str(derivativeJ_1))

 update_0 = stepsize*derivativeJ_0
 update_1 = stepsize*derivativeJ_1

 print(update_0)
 print(update_1)

 newtheta_0 = theta_0 - update_0
 newtheta_1 = theta_1 - update_1

 print(newtheta_0)
 print(newtheta_1)
 
 difftheta_0 = theta_0 - newtheta_0
 difftheta_1 = theta_1 - newtheta_1

 with open(outfileloc+"thetas{}.csv".format(iterationnr), 'w') as f:
  f.write("theta_0,theta_1\n")
  f.write("{},{}".format(theta_0,theta_1))
  #print("theta_0,theta_1")
  #print("{},{}".format(theta_0,theta_1))


 if ( abs(difftheta_0) + abs(difftheta_1) < 0.001 ):
  break 

 theta_0 = newtheta_0
 theta_1 = newtheta_1

 iterationnr += 1
 print("------------------")


