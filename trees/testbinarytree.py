import binarytree as bt


## example of a simple tree
##    a
##   / \ 
##  b   c
##  \  / \
##  d  e  f
#
#
#a_node = bt.BinaryTree('a')
#a_node.insert_left('b')
#a_node.insert_right('c')
#
#b_node = a_node.left_child
#b_node.insert_right('d')
#
#c_node = a_node.right_child
#c_node.insert_left('e')
#c_node.insert_right('f')
#
#d_node = b_node.right_child
#e_node = c_node.left_child
#f_node = c_node.right_child
#
#print(a_node.value) # a
#print(b_node.value) # b
#print(c_node.value) # c
#print(d_node.value) # d
#print(e_node.value) # e
#print(f_node.value) # f


# make test tree structured as
#        1
#       / \
#     2     5
#    / \   / \
#   3   4 6   7


root = bt.BinaryTree(1)
root.insert_left(2)
root.insert_right(5)

twonode = root.left_child
twonode.insert_left(3)
twonode.insert_right(4)

threenode = twonode.left_child

fournode = twonode.right_child

fivenode = root.right_child
fivenode.insert_left(6)
fivenode.insert_right(7)

sixnode = fivenode.left_child
sevennode = fivenode.right_child

print("Pre Order")
root.pre_order()
print("\n")

print("In Order")
root.in_order()
print("\n")

print("Post Order")
root.post_order()
print("\n")


