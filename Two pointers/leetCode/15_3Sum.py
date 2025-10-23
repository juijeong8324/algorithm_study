# Input
# nums = an integer array
# Output
# all the tripltes [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets
# Hint
# We fix one of the numbers say x. we are left with the two-sum problem y + z = -x
# Two Pointers

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        n = len(nums)
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            target = -nums[i]
            j = i + 1          # Left pointer
            k = n - 1          # Right pointer

            while j < k:
                current_sum = nums[j] + nums[k]
                if current_sum == target:
                    answer.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # Skip duplicates for the second and third numbers
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1

                elif current_sum < target:
                    j += 1
                elif current_sum > target:
                    k -= 1

        return answer
