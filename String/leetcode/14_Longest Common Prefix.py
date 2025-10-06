# Input
# strs
# Output
# the longest common prefix string amongst an array of strings
# Time Complexity : len(strs) = N, max(str[i]) = M -> O(NM)
# Hint
# Slicing!!!!!
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        prefix = strs[0]
        for idx in range(1, n):
            l1 = len(prefix)
            l2 = len(strs[idx])
            l = min(l1, l2)  # min word가 기준

            temp = ""
            for i in range(l):  # compare with prefix and strs[idx]
                if prefix[i] != strs[idx][i]:
                    break
                temp += prefix[i]  # update new common prefix

            prefix = temp

        return prefix

    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = float('inf')
        # Find smallest word (Longest Common Prefix candidate)
        for word in strs:
            if len(word) < smallest:
                smallest_word = word
                smallest = len(word)

        # Compare each char between the prefix and all an array of strings
        for idx in range(smallest):
            ch = smallest_word[idx]
            for word in strs:
                if word[idx] == ch:
                    if word[idx] != ch:
                        return smallest_word[:idx]
        return smallest_word[:idx]
