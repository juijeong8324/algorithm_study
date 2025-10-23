# Input
# rowwIndex = an integer
# Output
# the rowIndexth (0-indexed) row of the Pascal's triangle
# Pascal's triangle = each number is the sum of the two numbers directly above it

class Solution:
    # DP
    def getRow(self, rowIndex: int) -> List[int]:
        answer = [1]
        for i in range(1, rowIndex+1):
            answer.append([1])  # make first element at ith row
            for j in range(1, i):
                answer[i].append(answer[i-1][j-1] + answer[i-1][j])
            answer[i].append(1)  # last element at ith row

        return answer[rowIndex]

    # Solve DP using 1D Array
    def getRow(self, rowIndex: int) -> List[int]:
        answer = [1] * (rowIndex+1)
        for i in range(2, rowIndex+1):  # Iterate rows from 2nd to rowIndex
            # Update current row values in reverse order to avoid overwritting
            for j in range(i-1, 0, -1):
                answer[j] += answer[j-1]

        return answer
