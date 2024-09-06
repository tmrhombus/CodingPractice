from typing import List

class Solution:
 def rotate(self, matrix: List[List[int]]) -> None:
  """
  Do not return anything, modify matrix in-place instead.
  """

  n = len(matrix)
  if n == 1: return

  # transpose
  for i in range(n): 
   for j in range(i+1,n):
    #print(f"i {i}, j {j}, m[i][j] {matrix[i][j]}, opp {matrix[n-1-i][n-1-j]}")
    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
  
  # reflect
  for i in range(n):
   for j in range(n//2):
    matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]

  
        
