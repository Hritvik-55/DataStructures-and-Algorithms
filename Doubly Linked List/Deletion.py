import gc
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Doubly_LinkedList:
    def __init__(self):
        self.head=None

    def Deletion(self,dele_node):
        if (self.head is None or dele_node is None):
            return
        if (self.head==dele_node):
            self.head=dele_node.next

        if dele_node.next is not  None:
            dele_node.next.prev=dele_node.prev

        if dele_node.prev is not None:
            dele_node.prev.next=dele_node.next

        gc.collect()

    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        if (self.head is not None):
            self.head.prev=new_node
        self.head=new_node


    def PrintList(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
        print()


llist=Doubly_LinkedList()
llist.push(45)
llist.push(12)
llist.push(12146)
llist.push(121)
llist.push(1212)
llist.Deletion(llist.head.next)
llist.PrintList()


