# Input
# s = containing the char '(', ')', '{', '}', '[' , ']'
# Output
# boolean if the input string is valid

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in mapping:  # closed brackets
                # exist corresponding open brackets
                if stack and mapping[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)

        return not stack  # if stack is empty return True
