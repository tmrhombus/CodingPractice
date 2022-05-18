

def solution( ):
 """
 returns the largest palendrome made from
 the product of two 3-digit numbers

 method:

 The two numbers are i,j
 Start at i=999, j=999

 check i*j, then (i-1)*j, then (i-1)(j-1), etc
 
 the first palendrome we find will be the largest
 """

def isapalendrome( x ):
 """
 Checks if an integer is a palendrome
 convert x to a string, indexing backwards steps
 """
 if str(int(x)) == str(x)[::-1]:
  return True
 else:
  return False
