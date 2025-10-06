# Input
# s = a string
# Output
# the length of longest substring without duplicate characters
# Hint
# Generate all possible substrings & check for each substring if it's valid
class Solution:
    # Two pointers
    # O(N^2)
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        for start in range(len(s)):
            check = {}
            temp = 0
            for end in range(start, len(s)):
                if not s[end] in check:
                    temp = temp + 1
                    check[s[end]] = 1
                else:
                    break
            if maxLen < temp:
                maxLen = temp
        return maxLen

    # Sliding Window(Two pointers), Set
    # Invariant: set == unique chars in s[left:right+1]
    # O(N)
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        sub = set()
        left = 0
        for right in range(len(s)):
            while s[right] in sub:  # Sliding from left
                sub.remove(s[left])
                left += 1
            sub.add(s[right])
            maxLen = max(maxLen, right - left + 1)

        return maxLen
