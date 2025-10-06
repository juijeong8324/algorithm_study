# Input
# nums1, nums2 = two integer array sorted in increasing order
# m, n = representing the number of elements in nums1 and nums2 respectively
# Output
# Merge nums1 and nums2 into a single array sorted in increasing order
# Be sorted inside the array nums1, EX) nums1 = [1,2,3,0,0,0]
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1 # for nums1
        j = n-1 # for nums2
        k = n+m-1 # for zero 
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i = i - 1
            else:
                nums1[k] = nums2[j]
                j = j - 1
            k = k - 1
        
        # if nums2 remain, copy them in front
        if j >= 0:
            nums1[:j+1] = nums2[:j+1]