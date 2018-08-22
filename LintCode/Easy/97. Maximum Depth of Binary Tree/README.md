# 97. Maximum Depth of Binary Tree

- **Description**
    - Given a binary tree, find its maximum depth.
    - The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
- **Example**
    - Given a binary tree as follow:

    ```
      1
     / \
    2   3
       / \
      4   5  
    ```

    - The maximum depth is 3.


## Solution

### `Divide & Conquer`

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
```


### Traverse

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
```
