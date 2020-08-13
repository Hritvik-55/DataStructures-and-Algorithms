class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def Length_of_LinkedList(self):
        temp=self.head
        count=0
        while(temp):
            count+=1
            temp=temp.next
        return  count
    def Insert_at_front(self,new_data):
        new_node=Node(new_data)
        temp=self.head
        if (self.head is None):
            return
        self.head=new_node
        new_node.next=temp

    def Insert_at_End(self,new_data):
        new_node=Node(new_data)

        if (self.head is None):
            self.head=new_node

            return
        temp=self.head
        while(temp.next is None):

            temp=temp.next

        temp.next=new_node
        new_node.next=None

    def Insert_after_node(self,prev_node,new_data):
        new_node=Node(new_data)
        if prev_node is None:
            print("No such Node found in Linked List")
            return
        new_node.next=prev_node.next
        prev_node.next=new_node

    def Delete_By_key(self,key):
        temp=self.head
        if (self.head is None):
            print("Linked Lisst is Empty")
            return
        if (temp.data==key):
            self.head=temp.next
            temp=None
            return
        while (temp is not  None):
            if (temp.data == key):
                break
            prev=temp
            temp=temp.next

        if (temp==None):
            return
        prev.next=temp.next
        temp=None

    def Delete_By_Position(self,position):
        temp=self.head
        if (self.head is None):
            print("Linked List Empty")
            return
        if (position ==0):
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
        temp=None

    def PrintList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
            






