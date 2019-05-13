"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        # write your code here
        self.length = 1
        self._dfs(root)
        return self.length

    def _dfs(self, root):
        if root is None:
            return 0

        length_left = self._dfs(root.left)
        length_right = self._dfs(root.right)

        current = 1
        if root.left is not None and root.val + 1 == root.left.val:
            current = max(current, length_left + 1)

        if root.right is not None and root.val + 1 == root.right.val:
            current = max(current, length_right + 1)

        self.length = max(self.length, current)

        return current
