

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
     
 def printList(self):
  temp = self.head
  while (temp):
   print (temp.data)
   temp = temp.next

# def get(self, index: int) -> int:
#     
#
 def addAtHead(self, val: int) -> None:
  new_node = Node(val)
     

# def addAtTail(self, val: int) -> None:
#     
#
# def addAtIndex(self, index: int, val: int) -> None:
#     
#
# def deleteAtIndex(self, index: int) -> None:
        


 
# Code execution starts here
if __name__=='__main__':
 
    # Start with the empty list
    llist = MyLinkedList()
 
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
 
    llist.head.next = second; # Link first node with second
    second.next = third; # Link second node with the third node
 
    llist.printList()



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


