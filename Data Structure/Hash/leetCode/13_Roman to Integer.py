# Input
# Roman numeral
# Output
# Convert it to an integer
# Hint
# Solve by working the string from back to front and using a map

class Solution:
    def romanToInt(self, s: str) -> int:
        symbol = {"I": 1, "V": 5, "X": 10,
                  "L": 50, "C": 100, "D": 500, "M": 1000}

        answer = 0
        for idx in range(len(s)-1):
            if symbol[s[idx]] >= symbol[s[idx+1]]:
                answer += symbol[s[idx]]
            else:
                answer -= symbol[s[idx]]
        answer = answer + symbol[s[-1]]
        return answer
