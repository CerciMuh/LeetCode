# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queueOne = deque([p])
        queueTwo = deque([q])

        while queueOne and queueTwo:
            nodeOne = queueOne.popleft()
            nodeTwo = queueTwo.popleft()

            if not nodeOne and not nodeTwo:
                continue
            if not nodeOne or not nodeTwo or nodeOne.val != nodeTwo.val:
                return False

            queueOne.append(nodeOne.left)
            queueOne.append(nodeOne.right)
            queueTwo.append(nodeTwo.left)
            queueTwo.append(nodeTwo.right)

        return len(queueOne) == len(queueTwo)