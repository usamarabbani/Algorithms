# Python program to swap two given nodes of a linked list
class LinkedList(object):
    def __init__(self):
        self.head = None

     # head of list
    class Node(object):
        def __init__(self, d):
            self.data = d
            self.next = None

    # Function to swap Nodes x and y in linked list by
    #  changing links
    def swapNodes(self,x,y):

        #nothing to d if x and y are same
        if x==y:
            return

        #search for x(keep track of prevX and CurrX)
        prevX = None
        currX = self.head
        while currX!=None and currX.data !=x:
            prevX=currX
            currX=currX.next


        #search for y (keep track of prevY and currY)
        prevY= None
        currY=self.head
        while currY!=None and currY.data !=y:
            prevY=currYcurrY=currY.next

        #if either x or y is not present, nothing to do
        if currX==None or Curry==None:
            return

        #if x is not head of linked list
        if prevX!=None:
            prevX.next=currY
        else: #male y he new head
            self.head=currY
            #if y is not head of linked list
        if prevY!=None:
            prevY.next = currX
        else: #make x the new head
            self.head=currX

        #swap next pointers
        temp=currX.next
        currX.next=currY.next
        currY.next=temp

    #function to add node at beginning of lsit
    def pish(self,new_data):

        #1.alloc the node and ut the data
        new_Node=self.node(new_data)

        #2. make next of new Node as head
        new_Node.next = self.head

        #3.move the head to point to new Node
        self.head= new_Node







