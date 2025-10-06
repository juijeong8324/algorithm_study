# Input
# nums = an integer array
# val = an integer
# Output
# the number of elements in nums which are not equal to val
# remove all occurrences of val in nums in-place
# Hint
# Element order is not important
# Just keep copying the none val elements in-place
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:  # overwrite only if nums[i] is not val
                nums[k] = nums[i]
                k = k + 1
        return k
