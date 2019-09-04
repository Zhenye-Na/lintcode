"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: a root of tree
    @return: return a integer
    """

    def findBottomLeftValue(self, root):
        # write your code here
        self.max_level = 0
        self.val = 0
        self.helper(root, 1)
        return self.val

    def helper(self, root, level):
        if not root:
            return

        if level > self.max_level:
            self.max_level = level
            self.val = root.val

        self.helper(root.left, level + 1)
        self.helper(root.right, level + 1)
