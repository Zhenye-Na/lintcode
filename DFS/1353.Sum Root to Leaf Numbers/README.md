# 1353. Sum Root to Leaf Numbers

**Description**

Given a binary tree containing digits from `0-9` only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path `1->2->3` which represents the number `123`.

Find the total sum of all root-to-leaf numbers.

```
A leaf is a node with no children.
```

**Example**

Example 1:

```
Input: {1,2,3}
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
```


Example 2:

```
Input: {4,9,0,5,1}
    4
   / \
  9   0
 / \
5   1
Output: 1026
Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
```

**DFS**

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
    @param root: the root of the tree
    @return: the total sum of all root-to-leaf numbers
    """
    def sumNumbers(self, root):
        # write your code here
        return self._dfs(root, 0)

    def _dfs(self, root, total):
        if root is None:
            return 0

        total = total * 10 + root.val
        if root.left is None and root.right is None:
            return total

        return self._dfs(root.left, total) + self._dfs(root.right, total)
```