"""
Definition of Doubly-ListNode
class DoublyListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = nextDefinition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of tree
    @return: the head of doubly list node
    """
    def bstToDoublyList(self, root):
        # write your code here
        if not root:
            return None
        traversal = self._inorderTraversal(root)

        parent_node = DoublyListNode(traversal[0])
        first = parent_node

        for i in range(1, len(traversal)):
            current_node = DoublyListNode(traversal[i])
            parent_node.next = current_node
            current_node.prev = parent_node
            parent_node = parent_node.next

        return first

    def _inorderTraversal(self, root):
        if not root:
            return []

        left = self._inorderTraversal(root.left)
        right = self._inorderTraversal(root.right)

        return left + [root.val] + right


