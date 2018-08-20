"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        queue  = []
        result = []
        flag = 1

        if not root:
            return result

        queue.append(root)
        while queue:
            level = []
            size  = len(queue)

            for i in range(size):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if flag != 1:
                level.reverse()

            flag = -flag
            result.append(level)

        return result
