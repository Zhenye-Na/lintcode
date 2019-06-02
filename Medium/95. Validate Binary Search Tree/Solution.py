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
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        if root is None:
            return True

        MAX = sys.maxsize
        MIN = -sys.maxsize-1

        return self.dfs(root, MIN, MAX)

    def dfs(self, root, Min, Max):

        if root is None:
            return True
        if root.val >= Max or root.val <= Min :
            return False

        return self.dfs(root.left, Min, root.val) and self.dfs(root.right, root.val, Max)
