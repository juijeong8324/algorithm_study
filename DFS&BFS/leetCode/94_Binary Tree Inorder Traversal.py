# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Input
# root = the root of a binary tree
# Output
# the inorder traversal of its nodes' values
# Hint
# Inorder = Left - > Root -> Right
class Solution:
    # Recursive
    # Idea
    # visit left subtree → append current node → right subtree
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []

        def visit(curr: Optional[TreeNode]) -> int:
            if not curr:
                return
            visit(curr.left)
            answer.append(curr.val)
            visit(curr.right)

        visit(root)

        return answer

    # Using Stack and DFS
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer, stack = [], []
        curr = root
        while curr or stack:
            # Serach Left tree until end
            while curr:
                stack.append(curr)
                curr = curr.left

            # append root
            curr = stack.pop()
            answer.append(curr.val)

            # Search right tree
            curr = curr.right

        return answer
