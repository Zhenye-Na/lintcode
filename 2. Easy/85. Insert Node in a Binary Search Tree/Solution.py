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
        if not root:
            return node
        self.helper(root, node)
        return root


    def helper(self, root, node):
        if node.val >= root.val:
            if root.right:
                self.helper(root.right, node)
            else:
                root.right = node
                return
        else:
            if root.left:
                self.helper(root.left, node)
            else:
                root.left = node
                return


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
        if not root:
            return node

        dummy = root
        while dummy:
            if node.val >= dummy.val:
                if dummy.right:
                    dummy = dummy.right
                else:
                    dummy.right = node
                    break
            else:
                if dummy.left:
                    dummy = dummy.left
                else:
                    dummy.left = node
                    break

        return root
