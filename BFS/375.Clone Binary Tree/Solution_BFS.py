"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree
    @return: root of new tree
    """
    def cloneTree(self, root):
        # write your code here
        if not root:
            return root

        # copy nodes
        nodes = self._getNodes(root)
        mapping = {}
        for node in nodes:
            mapping[node] = TreeNode(node.val)


        # copy edges
        for node in nodes:
            if node.left:
                mapping[node].left = mapping[node.left]
            if node.right:
                mapping[node].right = mapping[node.right]

        return mapping[root]


    def _getNodes(self, root):
        from collections import deque

        queue = deque([root])
        nodes = []
        while queue:
            node = queue.popleft()
            nodes.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return nodes
