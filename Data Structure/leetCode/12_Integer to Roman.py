# Input
# num =  1 <= num <= 3999
# Output
# Convert it to a Roman numeral
# Roman numeral are formed by appending the conversions of decimal place values from highes to lowest
# Rules:
# 1. the value does not start with 4 or 9 -> The symbol of the maximal value that can be subtracted from the input
# 2. the value starts with 4 or 9 -> The subtractive form representing one symbol subtracted from the following symbol
# 3. Only powers of 10 can consecutively at most 3 times
# 4. If you need to append a symbol 4 times use the subtractive form.
# Hint
# dict, String, Math
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1: "I", 5: "V", 10: "X", 50: "L",
                 100: "C", 500: "D", 1000: "M"}
        s = str(num)
        n = len(s) - 1
        answer = ""

        for ch in s:
            digit = int(ch)
            if digit == 4:
                answer += roman[10**n]+roman[(digit+1)*(10**n)]
            elif digit == 9:
                answer += roman[10**n]+roman[10**(n+1)]
            else:
                if digit <= 3:
                    answer += roman[10**n]*digit
                else:
                    answer += roman[5*(10**n)]+roman[10**n]*(digit-5)
            n -= 1

        return answer
