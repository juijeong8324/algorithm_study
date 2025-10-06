# Two Pointers
# Calculate odd length and even lenth separately

class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""

        def expand(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left+1:right]

        for i in range(len(s)):
            # odd
            palidrome_odd = expand(i, i)
            if len(palidrome_odd) > len(answer):
                answer = palidrome_odd
            # even
            palidrome_even = expand(i, i+1)
            if len(palidrome_even) > len(answer):
                answer = palidrome_even

        return answer
