import gc
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Doubly_LinkedList:
    def __init__(self):
        self.head=None

    def Reverse(self):
        curr=self.head
        temp=None
        while(curr is not None):
            temp=curr.prev
            curr.prev=curr.next
            curr.next=temp
            curr=curr.prev
        if (temp is not None):
            self.head=temp.prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if (self.head is not None):
            self.head.prev = new_node
        self.head = new_node

    def PrintList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()


llist=Doubly_LinkedList()
llist.push(45)
llist.push(12)
llist.push(12146)
llist.push(121)
llist.push(1212)
llist.PrintList()
llist.Reverse()
llist.PrintList()
