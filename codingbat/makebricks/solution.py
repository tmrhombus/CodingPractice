

def solution(nl, nb, goal):
 """
 nl = nr little bricks
 nb = nr big bricks
 goal = desired length
 """

 # ll = length of little brick
 lenl = 1
 # lb = length of big brick
 lenb = 5

 # case 0: big bricks fill it all
 if( lenb*nb == goal):
  return True

 # case 1: more than enough big bricks
 # Then 
 elif( lenb*nb > goal):
  nl_needed = goal % lenb
  if (nl_needed <= nl):
   return True
  else:
   return False

 else:
  nl_needed = goal - (nb*lenb)
  if (nl_needed <= nl):
   return True
  else:
   return False
  




  
