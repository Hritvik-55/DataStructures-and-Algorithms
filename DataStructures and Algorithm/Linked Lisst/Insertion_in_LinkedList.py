class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    '''
    Inserting in Linked List
    '''

    '''
    Inserting at the starting of the linked list
    '''
    def inserting_at_front(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node

    '''
    Inserting after a given Node
    '''

    def inserting_after_node(self,prev_node,new_data):
        new_node=Node(new_data)
        if prev_node is None:
            print("There must be a previous node to insert a node after")
            return
        new_node.next=prev_node.next
        prev_node.next=new_node

    '''
    Inserting a Node at the end of the Linked List
    '''
    def insert_at_end(self,new_data):
         new_node=Node(new_data)
         if self.head is None:
             self.head=new_node
             return
         last_node=self.head
         while(last_node.next):
             last_node=last_node.next

         last_node.next=new_node
         new_node.next=None

    '''
    Printing the whole Linked List
    '''
    def PrintList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
llsit=LinkedList()
llsit.insert_at_end(1)
llsit.inserting_at_front(55)
llsit.inserting_after_node(llsit.head.next,45)
llsit.insert_at_end(455)
llsit.inserting_after_node(llsit.head.next.next.next,5564)
llsit.PrintList()


