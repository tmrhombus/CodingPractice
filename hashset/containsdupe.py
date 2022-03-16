
## Problem Statement
## Given an integer array, return true if a value appears at least twice, false if none does

import myHashSet as mhs

def dupesearch(inputarray=[]):

 dupefound = False	
 thedupe = None
 hs = mhs.HashSet()

 itnr = 0
 while itnr<len(inputarray):

  if(not hs.contains(inputarray[itnr])):
   hs.add(inputarray[itnr])
  else:
   dupefound=True
   thedupe = inputarray[itnr]
   break

  itnr += 1

 return dupefound, thedupe



#### Testing
myarray = [1,2,3,4,1,6,7,8]

dupefound, thedupe = dupesearch(myarray)
print("Input array: {}".format(myarray))
print(" Has duplicates: {} ({})".format(dupefound, thedupe))
