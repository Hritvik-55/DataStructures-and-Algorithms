class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Doubly_LinkedList:
    def __init__(self):
        self.head=None

    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        if (self.head is not None):
            self.head.prev=new_node
        self.head=new_node

    def Insert_at_end(self,new_data):
        new_node=Node(new_data)
        temp=self.head
        if(temp is None):
            new_node.prev=None
            self.head=new_node
            return
        while(temp.next is not None):
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
        return
    def Insert_after(self,prev_node,new_data):
        new_node=Node(new_data)
        if prev_node is None:
            print("Previous Node cannot be None ")
            return
        new_node.next=prev_node.next
        prev_node.next=new_node
        new_node.prev=prev_node
        if new_node.next is not None:
            new_node.next.prev=new_node

    def Insert_node_before(self,next_node,new_data):
        if (next_node is None):
            print("given Node cannot be None")
            return
        new_node=Node(new_data)
        new_node.prev=next_node.prev
        next_node.prev=new_node
        new_node.next=next_node
        if (new_node!=None):
            new_node.prev.next=new_node
        else:
            self.head=new_node


    def PrintList(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
        print()

llist=Doubly_LinkedList()
llist.push(45)
llist.Insert_at_end(12)
llist.Insert_at_end(12146)
llist.Insert_at_end(121)
llist.Insert_at_end(1212)
llist.PrintList()




