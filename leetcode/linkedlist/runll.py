
import linkedlist as ll

llist = ll.MyLinkedList()

llist.addAtIndex(1,0)
llist.get(0)
llist.addAtHead(4)
llist.addAtHead(3)
llist.addAtHead(2)
llist.addAtHead(1)
for i in range(llist.count):
 print("i={}, data={}".format(i,llist.get(i)))
