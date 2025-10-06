# Input
# s = a string consisting of words and spaces
# Output
# the length of the last word in the string
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])
