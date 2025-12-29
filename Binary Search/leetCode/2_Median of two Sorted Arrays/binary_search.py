# Input
# nums1 = sorted arrays (size = m)
# nums2 = sorted arrays (size = n)
# Output
# median of the two sorted arrays
# Time Complexity should be O(log(m+n))
# Hint
# Binary Search: Find the partition(= mid) each array
# Condition: The points Where all elems on the left are smaller than all elmes on the right across both arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):  # Ensure half in nums2
            return self.findMedianSortedArrays(nums2, nums1)  # Swap

        # Initialize
        m = len(nums1)
        n = len(nums2)
        left_size = (m+n+1) // 2  # Calculate the left partition size
        # Why +1? = To ensure median (max_left) is in left partition when total_len is odd

        # Set up for Binary Search
        low, high = 0, m
        while low <= high:
            # Partition both arrays
            # mid1 = The number of elems on the left side of nums1
            # mid2 = The number of elems on the right side of nums2
            mid1 = (low+high) // 2
            mid2 = left_size - mid1  # mid1 + mid2 = left_size

            max_left1 = -1e6 if mid1 == 0 else nums1[mid1-1]
            min_right1 = 1e6 if mid1 == m else nums1[mid1]

            max_left2 = -1e6 if mid2 == 0 else nums2[mid2-1]
            min_right2 = 1e6 if mid2 == n else nums2[mid2]

            # Check validation
            # max_left <= min_right across both arrays
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # Median calculation
                if (m+n) % 2 == 0:  # even
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                else:  # odd
                    return max(max_left1, max_left2)
            # If Not - Update parition (Binary Search)
            elif max_left1 > min_right2:
                high = mid1 - 1
            else:
                low = mid1 + 1

        return 0
