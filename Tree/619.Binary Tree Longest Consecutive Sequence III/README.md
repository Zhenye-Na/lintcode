# 619. Binary Tree Longest Consecutive Sequence III

**Description**

This is the follow up problem for `Binary Tree Longest Consecutive Sequence II`.

Given a `k-ary tree`, find the length of the longest consecutive sequence path.

The path could be start and end at any node in the tree

**Example**

Example 1:

```
Input:
5<6<7<>,5<>,8<>>,4<3<>,5<>,31<>>>
Output:
5
Explanation:
     5
   /   \
  6     4
 /|\   /|\
7 5 8 3 5 3

return 5, // 3-4-5-6-7
```

Example 2:

```
Input:
1<>
Output:
1
```

```python
"""
Definition for a multi tree node.
class MultiTreeNode(object):
    def __init__(self, x):
        self.val = x
        children = [] # children is a list of MultiTreeNode
"""

class Solution:
    # @param {MultiTreeNode} root the root of k-ary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive3(self, root):
        # Write your code here
        self.maxLength = 0
        self._find_path(root)
        return self.maxLength

    def _find_path(self, root):

        if root is None:
            return 0

        up, down = 0, 0
        for child in root.children:
            child_up, child_down = self._find_path(child)
            if child.val - 1 == root.val:
                up = max(up, child_up + 1)
            elif child.val + 1 == root.val:
                down = max(down, child_down + 1)
            self.maxLength = max(self.maxLength, up + down + 1)

        return up, down
```
