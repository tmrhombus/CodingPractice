from typing import List
from collections import OrderedDict

class Solution:
 def isValidSudoku(self, board: List[List[str]]) -> bool:

  ## check rows
  for row in range(9):
   thisrow = set()   
   for col in range(9):
    val = board[row][col] 
    if val != ".":
     if val not in thisrow:
      thisrow.add(val)
     else:
      return False

  ## check columns
  for col in range(9):
   thiscol = set()   
   for row in range(9):
    val = board[row][col] 
    if val != ".":
     if val not in thiscol:
      thiscol.add(val)
     else:
      return False
  
  ### check squares
  #thissq = set()
  #for row in range(3):
  # for col in range(3):
  #  val = board[row][col]
  #  if val != ".":
  #   if val not in thissq:
  #    thissq.add(val)
  #   else:
  #    return False

  #print(self.checkSquare(board, 0, 3, 0, 3))
  #print(self.checkSquare(board, 0, 3, 3, 6))
  #print(self.checkSquare(board, 0, 3, 6, 9))
  #print(self.checkSquare(board, 3, 6, 0, 3))
  #print(self.checkSquare(board, 3, 6, 3, 6))
  #print(self.checkSquare(board, 3, 6, 6, 9))
  #print(self.checkSquare(board, 6, 9, 0, 3))
  #print(self.checkSquare(board, 6, 9, 3, 6))
  #print(self.checkSquare(board, 6, 9, 6, 9))

  return(
   (self.checkSquare(board, 0, 3, 0, 3)) and
   (self.checkSquare(board, 0, 3, 3, 6)) and
   (self.checkSquare(board, 0, 3, 6, 9)) and
   (self.checkSquare(board, 3, 6, 0, 3)) and
   (self.checkSquare(board, 3, 6, 3, 6)) and
   (self.checkSquare(board, 3, 6, 6, 9)) and
   (self.checkSquare(board, 6, 9, 0, 3)) and
   (self.checkSquare(board, 6, 9, 3, 6)) and
   (self.checkSquare(board, 6, 9, 6, 9))
  )

 def checkSquare(self, board: List[List[str]], row_s: int, row_e: int, col_s: int, col_e: int) -> bool:
  #print(f"row: [{row_s},{row_e}] col: [{col_s},{col_e}]")

  ## check squares
  thissq = set()
  for row in range(row_s, row_e):
   for col in range(col_s, col_e):
    val = board[row][col]
    if val != ".":
     if val not in thissq:
      thissq.add(val)
     else:
      return False

  return True


