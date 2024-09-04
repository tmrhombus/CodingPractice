from typing import List

class Solution:
 def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

  m = len(matrix)    ## nr rows
  n = len(matrix[0]) ## nr columns

  out = m*n*[-1]

  ## wall positions
  lw_pos = -1
  tw_pos = 0
  rw_pos = n
  bw_pos = m

  ## directions
  L, R, U, D = 1,2,3,4
  cur_dir = R

  i = 0
  cur_i = 0 # row index
  cur_j = 0 # column index

  while i < m*n:
   if cur_dir == R: 
    while cur_j < rw_pos:
     out[i] = matrix[cur_i][cur_j]
     i+=1
     cur_j+=1
    cur_dir = D
    cur_i += 1
    cur_j -= 1
    rw_pos -= 1
   elif cur_dir == D:
    while cur_i < bw_pos:
     out[i] = matrix[cur_i][cur_j]
     i+=1
     cur_i += 1
    cur_dir = L
    cur_j -= 1
    cur_i -= 1
    bw_pos -= 1
   elif cur_dir == L:
    while cur_j > lw_pos:
     out[i] = matrix[cur_i][cur_j]
     i+=1
     cur_j -= 1
    cur_dir = U
    cur_j += 1
    cur_i -= 1
    lw_pos += 1
   else:
    while cur_i > tw_pos:
     out[i] = matrix[cur_i][cur_j]
     i+=1
     cur_i -= 1
    cur_dir = R
    cur_j += 1
    cur_i += 1
    tw_pos += 1
     
  return out
        
