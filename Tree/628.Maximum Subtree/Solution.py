"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the maximum weight node
    """
    maximum = - sys.maxsize - 1
    node = None

    def findSubtree(self, root):
        # write your code here
        self._dfs(root)
        return self.node

    def _dfs(self, root):
        if not root:
            return 0

        leftTotal = self._dfs(root.left)
        rightTotal = self._dfs(root.right)

        if leftTotal + rightTotal + root.val > self.maximum:
            self.maximum = leftTotal + rightTotal + root.val
            self.node = root

        return leftTotal + rightTotal + root.val
