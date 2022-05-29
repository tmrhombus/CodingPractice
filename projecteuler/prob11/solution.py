import math 

def solution( n, grid ):
 """
 returns the largest product of n sequential numbers
 where sequential can mean horizontal, vertical, diagonal

 method:
 use rotated coordinate system
 at grid point (i,j) only check right,down,downward diagonals
 """

 maxprod = -1
 hlen = len(grid)
 vlen = len(grid[0])

 for i in range(hlen):
  for j in range(vlen):

   # check horisontally
   if (i <= hlen - n):
    print(" ({},{})={}".format(i,j,grid[i][j]))
    print("  {}".format(prod(i,j,1,0,n,grid)))
    #print(grid)
    #print(i)
   #print(grid[i][j])
  print("\n")

 index = [-1,-1]
 nums = [-1,-1,-1,5]

 return index, nums

 

def prod(i,j,di,dj,n,grid):
 p = 1 
 for k in range(n):
  p *= grid[i+k*di][j+k*dj]
 return p 
