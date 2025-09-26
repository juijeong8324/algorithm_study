# Input
# string s
# Output
# longest palindromic substring in s
# Hint
# 1. Reuse a previously computed palindrome
# 2. "aba" == palindrome -> "xabax" == palindrome
# 3. Brute-force
#    - O(n^2) = make every start - end pairs substring
#    - O(n) = palindromic checks
# Reduce the time for palindromic checks to O(1) by Reusing previous computation
# Two Pointers

class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ""
        temp = ""
        for start in range(0, len(s)):
            temp = ""
            end = start
            while start >= 0 and end <= len(s)-1:
                if start == end:
                    temp = s[start]
                elif start != end and s[start] == s[end]:
                    temp = s[start] + temp + s[end]

                start -= 1
                end += 1

            if len(answer) < len(temp):
                answer = temp

        return answer

# But...
# Wrong at the case even length like, s = "cbbd" / answer = "bb"
