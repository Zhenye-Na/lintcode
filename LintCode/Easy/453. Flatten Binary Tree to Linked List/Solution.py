"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        self.flattenHelper(root)


    def flattenHelper(self, root):
        if not root:
            return root

        left  = self.flattenHelper(root.left)
        right = self.flattenHelper(root.right)

        # Re-connect leftmost leaf to root.right
        if left:
            left.right = root.right
            root.right = root.left
            root.left = None

        # Return rightmost leaf for next recursion
        if right:
            return right

        # Return leftmost if there is no right subtree
        if left:
            return left

        # Reached leaf node, return leaf
        return root
