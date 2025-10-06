# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Input
# a binary tree
# Output
# determine if it is height-balanced
# Hint
# DFS
# if the tree is height balanced, its height of subtree is also height balanced
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:  # Buttom up
                return 0

            h_l = dfs(node.left)
            if h_l == -1:
                return -1  # check subtree balance
            h_r = dfs(node.right)
            if h_r == -1:
                return -1  # check subtree balance

            if abs(h_l - h_r) > 1:
                return -1  # check current tree balance
            return max(h_l, h_r) + 1

        return dfs(root) != -1
