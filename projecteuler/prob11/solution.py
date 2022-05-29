import math 

def solution( n, grid ):
 """
 returns the largest product of n sequential numbers
 where sequential can mean horizontal, vertical, diagonal

 method:
 work top to bottom, left to right
 at grid point (i,j) only check right,down,downward diagonals
 """

 maxprod = -1
 horlen = len(grid[0])
 verlen = len(grid)
 print(horlen)
 print(verlen)

# for i in range(horlen):
#  for j in range(verlen):
#
#   # check horisontally
#   #if (i < 
#   print(grid[i][j])

 index = [-1,-1]
 nums = [-1,-1,-1,5]

 return index, nums

 
