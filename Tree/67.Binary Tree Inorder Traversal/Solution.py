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

            # 3. 查找当前 node 的右边节点是否为空, 如果不为空, 重复 step 1
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
        if root is None:
            return []
            
        # 创建一个 dummy node，右指针指向 root
        # 并放到 stack 里，此时 stack 的栈顶 dummy
        # 是 iterator 的当前位置
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
            
        inorder = []
        # 每次将 iterator 挪到下一个点
        # 也就是调整 stack 使得栈顶到下一个点
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                inorder.append(stack[-1].val)
                
        return inorder




# Divide and Conquer

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
        if not root:
            return []

        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        return left + [root.val] + right



# Traverse

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
        self._traverse(root, result)
        return result


    def _traverse(self, root, result):
        if not root:
            return

        self._traverse(root.left, result)
        result.append(root.val)
        self._traverse(root.right, result)
