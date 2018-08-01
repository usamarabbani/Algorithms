def reverseArray(arr):
    if len(arr)<=1:
        return arr
    n=len(arr)
    i=0
    j=n-1
    while arr[i] <arr[j]:
        swap(arr[i],arr[j])

        ++i
        --j

        return arr

def swap(arr,i,j):
    temp=arr[i]
    arr[i]=arr[j]
    arr[j]=temp

l=[8,2,5,100,3,50]
print(reverseArray(l))