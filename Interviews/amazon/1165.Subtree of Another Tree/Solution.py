"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param s: the s' root
    @param t: the t' root
    @return: whether tree t has exactly the same structure and node values with a subtree of s
    """
    def isSubtree(self, s, t):
        # Write your code here
        if s is None:
            return t is None

        if s.val == t.val and self.checkSubtree(s, t):
            return True

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def checkSubtree(self, s, t):
        if s is None:
            return t is None

        if t is None or s.val != t.val:
            return False

        return self.checkSubtree(s.left, t.left) and self.checkSubtree(s.right, t.right)
