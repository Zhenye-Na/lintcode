# 595. Binary Tree Longest Consecutive Sequence

**Description**

Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The longest consecutive path need to be from parent to child (cannot be the reverse).

**Example**

Example 1:

```
Input:
   1
    \
     3
    / \
   2   4
        \
         5
Output:3
Explanation:
Longest consecutive sequence path is 3-4-5, so return 3.
```

Example 2:

```
Input:
   2
    \
     3
    / 
   2    
  / 
 1
Output:2
Explanation:
Longest consecutive sequence path is 2-3,not 3-2-1, so return 2.
```



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
    def longestConsecutive(self, root):
        # write your code here
        self.length = 1
        self._dfs(root)
        return self.length

    def _dfs(self, root):
        if root is None:
            return 0

        length_left = self._dfs(root.left)
        length_right = self._dfs(root.right)

        current = 1
        if root.left is not None and root.val + 1 == root.left.val:
            current = max(current, length_left + 1)

        if root.right is not None and root.val + 1 == root.right.val:
            current = max(current, length_right + 1)

        self.length = max(self.length, current)

        return current
```

