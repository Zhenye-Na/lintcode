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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        result = []
        stack  = []

        if root is None:
            return result

        # 1. 添加所有最左边节点到栈
        while root:
            stack.append(root)
            root = root.left

        while stack:
            # 2. pop stack 然后添加到结果
            node = stack.pop()
            result.append(node.val)

            # 3. 查找当前node的右边节点是否为空，如果不为空，重复 step 1
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

        return result





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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        result = []

        if root is None:
            return result

        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        result.extend(left)
        result.append(root.val)
        result.extend(right)

        return result





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
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        result = []
        self.inorderHelper(root, result)
        return result


    def inorderHelper(self, root, result):
        if root is None:
            return result

        if root.left is not None:
            self.inorderHelper(root.left, result)

        result.append(root.val)

        if root.right is not None:
            self.inorderHelper(root.right, result)
