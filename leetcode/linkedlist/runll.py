
import linkedlist as ll

llist = ll.MyLinkedList()

llist.addAtHead(4)
llist.addAtHead(3)
llist.addAtHead(2)
llist.addAtHead(1)
llist.addAtTail(9)

print("original list:")
llist.printList()

print("------reverse-----")
llist.reverseList()

llist.printList()
