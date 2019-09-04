# 94. Binary Tree Maximum Path Sum

**Description**

Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

**Example**

```
Example 1:
	Input:  For the following binary tree（only one node）:
	2
	Output：2

Example 2:
	Input:  For the following binary tree:

      1
     / \
    2   3

	Output: 6
```

**Divide and Conquer**

最大的结果可能出现在 `root.val + leftsum + rightsum`, `leftsum + root.val`, `rightsum + root.val`, `root.val` 之中

```python
import sys

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
    def maxPathSum(self, root):
        # write your code here
        self.maxSum = -sys.maxsize
        self._find_max_path_sum(root)
        return self.maxSum

    def _find_max_path_sum(self, root):
        if root is None:
            return 0 

        leftSum = self._find_max_path_sum(root.left)
        rightSum = self._find_max_path_sum(root.right)

        self.maxSum = max(self.maxSum, root.val + leftSum + rightSum, leftSum + root.val, rightSum + root.val, root.val)
        return max(root.val + leftSum, root.val + rightSum)

```
