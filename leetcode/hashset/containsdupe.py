
## Problem Statement
## Given an integer array, return true if a value appears at least twice, false if none does

import myHashSet as mhs

def containsdupes(inputarray=[]):

 dupefound = False	
 hs = mhs.HashSet()
 

 return dupefound



#### Testing
myarray = [1,2,3,4,1]

print("Input array: {}".format(myarray))
print(" Has duplicates: {}".format(containsdupes(myarray)))
