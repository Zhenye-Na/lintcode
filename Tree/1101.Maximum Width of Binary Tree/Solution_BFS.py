from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        queue = deque([(root, 0)])
        result = 0

        while queue:
            left = queue[0][1]
            right = left
            size = len(queue)
            for i in range(size):
                node, right = queue.popleft()
                if node.left:
                    queue.append((node.left, right * 2))
                if node.right:
                    queue.append((node.right, right * 2 + 1))
            result = max(result, right - left + 1)

        return result
