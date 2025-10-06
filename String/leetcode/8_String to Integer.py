# Input
# string s
# Output
# converts a string to a 32-bit signed integer

class Solution:
    def myAtoi(self, s: str) -> int:
        new_s = ""
        for d in s:
            if not new_s and d == " ":
                continue
            elif d == '-' or d == '+':
                if not new_s:
                    new_s += d
                else:
                    break
            elif d.isdigit():
                new_s += d
            else:  # letters
                break

        if not new_s or new_s in ('+', '-'):
            return 0

        num = int(new_s)
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if num < INT_MIN:
            return INT_MIN
        elif num > INT_MAX:
            return INT_MAX
        else:
            return num

    def myAtoi(self, s: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        i = 0  # index
        n = len(s)

        while i < n and s[i] == " ":  # Skip space
            i += 1

        sign = 1
        if i < n and (s[i] == "-" or s[i] == "+"):  # Check sign (only once)
            sign = -1 if s[i] == "-" else 1
            i += 1

        res = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            res = res*10 + digit
            i += 1

        if res > INT_MAX and sign == 1:
            return INT_MAX
        elif res > INT_MAX + 1 and sign == -1:
            return INT_MIN

        return sign*res
