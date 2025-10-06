# Input
# height = an integer array (length = n), vertical lines
# Output
# Find two lines, such that the container contains the most water
# Return the maximum amount of water a container can store
# Hint
# Greedy, Two Pointers
class Solution:
    # O(N^2)
    # Time Limit Exceeded
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        for i in range(n):
            for j in range(i, n):
                h = min(height[i], height[j])
                w = j - i
                ans = max(ans, h*w)

        return ans

    # Two Pointers
    # O(N)
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0
        while left < right:
            temp = min(height[left], height[right])*(right-left)  # h * w
            # move pointer that points lower (greedy)
            if height[left] > height[right]:
                right = right - 1
            else:
                left = left + 1
            ans = max(ans, temp)

        return ans
