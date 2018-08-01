def maxSubarray(array):
    max_so_far=0
    max_ends_here=array[0]
    for i in len(array):
        max_so_far=max_so_far+array[0]
        if max_so_far < max_ends_here:
           max_so_far =max_ends_here
        elif max_ends_here<0:
            max_ends_here=0


