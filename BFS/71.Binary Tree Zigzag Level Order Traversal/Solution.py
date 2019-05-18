from collections import deque

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        traversal = []
        if root is None:
            return traversal

        queue = deque([])
        queue.append(root)

        while queue:
            level = []
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if len(traversal) % 2 == 0:
                traversal.append(level)
            else:
                traversal.append(level[::-1])

        return traversal 
