"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        ret = []
        self.search(root, k1, k2, ret)
        return ret

    def search(self, root, k1, k2, ret):
        if root is None:
            return

        if root.val > k2:
            self.search(root.left, k1, k2, ret)
        elif root.val < k1:
            self.search(root.right, k1, k2, ret)
        else:
            self.search(root.left, k1, k2, ret)
            ret.append(root.val)
            self.search(root.right, k1, k2, ret)
