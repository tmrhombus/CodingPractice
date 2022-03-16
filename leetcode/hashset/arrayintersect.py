
## Problem Statement
## Given two integer arrays, find their intersection
# Each element in the result must be unique and you may return the result in any order.

import myHashSet as mhs

def intersection(arr1=[], arr2=[]):
 arrintersect=[]

 hs = mhs.HashSet()
 if(len(arr1)<len(arr2)):
  shortarr = arr1
  longarr  = arr2
 else:
  shortarr = arr2
  longarr  = arr1
  

 for num in shortarr:
  hs.add(num)

 hs.display()

 return arrintersect



array1 = [1,2,3,4,5]
array2 = [4,5,6,7,8]

print("Input arrays:")
print(" {}".format(array1))
print(" {}".format(array2))

arrintersect = intersection(array1, array2)
