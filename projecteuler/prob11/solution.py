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
 hlen = len(grid[0])
 vlen = len(grid)

 for j in range(vlen):
  for i in range(hlen):

   # check horisontally
   if (i <= hlen - n):
    #print(grid)
    print(i)
   #print(grid[i][j])

 index = [-1,-1]
 nums = [-1,-1,-1,5]

 return index, nums

 

def prod(i,j,di,dj,n,grid):
 p = 1 
 for k in range(n):
  p *= grid[j+k*dj][i+k*di]
 return p 
