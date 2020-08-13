class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def Finding_Element(self,element):
        temp=self.head
        if (self.head is None):
            print("Linked List IS Empty")
            return

        while(temp):
            if(temp.data == element):
                return True

            temp=temp.next

        if (temp is None):
            return  False

    def PrintList(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next


llist=LinkedList()
llist.head=Node(1)
second=Node(2)
third=Node(3)
llist.head.next=second
second.next=third
llist.PrintList()
print(llist.Finding_Element(200))



