# Input
# a, b = two binary strings
# Output
# their sum as binary string
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer = bin(int(a, 2) + int(b, 2))
        return answer[2:]  # remove 0b prefix

    # Binary manipulation
    # Idea = divide carry and sum, repeat until carry doesn’t exist
    def addBinary(self, a: str, b: str) -> str:
        x = int(a, 2)
        y = int(b, 2)

        while y:
            carry = (x & y) << 1  # XOR -> shit left one
            x = (x ^ y)
            y = carry

        return bin(x)[2:]
