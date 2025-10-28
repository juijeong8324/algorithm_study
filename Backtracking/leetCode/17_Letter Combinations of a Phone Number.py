# Input
# a string containing digits from 2-9
# Output
# all posible letter combinations that the number could represent
# Hint
# Backtracking
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        answer = []
        mapping = {"2": ["a", "b", "c"],
                   "3": ["d", "e", "f"],
                   "4": ["g", "h", "i"],
                   "5": ["j", "k", "l"],
                   "6": ["m", "n", "o"],
                   "7": ["p", "q", "r", "s"],
                   "8": ["t", "u", "v"],
                   "9": ["w", "x", "y", "z"]
                   }

        def backtrack(order):
            if len(order) == len(digits):
                answer.append(order)
                return

            n = len(order)
            for digit in mapping[digits[n]]:
                backtrack(order+digit)

        backtrack("")
        return answer
