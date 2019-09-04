"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: root of the tree
    @param p: the node p
    @param q: the node q
    @return: find the LCA of p and q
    """

    def lowestCommonAncestor(self, root, p, q):
        # write your code here
        ancestor = self.dfs(root, p, q)
        return ancestor

    def dfs(self, root, p, q):
        if root is None:
            return None

        if root == p or root == q:
            return root

        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)

        if left and right:
            return root

        if left:
            return left

        if right:
            return right

        return None
