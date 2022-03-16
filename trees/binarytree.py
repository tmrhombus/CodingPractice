
class binarytree:
 '''
 Binary Tree implementation
 '''
 def __init__(self, value):
  '''
  initialize node with value, no children yet
  '''
  self.value = value
  self.leftchild  = None
  self.rightchild = None

 def insertleft(self, value):
  '''
  If there is no left child already, 
   make a new node (binarytree) and insert it
  If there is a left child alraedy,
   make a new node and add the left child to
   it, then make the new node the new left child
  '''
  if self.leftchild == None:
   self.leftchild = binarytree(value)
  else:
   newnode = binarytree(value)
   newnode.leftchild = self.leftchild
   self.leftchild = newnode
