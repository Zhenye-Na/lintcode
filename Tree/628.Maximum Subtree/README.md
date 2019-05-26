# 628. Maximum Subtree

**Description**

Given a binary tree, find the subtree with maximum sum. Return the root of the subtree.

```
LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with maximum sum and the given binary tree is not an empty tree.
```

**Example**

Example 1:

```
Input:
{1,-5,2,0,3,-4,-5}
Output:3
Explanation:
The tree is look like this:
     1
   /   \
 -5     2
 / \   /  \
0   3 -4  -5
The sum of subtree 3 (only one node) is the maximum. So we return 3.
```

Example 2:

```
Input:
{1}
Output:1
Explanation:
The tree is look like this:
   1
There is one and only one subtree in the tree. So we return 1.
```

**Divide Conquer**

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
    @return: the maximum weight node
    """
    maximum = - sys.maxsize - 1
    node = None

    def findSubtree(self, root):
        # write your code here
        self._dfs(root)
        return self.node

    def _dfs(self, root):
        if not root:
            return 0

        leftTotal = self._dfs(root.left)
        rightTotal = self._dfs(root.right)

        if leftTotal + rightTotal + root.val > self.maximum:
            self.maximum = leftTotal + rightTotal + root.val
            self.node = root

        return leftTotal + rightTotal + root.val
```