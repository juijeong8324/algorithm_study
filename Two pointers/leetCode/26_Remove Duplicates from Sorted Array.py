# Input
# nums = an integer array sorted in non-decreasing order
# Output
# modify the array in-place
# nums such that each unique element appears only once
# relative order of the elements should be kept the same
# Hint
# Overwriting, Two Pointer

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0  # write
        k = 1

        for j in range(len(nums)):  # read
            if nums[i] == nums[j]:
                continue

            i = i+1
            nums[i] = nums[j]
            k = k+1

        return k
