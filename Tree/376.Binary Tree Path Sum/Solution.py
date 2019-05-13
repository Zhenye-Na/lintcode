"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        # write your code here
        self.paths = []
        self._dfs(root, target, [])
        return self.paths

    def _dfs(self, root, target, path):
        if root is None:
            return

        if target == root.val and root.left is None and root.right is None:
            path.append(root.val)
            self.paths.append(path[:])
            return

        self._dfs(root.left, target - root.val, path + [root.val])
        self._dfs(root.right, target - root.val, path + [root.val])
