import random
def partition(sample,start,end):
    if len(sample)<=1:
        return sample

    print("sample",sample)

    pivot=sample[end]
    index=start
    current=start
    while current<end:
        if sample[current]<=pivot:
            sample[index],sample[current]=sample[current],sample[index]
            index+=1
        current+=1
    sample[index],sample[end]=sample[end],sample[index]
    print("After partition",sample)
    return index

def quicksort(sample,start,end):
    if(start<end):
        index=partition(sample,start,end)
        quicksort(sample,start,index-1)
        quicksort(sample,index+1,end)

sample = random.sample(range(-20,100),10)
quicksort(sample,0,9)