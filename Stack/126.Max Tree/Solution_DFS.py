"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param A: Given an integer array with no duplicates.
    @return: The root of max tree.
    """
    def maxTree(self, A):
        # write your code here
        if not A or len(A) == 0:
            return None

        return self._findMaxTree(0, len(A) - 1, A)

    def _findMaxTree(self, start, end, A):
        if start > end:
            return None

        if start == end:
            return TreeNode(A[start])

        maxVal = max(A[start:end + 1])
        maxValIdx = A[start:end + 1].index(maxVal) + start

        root = TreeNode(maxVal)
        root.left = self._findMaxTree(start, maxValIdx - 1, A)
        root.right = self._findMaxTree(maxValIdx + 1, end, A)

        return root