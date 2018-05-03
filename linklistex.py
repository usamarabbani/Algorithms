'''def remove_dup(self):
    cur=self.head
    prev=None

    dup_vlaues = dict()

    while cur is not None:
        if cur.data in dup_values:
            #remove Node:
            prev.next=cur.next
            cur = None
        else:
            dup_values[cur.data]=1
            prev=cur
        cur=prev.next'''