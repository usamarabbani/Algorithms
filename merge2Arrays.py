#Given 2 sorted Arrays merge array B into A When A has enough Buffer space for B.
#eample: A= [1,NA,3,5,NA,8,NA]
#B=[2,4,10]
#first move all element in A at the end of the array.
#A=[NA,NA,NA,1,3,5,8]
#now merge B into A by check every element in A and B.
#A=[1,2,3,4,5,8,10]

NA=-1

def moveToEnd(A,size):
    i=0
    j=size-1
    for i in range(size-1,-1,-1):
        if (A[i]!=NA):
            A[j]=A[i]
            j-=1


def merge(A,m,B,n)
    i=m-1
    j=n-1
    k=m+n-1
    while (k>0):
        if (j<0 ||(i>=0 && A[i]>B[j])):
            A[k--]=A[i--]
        else:
            A[k--]=B[j--]


