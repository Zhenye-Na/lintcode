"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the tree
    @return: the total sum of all root-to-leaf numbers
    """
    def sumNumbers(self, root):
        # write your code here
        return self._dfs(root, 0)

    def _dfs(self, root, total):
        if root is None:
            return 0

        total = total * 10 + root.val
        if root.left is None and root.right is None:
            return total

        return self._dfs(root.left, total) + self._dfs(root.right, total)
