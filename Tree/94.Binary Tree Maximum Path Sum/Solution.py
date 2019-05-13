import sys

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
    @return: An integer
    """
    def maxPathSum(self, root):
        # write your code here
        self.maxSum = -sys.maxsize
        self._find_max_path_sum(root)
        return self.maxSum

    def _find_max_path_sum(self, root):
        if root is None:
            return 0 

        leftSum = self._find_max_path_sum(root.left)
        rightSum = self._find_max_path_sum(root.right)

        self.maxSum = max(self.maxSum, root.val + leftSum + rightSum, leftSum + root.val, rightSum + root.val, root.val)
        return max(root.val + leftSum, root.val + rightSum)
