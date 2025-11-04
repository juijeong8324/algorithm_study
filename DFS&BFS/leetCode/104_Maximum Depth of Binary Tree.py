# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Input
# root of a binary tree
# Output
# its maximum depth
# the number of nodes along the logest path from the root node down to the farthest leaf node
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # DFS
        def depth(node, d):
            if node == None:
                return d
            return max(depth(node.left, d+1), depth(node.right, d+1))

        return depth(root, 0)

        # BFS
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()
        depth = 0
        if root:
            q.append(root)
        while q:
            n = len(q)
            for i in range(n):  # Search all nodes at the current depth
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1

        return depth
