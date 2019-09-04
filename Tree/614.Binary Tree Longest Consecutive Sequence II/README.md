# 614. Binary Tree Longest Consecutive Sequence II

**Description**

Given a binary tree, find the length(number of nodes) of the longest consecutive sequence (Monotonic and adjacent node values differ by `1`) path.

The path could be start and end at any node in the tree

**Example**

Example 1:

```
Input:
{1,2,0,3}
Output:
4
Explanation:
    1
   / \
  2   0
 /
3
0-1-2-3
```

Example 2:

```
Input:
{3,2,2}
Output:
2
Explanation:
    3
   / \
  2   2
2-3
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
    def longestConsecutive2(self, root):
        # write your code here
        self.maxLength = 0
        self._find_path(root)
        return self.maxLength

    def _find_path(self, root):
        if not root:
            return 0, 0

        up_length = 1
        down_length = 1

        left_up, left_down = self._find_path(root.left)
        right_up, right_down = self._find_path(root.right)

        if root.left:
            if root.left.val - 1 == root.val:
                up_length = max(up_length, left_up + 1)
            if root.left.val + 1 == root.val:
                down_length = max(down_length, left_down + 1)

        if root.right:
            if root.right.val - 1 == root.val:
                up_length = max(up_length, right_up + 1)
            if root.right.val + 1 == root.val:
                down_length = max(down_length, right_down + 1)

        self.maxLength = max(self.maxLength, up_length + down_length - 1)
        return up_length, down_length
```
