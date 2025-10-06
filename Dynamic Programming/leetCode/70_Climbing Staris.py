# Input
# n = steps to reach the top
# Output
# How many distint ways can you climb to the top?
# Each time you can either climb 1 or 2 steps
# Hint
# To reach nth step, What could have been your previous steps?
# Dynamic Programming
class Solution:
    def climbStairs(self, n: int) -> int:
        # Base cased
        if n == 1 or n == 2:
            return n

        # dp[i] = number to reach step i
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        dp[2] = 2

        # To reach step i:
        # from step (i-1) take 1 step
        # from step (i-2) take 2 steps
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
