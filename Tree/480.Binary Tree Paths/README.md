# 480. Binary Tree Paths

**Description**

Given a binary tree, return all root-to-leaf paths.

**Example**

Example 1:

```
Input:

   1
 /   \
2     3
 \
  5

Output:

[
  "1->2->5",
  "1->3"
]
```

Example 2:

```
Input:

   1
 /   
2     
 

Output:

[
  "1->2"
]
```


**Divide and Conquer**

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
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        self.result = []
        if not root:
            return self.result

        self.dfs(root, "")
        return self.result

    def dfs(self, root, path):

        # dfs has reached the leaf node, add path to result
        if root.left is None and root.right is None:
            path = path + str(root.val)
            self.result.append(path)
            return

        # turn left
        if root.left:
            self.dfs(root.left, path + str(root.val) + "->")

        # turn right
        if root.right:
            self.dfs(root.right, path + str(root.val) + "->")
```


**Traverse**

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
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        result = []
        if not root:
            return result

        self._traverse(root, result, [str(root.val)])
        return result

    def _traverse(self, root, result, path):
        
        if root.left is None and root.right is None:
            result.append("->".join(path))
            return

        if root.left:
            path.append(str(root.left.val))
            self._traverse(root.left, result, path)
            path.pop()

        if root.right:
            path.append(str(root.right.val))
            self._traverse(root.right, result, path)
            path.pop()
```




