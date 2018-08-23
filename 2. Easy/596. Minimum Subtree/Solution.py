"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def __init__(self):
        self.summation = sys.maxint
        self.node = None

    def findSubtree(self, root):
        # write your code here
        self.helper(root)
        return self.node

    def helper(self, root):
        if not root:
            return 0

        # Divide & Conquer
        left  = self.helper(root.left)
        right = self.helper(root.right)

        # if current subtree sum is less than flobal minimum, update it
        if left + right + root.val < self.summation:
            self.node = root
            self.summation = left + right + root.val

        # else return bustree sum
        return left + right + root.val
