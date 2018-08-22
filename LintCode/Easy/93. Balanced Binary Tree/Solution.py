"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class ResultType:
    def __init__(self, depth, isBalanced):
        self.depth = depth
        self.isBalanced = isBalanced


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        # write your code here
        if not root:
            return True
        return self.helper(root).isBalanced


    def helper(self, root):
        if not root:
            return ResultType(0, True)

        # Divide -> find left subtree depth and right subtree depth
        left  = self.helper(root.left)
        right = self.helper(root.right)

        # return False if subtree is not balanced
        if not left.isBalanced or not right.isBalanced:
            return ResultType(0, False)

        # return false if current subtree depth difference is greater than 1
        if abs(left.depth - right.depth) > 1:
            return ResultType(0, False)

        return ResultType(max(left.depth, right.depth) + 1, True)
