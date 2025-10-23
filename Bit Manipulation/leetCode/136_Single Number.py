# Input
# nums = a non-empty array of integers
# every element appears twice except for one
# Output
# Find that single one
# Must Implement a solution with a linear runtime complexity and use only constant extra space
# Hint
# XOR (^) operator's property
# XOR satisfies the Commutative and Associative properties
# By XORing all elements, the duplicate numbers (A ^ A) will cancel each other out to 0,
# Leaving only the single unique number (X ^ 0 = X).
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            answer = answer ^ num

        return answer
