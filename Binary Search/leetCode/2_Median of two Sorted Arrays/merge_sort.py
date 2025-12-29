# Input
# nums1 = sorted arrays (size = m)
# nums2 = sorted arrays (size = n)
# Output
# median of the two sorted arrays
# Time Complexity should be O(log(m+n))
# Idea
# Merge Sort = 1.Given Sorted Arrays, Using two Pointers
# But Time COmplexity is O(m+n)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = 0 # pointers for nums1
        j = 0 # pointers for nums2
        m = len(nums1)
        n = len(nums2)
        arr = [] # Merged Array

        while i != m and j != n:
            if nums1[i] <= nums2[j]:
                arr.append(nums1[i])
                i += 1
            else:
                arr.append(nums2[j])
                j += 1
            
        if i is not m:
            arr += nums1[i:]
        if j is not n:
            arr += nums2[j:]

        mid = 0
        s = m + n
        mid = s // 2
        if s % 2 == 0:
            print((arr[mid] + arr[mid-1]))
            return (arr[mid] + arr[mid-1]) / 2
        else:
            return arr[mid]