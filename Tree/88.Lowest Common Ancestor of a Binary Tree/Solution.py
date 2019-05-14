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
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        node = self._dfs(root, A, B)
        return node

    def _dfs(self, root, A, B):
        if root is None:
            return None

        if root == A or root == B:
            return root

        left = self._dfs(root.left, A, B)
        right = self._dfs(root.right, A, B)


        # A 和 B 一边一个
        if left and right: 
            return root
        
        # 左子树有一个点或者左子树有 LCA
        if left:
            return left
        
        # 右子树有一个点或者右子树有 LCA
        if right:
            return right
        
        # 左右子树啥都没有
        return None