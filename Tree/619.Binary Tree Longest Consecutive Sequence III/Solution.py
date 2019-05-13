"""
Definition for a multi tree node.
class MultiTreeNode(object):
    def __init__(self, x):
        self.val = x
        children = [] # children is a list of MultiTreeNode
"""


class Solution:
    # @param {MultiTreeNode} root the root of k-ary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive3(self, root):
        # Write your code here
        self.maxLength = 0
        self._find_path(root)
        return self.maxLength

    def _find_path(self, root):

        if root is None:
            return 0

        up, down = 0, 0
        for child in root.children:
            child_up, child_down = self._find_path(child)
            if child.val - 1 == root.val:
                up = max(up, child_up + 1)
            elif child.val + 1 == root.val:
                down = max(down, child_down + 1)
            self.maxLength = max(self.maxLength, up + down + 1)

        return up, down
