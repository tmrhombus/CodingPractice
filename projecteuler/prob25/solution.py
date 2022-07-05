
def solution(ndigits):

 i = 1
 j = 1
 index = 2
 while True:
  
  if (index > 12):
   break

  j = j+i
  i = j-i
  index += 1

  print("i={}, j={}, ind = {}".format(i,j,index))
 
 return j,index
