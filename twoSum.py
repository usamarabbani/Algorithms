def twoSum(nums, target):
    if len(nums) <= 1:
        return False
    buff_dict = {}
    for i in range(len(nums)):
        if nums[i] in buff_dict:
            return [buff_dict[nums[i]], i]
        else:
            buff_dict[target - nums[i]] = i


nums=[2,4,5,7,10,14,16,78,34]
target=17

print(twoSum(nums,target))