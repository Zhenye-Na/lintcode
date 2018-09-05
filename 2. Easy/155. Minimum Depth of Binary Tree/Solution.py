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
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        if not root:
            return 0
        return self.helper(root)


    def helper(self, root):
        # base case
        if not root:
            return sys.maxint

        # recursive case
        else:
            # leaf node
            if not root.left and not root.right:
                return 1

            # recursively compare minDepth of left and right subtree
            return min(self.helper(root.left), self.helper(root.right)) + 1
