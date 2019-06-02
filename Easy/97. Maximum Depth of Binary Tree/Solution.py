"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        if not root:
            return 0
        return self.helper(root)


    def helper(self, root):
        # base case
        if not root:
            return -1

        if not root.left and not root.right:
            return 1

        return max(self.helper(root.left), self.helper(root.right)) + 1











"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        return self.findMaxDepth(root)


    def findMaxDepth(self, root):
        if not root:
            return 0

        # 无脑丢给左右子树
        left  = self.findMaxDepth(root.left)
        right = self.findMaxDepth(root.right)

        return max(left, right) + 1





"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def __init__(self):
        self.depth = 0


    def maxDepth(self, root):
        # write your code here
        self.traverse(root, 1)
        return self.depth

    def traverse(self, root, currDepth):
        if not root:
            return

        if currDepth > self.depth:
            self.depth = currDepth

        self.traverse(root.left, currDepth + 1)
        self.traverse(root.right, currDepth + 1)





"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def __init__(self):
        self.depth = 0


    def maxDepth(self, root):
        # write your code here
        self.traverse(root, 1)
        return self.depth

    def traverse(self, root, currDepth):
        if not root:
            return

        if currDepth > self.depth:
            self.depth = currDepth

        self.traverse(root.left, currDepth + 1)
        self.traverse(root.right, currDepth + 1)
