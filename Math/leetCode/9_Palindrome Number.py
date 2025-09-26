# Input
# x = integer 
# Output 
# Return true if x is palindrome
# Mission
# Solve it without converting the integer to a string.
# Idea
# Compare with reversal

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0): # negative or multiple of 10  
            return False
        
        revert_x = 0
        while x > revert_x: # half reversal 
            revert_x = revert_x*10 + (x%10)
            x = x // 10
        
        # if len(x) == even
        # 1221, x = 12 y = 12
        # if len(x) == odd, delete middle digit
        # 121, x = 1 y = 12
        return x == revert_x or x == (revert_x // 10)
            