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
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def removeNode(self, root, value):
        # write your code here
        if root is None:
            return root

        # check if node to delete is in left/right subtree
        if value < root.val:
            root.left = self.removeNode(root.left, value)
        elif value > root.val:
            root.right = self.removeNode(root.right, value)
        else:
            # if root is has 2 childs/only one child/leaf node
            if root.left and root.right:
                maxNode = self.findMax(root)
                root.val = maxNode.val
                root.left = self.removeNode(root.left, maxNode.val)
            elif root.left:
                root = root.left
            elif root.right:
                root = root.right
            else:
                root = None

        return root

    # find max node in left subtree of root
    def findMax(self, root):
        node = root.left
        while node.right:
            node = node.right
        return node
