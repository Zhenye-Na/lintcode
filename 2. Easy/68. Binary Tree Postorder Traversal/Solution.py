# Traverse helper function

```python
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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        result = []
        self.helper(root, result)
        return result

    def helper(self, root, result):
        if root is None:
            return

        self.helper(root.left, result)
        self.helper(root.right, result)
        result.append(root.val)
```


# Divide & Conquer

```python
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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        result = []
        if root is None:
            return result
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
```
