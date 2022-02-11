import copy 
import csv

class point:
 """
 point class 
 
 contains coordinates (point.x, point.y)
 and list of points that would be valid steps
 """
 def __init__(self, x, y): 
  self.x = x 
  self.y = y 
  self.availablepoints = []

def makemorearrays(array):

 arraylist = []
 arraylist.append(array)

 for x in range(0,len(array)):
  for y in range(0,len(array[0])):
   #print( array[x][y] )
   if array[x][y] == 1:
    vsteps = validsteps(array,point(x,y))
    if vsteps: 
     tmparray = copy.deepcopy(array)
     tmparray[x][y] = 0
     arraylist.append(tmparray)

 return arraylist


def validsteps(themap, currentloc):
 """
 Given a map and a location (point),
 return list of points that are valid
 next moves
 """
 
 steplist = []

 x = currentloc.x
 y = currentloc.y
 
 upX   = False
 downX = False
 upY   = False
 downY = False
 if( x+1 <= maxX ): upX=True
 if( y+1 <= maxY ): upY=True
 if( x-1 >= 0 ):  downX=True
 if( y-1 >= 0 ):  downY=True
  
 if(upX):
  if( themap[x+1][y]==0 ):
   steplist.append( point(x+1,y) )
 if(downX):
  if( themap[x-1][y]==0 ):
   steplist.append( point(x-1,y) )
 if(upY):
  if( themap[x][y+1]==0 ):
   steplist.append( point(x,y+1) )
 if(downY):
  if( themap[x][y-1]==0 ):
   steplist.append( point(x,y-1) )

 return steplist
 

def haventbeento(candidatepoint, alreadybeento):
 """
 For a given point P, check against list of
 points already been to
 
 return bool
  True  if P not in list
  False if P is in list
 """
 x = candidatepoint.x
 y = candidatepoint.y
 for abt in alreadybeento:
  if (abt.x==x and abt.y==y):
   return False
 return True


def checkforconvergence(currentloc):
 """
 Is a given location the end?
 """
 if(currentloc.x == maxX and currentloc.y == maxY):
  return True
 else: return False


def solution(themap):

 printitallout=True

 if(printitallout):
  with open("./outfiles/input.csv", 'w') as afile:
   arraywriter = csv.writer(afile, delimiter=',')
   arraywriter.writerows(themap)

 # determine size of map
 global maxX, maxY
 maxX = len(themap)-1
 maxY = len(themap[0])-1

 beststeps = (maxX+1)*(maxY+1)

 # allarrays = makemorearrays(array)

 # arraynr = 0

 start1_X = 0
 start1_Y = 0
 start2_X = maxX
 start2_Y = maxY
 
 initialpoint1 = point(start1_X,start1_Y)
 initialpoint1.availablepoints.append(initialpoint1)
 initialpoint2 = point(start2_X,start2_Y)
 initialpoint2.availablepoints.append(initialpoint2)
 
 converged = checkforconvergence(initialpoint1)
 if converged: return 0
 
 alreadybeento1 = []
 alreadybeento1.append(initialpoint1)
 alreadybeento2 = []
 alreadybeento2.append(initialpoint2)
 
 nsteps = 0
 while(True):
  nsteps += 1
  if(nsteps > beststeps/2):
  #if(nsteps > (beststeps-1)/2):
   break

  converged1 = False
  converged2 = False

  if(printitallout):
   with open("./outfiles/sp1_{:03d}.csv".format(nsteps), 'w' ) as ipfile:
    for startpoint in initialpoint1.availablepoints:
     ipfile.write("{},{}\n".format(startpoint.x, startpoint.y) )
 
  possiblemoves1 = []
  for startpoint in initialpoint1.availablepoints:
   thispointsmoves = validsteps(themap, startpoint)
   for candidatepoint in thispointsmoves:
    if haventbeento(candidatepoint, alreadybeento1):

     # check if point is in other list
     if not haventbeento(candidatepoint, alreadybeento2):
      converged1 = True

     possiblemoves1.append(candidatepoint)
     alreadybeento1.append(candidatepoint)

  if(printitallout):
   with open("./outfiles/sp2_{:03d}.csv".format(nsteps), 'w' ) as ipfile:
    for startpoint in initialpoint2.availablepoints:
     ipfile.write("{},{}\n".format(startpoint.x, startpoint.y) )

  possiblemoves2 = []
  for startpoint in initialpoint2.availablepoints:
   thispointsmoves = validsteps(themap, startpoint)
   for candidatepoint in thispointsmoves:
    if haventbeento(candidatepoint, alreadybeento2):

     # check if point is in other list
     if not haventbeento(candidatepoint, alreadybeento1):
      converged2 = True

     possiblemoves2.append(candidatepoint)
     alreadybeento2.append(candidatepoint)


  if (converged1):
   beststeps = 2*nsteps
   if(printitallout):
    with open("./outfiles/convergence.txt", 'w') as cfile:
     cfile.write("Convergence Found by Path 1\n")
     cfile.write("Total Iterations: {}\n".format(nsteps))
     cfile.write("Formula: 2 x nIterations\n")
     cfile.write("Total Steps: {}".format(beststeps))
   break
  if (converged2):
   beststeps = 2*nsteps+1
   if(printitallout):
    with open("./outfiles/convergence.txt", 'w') as cfile:
     cfile.write("Convergence Found by Path 2\n")
     cfile.write("Total Iterations: {}\n".format(nsteps))
     cfile.write("Formula: 2 x nIterations + 1\n")
     cfile.write("Total Steps: {}".format(beststeps))
   break

  initialpoint1.availablepoints = set(possiblemoves1)
  initialpoint2.availablepoints = set(possiblemoves2)

 return beststeps


