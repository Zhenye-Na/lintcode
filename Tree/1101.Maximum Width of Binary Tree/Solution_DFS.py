"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root
    @return: the maximum width of the given tree
    """

    def widthOfBinaryTree(self, root):
        # Write your code here
        queue = [(root, 0, 0)]
        cur_depth = left = ans = 0

        for node, depth, pos in queue:
            if node:
                queue.append((node.left, depth + 1, pos * 2))
                queue.append((node.right, depth + 1, pos * 2 + 1))

                if cur_depth != depth:
                    cur_depth = depth
                    left = pos

                ans = max(pos - left + 1, ans)

        return ans
