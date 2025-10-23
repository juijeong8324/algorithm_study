# Input
# s = string
# Output
# Boolean if it is a palindrome
# palindrome
# 1. Converting all uppercase letters into lowcase letters
# 2. Removing all non-alphanumeric characters
# 3. Reads the same forward and backward

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(re.findall(r"[0-9a-z]", s))

        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1

        return True

    # Use str.isalnum(): Return if str consists digit or alphabet
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i <= j:
            try:
                while not s[i].isalnum():
                    i += 1
                while not s[j].isalnum():
                    j -= 1
            except:  # catch Index Error
                return True

            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True
