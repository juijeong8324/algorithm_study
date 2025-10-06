# Input
# x = a signed 32-bit integer x
# Output
# x with its digits reversed
# If reversing x causes the value to go outside [-2^31, 2^31-1], then return 0

class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        l = []
        sign = 1 if x >= 0 else -1
        x = abs(x)
        while x > 0:
            l.append(x % 10)
            x = x // 10

        new_x = 0
        digit = 1
        while l:
            new_x += digit * l.pop()
            digit *= 10
        return sign * new_x if INT_MIN <= new_x <= INT_MAX else 0

    # int -> str
    def reverse(self, x: int) -> int:
        x = str(x)
        sign = ''
        digits = ''
        if x[0] == '-':
            sign = x[0]
            digits = x[1:]
            digits = digits[::-1]
        else:
            digits = x[::-1]
        if int(digits) > (2**31 - 1):
            return 0
        else:
            return int(sign+digits)
