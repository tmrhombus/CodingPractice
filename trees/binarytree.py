
class BinaryTree:
 '''
 Binary Tree implementation
 '''
 def __init__(self, value):
  '''
  initialize node with value, no children yet
  '''
  self.value = value
  self.left_child  = None
  self.right_child = None

 def insert_left(self, value):
  '''
  If there is no left child already, 
   make a new node (BinaryTree) and insert it
  If there is a left child alraedy,
   make a new node and add the left child to
   it, then make the new node the new left child
  '''
  if self.left_child == None:
   self.left_child = BinaryTree(value)
  else:
   new_node = BinaryTree(value)
   new_node.left_child = self.left_child
   self.left_child = new_node

 def insert_right(self, value):
  '''
  If there is no right child already, 
   make a new node (BinaryTree) and insert it
  If there is a right child alraedy,
   make a new node and add the right child to
   it, then make the new node the new right child
  '''
  if self.right_child == None:
   self.right_child = BinaryTree(value)
  else:
   new_node = BinaryTree(value)
   new_node.right_child = self.right_child
   self.right_child = new_node
