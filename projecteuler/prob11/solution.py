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

 doprint = False

 for i in range(hlen):
  for j in range(vlen):

   if(doprint):
    print(" ({},{})={}".format(i,j,grid[i][j]))

   # check horizontally
   if (i <= hlen - n):
    if(doprint):
     print("  h: {}".format(prod(i,j,1,0,n,grid)))
    p,tempnum = prod(i,j,1,0,n,grid)
    if (p>maxprod):
     maxprod = p
     index=[i,j]
     nums=tempnum
     nums.append(maxprod)
     index.append("horizontal")
   # check vertically
   if (j <= vlen - n):
    if(doprint):
     print("  v: {}".format(prod(i,j,0,1,n,grid)))
    p,tempnum = prod(i,j,0,1,n,grid)
    if (p>maxprod):
     maxprod = p
     index=[i,j]
     nums=tempnum
     nums.append(maxprod)
     index.append("vertical")
   # check diag up
   if (i <= hlen-n and j <= vlen - n):
    if(doprint):
     print("  du: {}".format(prod(i,j,1,1,n,grid)))
    p,tempnum = prod(i,j,1,1,n,grid)
    if (p>maxprod):
     maxprod = p
     index=[i,j]
     nums=tempnum
     nums.append(maxprod)
     index.append("diagonal up")
   # check diag down
   if (i >= n and j <= vlen - n): 
    if(doprint):
     print("  dd: {}".format(prod(i,j,-1,1,n,grid)))
    p,tempnum = prod(i,j,-1,1,n,grid)
    if (p>maxprod):
     maxprod = p 
     index=[i,j]
     nums=tempnum
     nums.append(maxprod)
     index.append("diagonal down")

  if(doprint):
   print("\n")


 return index, nums

 

def prod(i,j,di,dj,n,grid):
 p = 1 
 nums = []
 for k in range(n):
  p *= grid[i+k*di][j+k*dj]
  nums.append(grid[i+k*di][j+k*dj])

 return p,nums
