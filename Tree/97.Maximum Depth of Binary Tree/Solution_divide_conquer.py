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
        return self._find_depth(root)

    def _find_depth(self, root):
        if not root:
            return 0

        return max(self._find_depth(root.left), self._find_depth(root.right)) + 1
