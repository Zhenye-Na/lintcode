from collections import deque


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root node
    @param k: an integer
    @return: the number of nodes in the k-th layer of the binary tree
    """
    def kthfloorNode(self, root, k):
        # Write your code here
        if not root or k <= 0:
            return 0

        queue = deque([root])
        depth = 0
        num = 0
        while queue:
            depth += 1
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if depth == k:
                    num += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if depth > k:
                break

        return num
