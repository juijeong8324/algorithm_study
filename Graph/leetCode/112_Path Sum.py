# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Input
# root = binary tree
# targetSum = an integer
# Output
# if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum
# Hint
# DFS
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, currSum):
            if not root:  # None
                return False
            if not root.left and not root.right:  # leaf Node
                return (currSum + root.val == targetSum)

            left = dfs(root.left, currSum+root.val)
            right = dfs(root.right, currSum+root.val)
            return left or right

        return dfs(root, 0)
