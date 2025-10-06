# Input
# s = string
# numRows = given a numbers of rows
# Output
# make conversion given a numbers of rows
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        val = ["" for _ in range(numRows)]
        i = 0
        change = 1
        for ch in s:
            if change == 1 and i == numRows-1:
                change = -1
            elif change == -1 and i == 0:
                change = 1

            val[i] += ch
            i = i + change
        return "".join(val)
