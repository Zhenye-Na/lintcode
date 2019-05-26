"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param {TreeNode} root: The root of binary tree
    @return {TreeNode} root of new tree
    """
    def cloneTree(self, root):
        # Write your code here
        if root is None:
            return None
        clone_root = TreeNode(root.val)
        clone_root.left = self.cloneTree(root.left)
        clone_root.right = self.cloneTree(root.right)
        return clone_root