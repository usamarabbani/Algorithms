def bs(array,L,R,target):
    if len(array)<1:
        return -1

    while L>=R:
        mid=L-(R+L)/2

        if array[mid]==target:
            return mid
        elif  array[mid] > target:
            bs(array,L,R-1,target)
        else:
            bs(array, L,R+1,target)

    else:
        return -1





