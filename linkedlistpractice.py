class Node:
    def __init__(self,data,pointer):
        self.data=data
        self.pointer=None
class LinkedList:
    def __init__(self,pointer):
        self.start=None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def traverse(self):
        node=self
        while node!=None:
            print (node.data)
            node=node.pointer



llist=LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

print.print_list()

