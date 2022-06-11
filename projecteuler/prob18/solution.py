
def solution( triangle ):
 """
 returns the maximum sum following a path through <triangle>

 method:
 dynamic programming
 start at bottom
 for each row above, add larger of two adjacent options
 """


 for i in reversed( range( len( triangle )-1 ) ):
  for j in range(len(triangle[i])):

   tba = max( triangle[i+1][j], triangle[i+1][j+1] )
   triangle[i][j] += tba

 print(triangle)
 thesum = triangle[0][0]

 return thesum
