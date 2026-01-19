# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #we need to get to the absolute bottom of a root then once we stop getting bottoms we flip
        #im guessing a recursive approach would work best for this? like a dfs 
        if not root:
            return None
        queue = []
        queue.append(root)
        
        while queue:
            node = queue.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root