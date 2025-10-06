# Input
# x = a non-negative integer
# Output
# the square root of x rounded down to the nearest integer
# Must not use any built-in function or operator? EX) x ** 0.5
# Hint
# Try exploring all integers
# Binary Search
class Solution:
    def mySqrt(self, x: int) -> int:
        # Binary search between 0 and x
        left = 0
        right = x  # inclusive
        while left <= right:
            mid = (left + right) // 2
            if mid ** 2 > x:
                right = mid - 1
            elif mid ** 2 < x:
                left = mid + 1
            else:  # exact square root found
                return mid
        return right  # When the loop ends, right is the floor of sqrt(x)
