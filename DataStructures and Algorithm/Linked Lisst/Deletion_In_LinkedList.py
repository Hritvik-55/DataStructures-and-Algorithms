class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def Inserting_at_front(self,new_data):
        new_node=Node(new_data)

        new_node.next=self.head
        self.head=new_node

    def Deleting(self,key):
        temp=self.head
        if(temp is not  None):
            if (temp.data==key):
                self.head=temp.next
                temp=None
                return
        while (temp is not  None):
            if (temp.data==key):
                break

            prev=temp
            temp=temp.next
        if (temp==None):
            return 
        prev.next=temp.next
        temp=None

    def Delete_by_position(self,position):
        if self.head==None:
            return
        temp=self.head

        if (position==0):
            self.head=temp.next
            temp=None
            return
        for i in range(position-1):
            temp=temp.next
            if temp is None:
                break
        if temp is None:
           return
        if temp.next is None:
           return
        prev=temp
        next_of_temp=temp.next.next
        prev.next=next_of_temp
        temp.next=None

    def PrintList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

llist=LinkedList()
llist.head=Node(1)
llist.Inserting_at_front(45)
llist.Inserting_at_front(454)
llist.Delete_by_position(2)
llist.PrintList()


