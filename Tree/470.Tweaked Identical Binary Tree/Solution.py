"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param a: the root of binary tree a.
    @param b: the root of binary tree b.
    @return: true if they are tweaked identical, or false.
    """

    def isTweakedIdentical(self, a, b):
        # write your code here
        if a is None and b is None:
            return True

        if a is None or b is None:
            return False

        return self.checkIdentical(a, b)

    def checkIdentical(self, a, b):
        if a is None and b is None:
            return True

        if a is None or b is None:
            return False

        if a.val != b.val:
            return False

        return (self.checkIdentical(a.left, b.left) and self.checkIdentical(a.right, b.right)) or (self.checkIdentical(a.left, b.right) and self.checkIdentical(a.right, b.left))
