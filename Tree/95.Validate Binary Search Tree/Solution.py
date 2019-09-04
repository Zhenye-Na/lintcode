import sys


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        # write your code here
        if root is None:
            return True

        leftMax = sys.maxsize
        rightMin = -sys.maxsize - 1
        return self.dfs(root, rightMin, leftMax)

    def dfs(self, root, Min, Max):
        if root is None:
            return True

        if root.val >= Max or root.val <= Min:
            return False

        return self.dfs(root.left, Min, root.val) and self.dfs(root.right, root.val, Max)


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
        isBST, _, _ = self._validate(root)
        return isBST

    def _validate(self, root):
        if not root:
            return True, None, None

        leftIsBST, leftMin, leftMax = self._validate(root.left)
        rightIsBST, rightMin, rightMax = self._validate(root.right)

        # 左右子树不是 BST 直接返回不是
        if not leftIsBST or not rightIsBST:
            return False, None, None

        # left max 要大于根节点
        if leftMax is not None and leftMax >= root.val:
            return False, None, None

        # right min 要小于根节点
        if rightMin is not None and rightMin <= root.val:
            return False, None, None

        # is BST
        minNode = leftMin if leftMin is not None else root.val
        maxNode = rightMax if rightMax is not None else root.val

        return True, minNode, maxNode
