nums=[1,2,3,1,2,2,2]
ans =0
for i in range(len(nums)):
    ans ^=nums[i]

print(ans)