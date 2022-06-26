

# Node class
class Node:
  
 # Function to initialize the node object
 def __init__(self, data):
  self.data = data  # Assign data
  self.next = None  # Initialize
                       # next as null
  
class MyLinkedList:

 def __init__(self):
  self.head = None
  self.count = 0
     
 def printList(self):
  print("{} elements".format(self.count))
  temp = self.head
  while (temp):
   print (temp.data)
   temp = temp.next

 def get(self, index: int) -> int:
  if(index>self.count):
   return None
  curnode = self.head
  for i in range(index):
   curnode = curnode.next
   #print("current node: {}".format(curnode.data))
  return(curnode.data)
  
     

 def addAtHead(self, val: int) -> None:
  # allocate node, add data
  new_node = Node(val)
     
  # make new node point to old head
  new_node.next = self.head

  # move head to point to new node
  self.head = new_node

  # add one to count
  self.count += 1

 def addAtTail(self, val: int) -> None:
  # allocate node, add data
  new_node = Node(val)

  # add one to count
  self.count += 1

  # if linked list is empty,
  # this is now the head
  if self.head is None:
   self.head = new_node
   return

  # if list is not empty,
  # traverse until the end
  else:
   # start at head
   last = self.head
   # keep going until nothing next
   while(last.next):
    last = last.next

   last.next = new_node
     

# def addAtIndex(self, index: int, val: int) -> None:
#     
#
# def deleteAtIndex(self, index: int) -> None:
        


 
# Code execution starts here
if __name__=='__main__':
 
    # Start with the empty list
    llist = MyLinkedList()
 
    llist.addAtHead(3)
    llist.addAtHead(4)

    llist.addAtTail(1)
    llist.addAtTail(7)

    for i in range(3):
     print("i={}, data={}".format(i,llist.get(i)))

    llist.printList()

#    llist.head = Node(1)
#    second = Node(2)
#    third = Node(3)
# 
#    llist.head.next = second; # Link first node with second
#    second.next = third; # Link second node with the third node
# 
#    llist.printList()



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


