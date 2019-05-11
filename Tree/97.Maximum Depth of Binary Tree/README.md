# 97. Maximum Depth of Binary Tree

**Description**

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

**Example**

Example 1:

```
Input: tree = {}
Output: 0
Explanation: The height of empty tree is 0.
```

Example 2:

```
Input: tree = {1,2,3,#,#,4,5}
Output: 3	
Explanation: Like this:
   1
  / \                
 2   3                
    / \                
   4   5
it will be serialized {1,2,3,#,#,4,5}
```


**Divide and Conquer**

整颗树的最大深度 = max(左子树最大深度, 右子树最大深度) + 1 


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
        return self._find_depth(root)

    def _find_depth(self, root):
        if not root:
            return 0

        return max(self._find_depth(root.left), self._find_depth(root.right)) + 1
```


**Traverse**

遍历每一层时候, 在深度上加 `1` 再到下一层遍历

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
        self.max_depth = 0
        self._find_depth(root, 1)
        return self.max_depth

    def _find_depth(self, root, depth):
        if not root:
            return

        self.max_depth = max(self.max_depth, depth)
        self._find_depth(root.left, depth + 1)
        self._find_depth(root.right, depth + 1)
```
