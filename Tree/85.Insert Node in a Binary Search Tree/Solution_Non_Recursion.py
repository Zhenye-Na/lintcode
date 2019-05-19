"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if root is None:
            return node

        parent, current = None, root
        while current is not None:
            parent = current
            if current.val <= node.val:
                current = current.right
            else:
                current = current.left

        if parent.val <= node.val:
            parent.right = node
        else:
            parent.left = node

        return root