"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        # write your code here
        path_a = self._find_path(root, A)
        path_b = self._find_path(root, B)

        ancestor = root
        for (a, b) in zip(reversed(path_a), reversed(path_b)):
            if a.val == b.val:
                ancestor = a
            else:
                break
        return ancestor


    def _find_path(self, root, target):
        node = target
        path = []
        while node is not None:
            path.append(node)
            node = node.parent

        return path