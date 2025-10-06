# Input
# needle = strings
# haystack = strings
# Output
# the index of the first occurrence of needle in haystack
# -1 if needle is not part of haystack
# Hint
# Two Pointer
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0  # start
        j = 0  # length
        n = len(haystack)
        m = len(needle)
        if n < m:
            return -1

        while i < n - m + 1 and j < m:
            if needle[j] == haystack[i+j]:  # check two strings
                j = j + 1
            else:  # find start index
                i = i + 1
                j = 0

        return i if j == m else -1

    # Using Slicing!!!!!!!!!! More Easier
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        for i in range(n-m+1):  # start index
            if haystack[i:i+m] == needle:
                return i
            return -1
