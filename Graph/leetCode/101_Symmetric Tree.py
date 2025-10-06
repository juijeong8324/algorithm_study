# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Input
# root = the root of a binary tree
# Output
# wheter it is mirror of itself
from collections import deque


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        #  BFS
        queue = deque()
        queue.append((root.left, root.right))

        while queue:
            a, b = queue.popleft()
            if a is b:  # both None
                continue
            if not a or not b or a.val != b.val:
                return False

            queue.append((a.left, b.right))
            queue.append((a.right, b.left))

        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(left, right):
            if left is right:  # Both None
                return True

            if not left or not right or left.val != right.val:
                return False

            return check(left.left, right.right) and check(left.right, right.left)

        return check(root.left, root.right)
