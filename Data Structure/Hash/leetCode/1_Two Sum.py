# Input
# nums = array of integers
# target = an integer
# Output
# indices of the two numbers such that they add up to target
# Only one valid answer exists.
# The same element may not be used twice

class Solution:
    # Brute force, O(N^2)
    def twoSum(self, nums: List[int], target: int) -> List[int]:  # O(N^2)
        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i != j and num + num2 == target:  # not use the same element twice
                    return [i, j]

    # Hash map, O(N)
    # Hint: fix one of the numbers x, find number y (value - x) in hash map
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = dict()
        for i, x in enumerate(nums):
            y = target - x
            if y in store:
                return [store[y], i]
            store[x] = i
