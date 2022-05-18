

def solution( idig, jdig ):
 """
 returns the largest palendrome made from
 the product of an idig x jdig -digit number

 method:

 The two numbers are i,j
 Start at i=999, j=999

 check i*j, then (i-1)*j, then (i-1)(j-1), etc
 
 the first palendrome we find will be the largest
 """

 maxi = -1
 maxj = -1
 maxprod = -1
 for i in range( 10**(idig-1),10**idig ):
  for j in range( 10**(jdig-1),10**jdig ):
   #print(" {}*{} = {}    :: {}".format( i,j,i*j,isapalendrome(i*j) ))
   if ( isapalendrome(i*j) and maxprod < i*j ):
    #print("------------------------")
    maxi = i
    maxj = j
    maxprod = i*j 
   
 return maxi, maxj, maxprod


def isapalendrome( x ):
 """
 Checks if an integer is a palendrome
 convert x to a string, indexing backwards steps
 """
 if str(int(x)) == str(x)[::-1]:
  return True
 else:
  return False
