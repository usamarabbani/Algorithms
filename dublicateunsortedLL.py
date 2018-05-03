#remove duplicate from list
'''ls1= [1,1,2,2,10,45,3,3,4,5,5,6,6,7,7,7,7,8,9,9,10,10]
print(ls1)
ls2 = set(ls1)
print (ls2)

'''


"""lis1=[2,3,2,423,42,3,2,2,2,1,3,4,5,6,4,3,2,23,42,3,42,4,25,24,23,423,423,423,4]
lis2=[]
for i in lis1:
    if i not in lis2:
        lis2.append(i)
print (lis2)"""



node=[3,3,4,1,2,5,5,4,4,4,4,8,10,12]
def twoone(node):
    '''
    Write code to remove duplicates from an unsorted linked list.
    '''
    seen = set()
    prev = None
    while node is not None:
        if node.value in seen:
            prev.next = node.next
        else:
            seen.add(node.value)
        prev = node
        node = node.next

print(twoone(node))