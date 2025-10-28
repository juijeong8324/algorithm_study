# Input
# nums = an integer array, length n
# target = an integer
# Output
# the sum of the three integers
# three integers in nums such that the sum is closet to target
# each input would have exactly one solution.
# Hint
# Two Pointers, Sort
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        answer = 0  # Max
        diff = 1e9
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = n-1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                new_diff = abs(target-temp)
                if new_diff < diff:
                    answer = temp
                    diff = new_diff

                if temp < target:
                    j += 1  # Note) Eacth input would have exactly one solution
                elif temp > target:
                    k -= 1
                else:  # same
                    return temp

        return answer
