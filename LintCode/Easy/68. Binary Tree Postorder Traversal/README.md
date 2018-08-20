68. Binary Tree Postorder Traversal
Description
Given a binary tree, return the postorder traversal of its nodes' values.

Example
Given binary tree {1,#,2,3},

   1
    \
     2
    /
   3


return [3,2,1].

Challenge
Can you do it without recursion?

## Solution

### Stack: non-recursion **[Recommended]**

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
        stack  = []

        if root is None:
            return result

        stack.append(root)
        while stack:
            node = stack.pop()
            result.insert(0, node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return result
```


### Traverse helper function

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



### Divide & Conquer

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


### Iterative Postorder Traversal of Binary Tree with Two Stacks

[Iterative Postorder Traversal of Binary Tree - YouTube by Tushar](https://www.youtube.com/watch?v=qT65HltK2uE)

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

        # Initialize two stacks
        s1 = []
        s2 = []


        s1.append(root)
        while s1:
            node = s1.pop()
            s2.append(node)

            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)

        # pop stack2 to get postorder traversal
        while s2:
            result.append(s2.pop().val)

        return result
```
