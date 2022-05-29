import math 

def solution( n, grid ):
 """
 returns the largest product of n sequential numbers
 where sequential can mean horizontal, vertical, diagonal

 method:
 work top to bottom, left to right
 at grid point (i,j) only check right,down,downward diagonals
 """

 for i in range(len(grid[0])):
  for j in range(len(grid[0])):
   print(grid[i][j])

 index = [-1,-1]
 nums = [-1,-1,-1,5]

 return index, nums

 
