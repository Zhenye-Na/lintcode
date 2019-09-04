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
    @return: new root
    """

    def upsideDownBinaryTree(self, root):
        # write your code here
        if root is None:
            return None
        return self.dfs(root)

    def dfs(self, root):
        if root.left is None:
            return root

        newRoot = self.dfs(root.left)
        root.left.right = root
        root.left.left = root.right
        root.left, root.right = None, None

        return newRoot
