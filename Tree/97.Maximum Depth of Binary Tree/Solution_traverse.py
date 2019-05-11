"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        self.max_depth = 0
        self._find_depth(root, 1)
        return self.max_depth

    def _find_depth(self, root, depth):
        if not root:
            return

        self.max_depth = max(self.max_depth, depth)
        self._find_depth(root.left, depth + 1)
        self._find_depth(root.right, depth + 1)
