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
        if root is None:
            return None

        self.flatten(root.left)
        self.flatten(root.right)

        if root.left is None:
            return None

        node = root.left
        while node.right is not None:
            node = node.right

        node.right = root.right
        root.right = root.left
        root.left = None





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
        self._flatten(root)

    def _flatten(self, root):
        if root is None:
            return None

        left  = self._flatten(root.left)
        right = self._flatten(root.right)

        if left is not None:
            left.right = root.right
            root.right = root.left
            root.left = None

        if right is not None:
            return right
            
        if left is not None:
            return left

        return root
