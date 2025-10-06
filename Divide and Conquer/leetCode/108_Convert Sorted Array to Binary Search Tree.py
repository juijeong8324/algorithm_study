# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Input
# nums = an integer array
# the elements are sorted in ascending order
# Output
# convert it to a height-balanced binary search tree
# Hint
# Divide and Conquer, Two pointers
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def bst(node, left, right):
            if left >= right:
                return
            mid = (left+right) // 2
            node.val = nums[mid]
            # Divide
            node.left = bst(TreeNode(), left, mid)
            node.right = bst(TreeNode(), mid+1, right)
            return node

        root = bst(TreeNode(), 0, len(nums))
        return root
