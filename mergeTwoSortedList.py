# Defining class which will create nodes for our linked lists
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Defining class which will create our linked list and also defining some methods
class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):                # Method to print linked list
        temp = self.head
        while temp:
            print (temp.data)
            temp = temp.next

    def append(self, new_data):         # Method to add node at the end of the linked list
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node


# Defining function which will merge our linked lists
def mergeLists(l1, l2):             
    temp = None
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l1.data <= l2.data:
        temp = l1
        temp.next = mergeLists(l1.next, l2)
    else:
        temp = l2
        temp.next = mergeLists(l1, l2.next)

    return temp

# The main logic starts from here
if __name__ == '__main__':

    list1 = LinkedList()                # Creating linked list 1
    list1.append(10)                    # Assigning values to linked list 1 in sorted manner
    list1.append(20)
    list1.append(30)
    list1.append(40)
    list1.append(50)

    list2 = LinkedList()                # Creating linked list 2
    list2.append(5)                     # Assigning values to linked list 2 in sorted manner
    list2.append(15)
    list2.append(25)
    list2.append(35)
    list2.append(45)

    print ("Printing Linked List 1")
    list1.printList()                   # Printing linked list 1
    print ("Printing Linked List 2")
    list2.printList()                   # Printing linked list 2

    list3 = LinkedList()                # Creating linked list 3

# Merging linked list 1 and linked list 2 in linked list 3
    list3.head = mergeLists(list1.head, list2.head)

    print ("Printing Linked List 3")
    list3.printList()                   # Printing linked list 3