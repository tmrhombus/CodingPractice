
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
  if(index>=self.count):
   return -1 # why is this better???
   #return None
  curnode = self.head
  if(index==0):
   return curnode.data
  else:
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
  return

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
   return

 def addAtIndex(self, index: int, val: int) -> None:

  if(index>self.count):
   return

  if(index==self.count):
   self.addAtTail(val)
   return
  
  if(index==0):
   self.addAtHead(val)
   return

  prevnode = self.head
  for i in range(index-1):
   prevnode = prevnode.next

  newnode = Node(val)
  newnode.next = prevnode.next
  prevnode.next = newnode
  self.count += 1
  
 def deleteAtIndex(self, index: int) -> None:
  if(index>=self.count):
   return

  prevnode = self.head
  for i in range(index-1):
   prevnode = prevnode.next

  if(index==0):
   self.head = prevnode.next
   
  else:
   delnode = prevnode.next
   nextnode = delnode.next

   prevnode.next = nextnode
  self.count -= 1

 def reverseList(self) -> None:

  # start at head
  curnode = self.head

  # loop through each node
  # keep going as long as there is something next
  while(curnode.next):

   nextnode = curnode.next
   overnode = nextnode.next
   print("curnode: {}, nextnode: {}, overnode: {}".format(curnode.data,nextnode.data,-1))
   curnode = curnode.next
#  for index in range(self.count):
#   print(index)
#   nextnode = curnode.next
#   if(curnode.next):
#    self.addAtHead(curnode.next.data)
#    self.deleteAtIndex(index+1)
#    curnode = curnode.next


# Code execution starts here
if __name__=='__main__':
 
 # Start with the empty list
 llist = MyLinkedList()
 
 llist.addAtIndex(1,0)
 llist.get(0)

# llist.addAtHead(4)
# llist.addAtHead(3)
# llist.addAtHead(2)
# llist.addAtHead(1)
#
# for i in range(llist.count):
#  print("i={}, data={}".format(i,llist.get(i)))
#
# llist.addAtIndex(2,9)
#
# print("-----------")
# for i in range(llist.count):
#  print("i={}, data={}".format(i,llist.get(i)))

# llist.deleteAtIndex(0)
# 
# print("-----------")
# for i in range(llist.count):
#  print("i={}, data={}".format(i,llist.get(i)))

 print("-----------")
 llist.printList()

