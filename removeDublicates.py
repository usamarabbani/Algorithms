def removeDuplicates(nums):
    print("sorted array", nums)

    if len(nums) < 2:
        return len(nums)

    j = 0

    for i in nums[1:]:
        if i != nums[j]:
            j += 1
            nums[j] = i
    return j + 1


nums=[0,0,1,2,2,4,5,6,6,7,8,9,9]



print("result",removeDuplicates(nums))


