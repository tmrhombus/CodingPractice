
#https://www.freecodecamp.org/news/all-you-need-to-know-about-tree-data-structures-bceacb85490c/

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

 #### Depth First Search Algos
 # an example tree looks like
 # 
 #        1
 #       / \
 #     2     5
 #    / \   / \
 #   3   4 6   7

 def pre_order(self):
  '''
  Look left, left, left, until hitting leaf
   then backtrack up, go right, recurse
  Result on test tree: 1 2 3 4 5 6 7
  '''
  print(self.value)
 
  if self.left_child:
   self.left_child.pre_order()
 
  if self.right_child:
   self.right_child.pre_order()

 def in_order(self):
  '''
  Look left, then node, then right
  Result on test tree: 3 2 4 1 6 5 7
  '''
  if self.left_child:
   self.left_child.in_order()

  print(self.value)

  if self.right_child:
   self.right_child.in_order()

 def post_order(self):
  '''
  Look left, then right, then up to node
  Result on test tree: 3 4 2 6 7 5 1
  '''
  if self.left_child:
   self.left_child.post_order()

  if self.right_child:
   self.right_child.post_order()

  print(self.value)







