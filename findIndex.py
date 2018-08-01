#find Index of given element

def findElement(A,b):
    i=0
    for i in len(A):
        if A[i]==b:
            return i
        else:
            i+=1
