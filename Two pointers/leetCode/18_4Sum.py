# Input
# nums = an array of n integers
# Output
# an array of all the unique quadruplets
# 0 <= a,b,c,d < n
# a,b,c and d are distinct
# nums[a] + nums[b] + nums[c] + nums[d] == target
# Hint
# Two Pointers, Sort

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        answer = []

        for a in range(n):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a+1, n):
                if b > a+1 and nums[b] == nums[b-1]:
                    continue
                new_target = target - nums[a] - nums[b]

                c = b + 1
                d = n - 1
                while c < d:

                    if new_target == nums[c] + nums[d]:
                        answer.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                        # Skip Duplicates
                        while c < d and nums[c] == nums[c-1]:
                            c += 1
                        while c < d and nums[d] == nums[d+1]:
                            d -= 1
                    elif new_target < nums[c] + nums[d]:
                        d -= 1
                    else:
                        c += 1

        return answer
