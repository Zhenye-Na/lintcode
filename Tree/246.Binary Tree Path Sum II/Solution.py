"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum2(self, root, target):
        # write your code here
        if root is None: 
            return []

        left   = self.binaryTreePathSum2(root.left, target)
        right  = self.binaryTreePathSum2(root.right, target)
        middle = self.fromRootToAny(root, target)
        return left + right + middle

    def fromRootToAny(self, root, target):
        results = []
        path = []
        self._dfs(root, target, results, path)
        return results
    
    def _dfs(self, root, target, results, path):
        if root is None:
            return 

        path.append(root.val)
        if root.val == target:
            results.append(path[:])

        self._dfs(root.left, target - root.val, results, path)
        self._dfs(root.right, target - root.val, results, path)

        path.pop()