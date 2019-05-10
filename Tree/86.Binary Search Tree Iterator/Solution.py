"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        self.current_node = root

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        # write your code here
        return self.current_node is not None or len(self.stack) > 0

    """
    @return: return next node
    """
    def next(self):
        # write your code here
        while self.current_node is not None:
            self.stack.append(self.current_node)
            self.current_node = self.current_node.left

        self.current_node = self.stack.pop()
        next_node = self.current_node
        self.current_node = self.current_node.right # current_node could be None
        return next_node
