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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        height, balanced = self._isBalanced(root)
        return balanced

    def _isBalanced(self, root):
        if not root:
            return 0, True

        left_height, left_is_balanced = self._isBalanced(root.left)
        right_height, right_is_balanced = self._isBalanced(root.right)

        if not left_is_balanced or not right_is_balanced:
            return 0, False

        if abs(left_height - right_height) > 1:
            return 0, False

        return max(left_height, right_height) + 1, True
