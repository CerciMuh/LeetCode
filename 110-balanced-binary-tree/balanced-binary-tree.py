# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True  
        
        #from max depth question
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))
        
        leftHeight = height(root.left)
        rightHeight = height(root.right)
        
        if abs(leftHeight - rightHeight) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)

