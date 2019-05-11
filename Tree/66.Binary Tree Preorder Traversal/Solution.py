"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# Non-Recursion (Stack)

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        stack  = []
        result = []

        if root is None:
            return result

        stack.append(root)

        # while stack is not Empty:
        while stack:
            node = stack.pop()
            result.append(node.val)

            # stack.push(node.right)
            if node.right is not None:
                stack.append(node.right)

            # stack.push(node.left)
            if node.left is not None:
                stack.append(node.left)

        return result



"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# Traverse

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        result = []
        self.helper(root, result)
        return result


    def helper(self, root, result):
        if root is None:
            return

        result.append(root.val)
        self.helper(root.left, result)
        self.helper(root.right, result)



"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

# Divide & Conquer

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        result = []
        if root is None:
            return result

        left  = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)

        result.append(root.val)
        result.extend(left)
        result.extend(right)

        return result
