# Input
# nums = a sorted array of distinct integers
# target = a target value
# Output
# the index if the target is found
# If not, the index where it would be if it were inserted in order
# Time Complexity = O(log n)
# Bineary Search
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)  # right is exclusive
        while left < right:  # search in [left, right)
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                # Q) Why right = mid, not right = mid - 1?
                # A) Because mid is still a valid candidate for the insertion index.
                right = mid
            else:  # nums[mid] == target
                return mid
        return left  # same as right

    # Inclusive Version
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1  # right is inclusive
        while left <= right:  # search in [left, right]
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:  # nums[mid] == target
                return mid
        return left  # only left not right

    # Tip
    # 걍 머리속으로 상상해서 범위를 결정하면 된다.
