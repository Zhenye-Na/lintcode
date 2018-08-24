# 595. Binary Tree Longest Consecutive Sequence

Description
Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

Have you met this question in a real interview?  
Example
For example,

```
   1
    \
     3
    / \
   2   4
        \
         5
Longest consecutive sequence path is 3-4-5, so return 3.
```

```
   2
    \
     3
    /
   2    
  /
 1
Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
```



## Solution


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
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def __init__(self):
        self.length = 0

    def longestConsecutive(self, root):
        # write your code here
        self.helper(root)
        return self.length

    # Definition: find longest consecutive sequence in subtree
    def helper(self, root):
        if not root:
            return 0

        # 记录当前根节点
        sublength = 1

        # Divide
        left  = self.helper(root.left)
        right = self.helper(root.right)

        if root.left and root.left.val - 1 == root.val:
            sublength = max(sublength, left + 1)

        if root.right and root.right.val - 1 == root.val:
            sublength = max(sublength, right + 1)

        if sublength > self.length:
            self.length = sublength

        return sublength
```
