# Input
# digits = a large integer, each digits[i] == ith digit of the integer
# Output
# the resulting array of digits which increment the large integer
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        num += 1
        return [int(d) for d in str(num)]
