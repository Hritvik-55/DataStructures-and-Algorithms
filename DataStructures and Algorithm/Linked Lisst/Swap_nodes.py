class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def Swap_Nodes(self,x,y):
        if (self.head is None):
            return
        if x==y:
            return
        '''
        Searching for x
        '''
        currX=self.head
        prevX=currX
        while(currX!=None and currX.data!=x):
            prevX=currX
            currX=currX.next
        '''
        Searching for Y
        '''
        currY=self.head
        prevY=currY
        while(currY!=None and currY.data!=y):
            prevY=currY
            currY=currY.next

        '''
        If x is Head
        '''
        if (prevX!=None):
            prevX.next=currY
        else:
            self.head=currY
        '''
        If Y is Head
        '''
        if (prevY!=None):
            prevY.next=currX
        else:
            self.head=currX

        temp=currX.next

        currX.next=currY.next
        currY.next=temp












    def push(self, new_data):

        # 1. alloc the Node and put the data
        new_Node = Node(new_data)

        # 2. Make next of new Node as head
        new_Node.next = self.head

        # 3. Move the head to point to new Node
        self.head = new_Node

        # This function prints contents of linked list starting

    # from the given Node
    def printList(self):
        tNode = self.head
        while tNode != None:
            print (tNode.data,end=" ")
            tNode = tNode.next

    # Driver program to test above function
llist = LinkedList()

# The constructed linked list is:
# 1->2->3->4->5->6->7
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
print
"Linked list before calling swapNodes() "
llist.printList()
llist.Swap_Nodes(4, 3)
print
"\nLinked list after calling swapNodes() "
llist.printList()