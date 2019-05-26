"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import defaultdict

class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    def findLeaves(self, root):
        # write your code here
        result = []
        if root is None:
            return result

        mapping = defaultdict(list)
        maxDepth = self._dfs(root, mapping)
        for i in range(1, maxDepth + 1):
            result.append(mapping.get(i))
        return result


    def _dfs(self, root, mapping):
        if root is None:
            return 0

        leftHeight = self._dfs(root.left, mapping)
        rightHeight = self._dfs(root.right, mapping)

        currentHeight = max(leftHeight, rightHeight) + 1
        mapping[currentHeight].append(root.val)

        return currentHeight