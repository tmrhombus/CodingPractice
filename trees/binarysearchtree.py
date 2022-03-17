
# Binary Search Tree

class BinarySearchTree:
 '''
 Binary tree (each node can only have two children)
 All values for right children are greater than 
  parent nodes
 All values for left children are less than parent nodes
 '''
 def __init__(self, value):
  '''
  Initialize root node with no children
  '''
  self.value = value
  self.left_child = None
  self.right_child = None

 def insert_node(self, value):
  ''' Node insertion '''
  if value <= self.value and self.left_child:
   # If value <= node, and there is a left child node
   #  go to left child node and recursively call insert
   self.left_child.insert_node(value)
  elif value <= self.value:
   # if value <= node and no left child
   #  make a new left child with value
   self.left_child = BinarySearchTree(value)
  elif value > self.value and self.right_child:
   # If value > node and there is a right child node
   #  go to right child and recursively call insert
   self.right_child.insert_node(value)
  else:
   # if value > node and there is no right child
   #  make a new right child with value
   self.right_child = BinarySearchTree(value)


