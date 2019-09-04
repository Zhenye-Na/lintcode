"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: a binary tree
    @param target: the sum
    @return: the scheme
    """

    def pathSum(self, root, target):
        # Write your code here.
        self.results = []
        self.dfs(root, target, [])
        return self.results

    def dfs(self, root, target, curr):
        if root is None:
            return

        if target == root.val and root.left is None and root.right is None:
            self.results.append(curr[:] + [root.val])

        self.dfs(root.left, target - root.val, curr + [root.val])
        self.dfs(root.right, target - root.val, curr + [root.val])
