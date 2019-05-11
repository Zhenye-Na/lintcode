# 66. Binary Tree Preorder Traversal

**Description**

Given a binary tree, return the preorder traversal of its nodes' values.

```
The first data is the root node, followed by the value of the left and right son nodes, and "#" indicates that there is no child node.
The number of nodes does not exceed 20.
```

**Example**

Example 1:

```
Input: {1,2,3}
Output: [1,2,3]
Explanation:
   1
  / \
 2   3
it will be serialized {1,2,3}
Preorder traversal
```

Example 2:

```
Input: {1,#,2,3}
Output: [1,2,3]
Explanation:

    1
     \
      2
     /
    3
it will be serialized {1,#,2,3}
Preorder traversal
```

**Challenge**

Can you do it without recursion?


**Stack: non-recursion**

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
        while len(stack) != 0:
            node = stack.pop()
            result.append(node.val)

            # stack.push(node.right)
            if node.right is not None:
                stack.append(node.right)

            # stack.push(node.left)
            if node.left is not None:
                stack.append(node.left)

        return result
```


**Traverse helper function**


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
```


**Divide & Conquer**


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
```
