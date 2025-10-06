# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Input
# a binary Tree
# Output
# its minimum depth
# the number of nodes along the shortest path from the root node down to the nearest leaf node
# BFS
from collections import deque


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        level = 1

        if not root:
            return 0
        while q:
            n = len(q)
            for i in range(n):  # Same Level
                curr = q.popleft()

                if not curr.left and not curr.right:  # if node is leafNode?
                    return level
                # Not
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            level += 1
        return level
