def subsets(nums):
  if nums is None: return 0
  subsets = [[]]
  next = []
  for n in nums:
    for s in subsets:
      next.append(s + [n])
    subsets += next
    next = []
  return subsets


#print(len(subsets(nums={1,4,6})))
print(subsets(nums={1,4,6}))