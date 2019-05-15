"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""

class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum3(self, root, target):
        # write your code here
        results = []
        self._dfs(root, target, results)
        return results

    def _dfs(self, root, target, results):
        if root is None:
            return

        path = []
        self._findSum(root, None, target, path, results)

        self._dfs(root.left, target, results)
        self._dfs(root.right, target, results)

    def _findSum(self, root, father, target, path, results):
        path.append(root.val)
        target -= root.val

        if target == 0:
            results.append(path[:])

        if root.parent not in [None, father]:
            self._findSum(root.parent, root, target, path, results)

        if root.left not in [None, father]:
            self._findSum(root.left, root, target, path, results)

        if root.right not in [None, father]:
            self._findSum(root.right, root, target, path, results)

        path.pop()
