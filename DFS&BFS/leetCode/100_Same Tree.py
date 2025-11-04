# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Input
# p, q = the roots of two binary trees
# Output
# boolean if they are the same or not
# same if they are structurally identical, and the nodes have the same values
from collections import deque


class Solution:
    # BFS
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append((p, q))

        while queue:
            currP, currQ = queue.popleft()
            if not currP and not currQ:
                continue
            elif (currP and not currQ) or (not currP and currQ):
                return False

            if currP.val != currQ.val:
                return False

            queue.append((currP.left, currQ.left))
            queue.append((currP.right, currQ.right))

        return True

    # BFS2
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = deque()
        queue.append((p, q))

        while queue:
            currP, currQ = queue.popleft()
            if currP is currQ:  # both None
                continue
            # mismatch in structure (one is None) or in val
            if not currP or not currQ or currP.val != currQ.val:
                return False

            # append children to compare next
            queue.append((currP.left, currQ.left))
            queue.append((currP.right, currQ.right))

        return True

    # DFS
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is q:
            return True

        if not p or not q or p.val != q.val:
            return False

        # short-circuit!!!! if left is False, then not call right
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
