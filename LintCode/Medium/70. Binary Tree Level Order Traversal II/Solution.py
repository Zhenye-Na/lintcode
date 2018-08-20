"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        # write your code here
        queue  = []
        result = []

        if root is None:
            return result

        queue.append(root)
        while queue:
            level = []
            size = len(queue)

            for i in range(size):
                # pop queue
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.insert(0, level)

        return result



class Solution:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        # write your code here
        queue  = []
        stack = []

        if root is None:
            return stack

        queue.append(root)
        while queue:
            level = []
            size = len(queue)

            for i in range(size):
                # pop queue
                node = queue.pop(0)
                level.insert(0, node.val)

                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

            stack.append(level)

        return stack[::-1]
