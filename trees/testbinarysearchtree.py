
import binarysearchtree as bst


thelist = [50, 76, 21, 4, 32, 100, 64, 52]


mytree = bst.BinarySearchTree(thelist[0])
for i in range(len(thelist)-1):
 mytree.insert_node(thelist[i+1])


num = 6
found = mytree.find_node(num)
print("The number {} is in tree: {}".format(num,found))

