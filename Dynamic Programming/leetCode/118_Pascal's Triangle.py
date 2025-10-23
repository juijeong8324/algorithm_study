# Input
# numRows = an integer
# Output
# first numRows of Pascal's triangle
# Pascal's trinagle
# each number is the sum of the two numbers directly above it
# Hint
# Dynamic Programming
# Reuse Subproblem
class Solution:
    # O(N^2)
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[1]]
        for i in range(1, numRows):
            answer.append([1])  # First one
            for j in range(1, i):
                # middle
                answer[i].append(answer[i-1][j-1] + answer[i-1][j])
            answer[i].append(1)  # Last one
        return answer
