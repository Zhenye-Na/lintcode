"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        result = []
        self.inorderHelper(root, result)
        return result


    def inorderHelper(self, root, result):
        if root is None:
            return result

        if root.left is not None:
            self.inorderHelper(root.left, result)

        result.append(root.val)

        if root.right is not None:
            self.inorderHelper(root.right, result)
