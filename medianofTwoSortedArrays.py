def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1)%2 == 0:
            return (nums1[(len(nums1)//2)-1]+nums1[len(nums1)//2])/2
        else:
            return nums1[(len(nums1)//2)]/1

nums1=[1,4,7,8,22,55,78]
nums2=[2,4,11,52,67,99,195]
print(findMedianSortedArrays(nums1,nums2))