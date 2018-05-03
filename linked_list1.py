class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

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

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print("Previous node is not in the list")
            return

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        #delete node at the beginning of the list

        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        #delete node between two nodes

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):

        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        count = 1
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def sum_two_lists(self,llist):
        p = self.head
        q=llist.head

        sum_llist=LinkedList()

        carry=0
        while p or q:
            if not p:
                i=0
            else:
                i=p.data
            if not q:
                j=0
            else:
                j=q.data
            s = i+j+carry
            print("S:" +str(s))
            if s>=10:
                carry =1
                remainder = s%10
                sum_llist.append(remainder)
            else:
                carry=0
                sum_llist.append(s)
            if p:
                p =p.next
            if q:
                q=q.next
        sum_llist.print_list()

# 3 6 5
# 2 4 8
# - - -
# 6 1 3
llist1 = LinkedList()
llist1.append(5)
llist1.append(6)
llist1.append(3)

llist2 = LinkedList()
llist2.append(8)
llist2.append(4)
llist2.append(2)

print(365+248)
llist1.sum_two_lists(llist2)

#llist.delete_node("B")
#llist.delete_node_at_pos(0)

#llist.print_list()