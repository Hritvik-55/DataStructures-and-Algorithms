class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def traversal(self):
        temp=self.head
        while (temp):
            print(temp.data)
            temp=temp.next

llsit=LinkedList()
llsit.head=Node(1)
second=Node(2)
third=Node(3)
llsit.head.next=second
second.next=third
llsit.traversal()