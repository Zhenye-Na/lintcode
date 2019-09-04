from collections import deque
import sys

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree.
    @return: true if it is a mirror of itself, or false.
    """

    def isSymmetric(self, root):
        # write your code here
        if not root:
            return True

        queue = deque([root])
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    level.append(node.left)
                    queue.append(node.left)
                else:
                    level.append(TreeNode(sys.maxsize))

                if node.right:
                    level.append(node.right)
                    queue.append(node.right)
                else:
                    level.append(TreeNode(sys.maxsize))

            for v1, v2 in zip(level, reversed(level)):
                if v1.val != v2.val:
                    return False

        return True
