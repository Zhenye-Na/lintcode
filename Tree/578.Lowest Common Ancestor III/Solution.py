"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""

class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        self.a = False
        self.b = False
        node = self._dfs(root, A, B)
        if self.a and self.b:
            return node
        return None

    def _dfs(self, root, A, B):
        if root is None:
            return None

        left = self._dfs(root.left, A, B)
        right = self._dfs(root.right, A, B)

        if root == A or root == B:
            if root == A:
                self.a = True
            else:
                self.b = True
            return root

        # A 和 B 一边一个
        if left and right:
            return root
        
        # 左子树有一个点或者左子树有LCA
        if left:
            return left
        
        # 右子树有一个点或者右子树有LCA
        if right:
            return right
        
        # 左右子树啥都没有
        return None