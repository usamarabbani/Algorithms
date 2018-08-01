def selectionSort(arr):

    for i in range(len(arr)):
        minindex=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[minindex]:
                minindex=j
        arr[i],arr[minindex]=arr[minindex],arr[i]

arr=[80,48,90,85,100,5,-98]
print(arr)
selectionSort(arr)
print(arr)