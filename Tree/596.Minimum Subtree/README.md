# 596. Minimum Subtree

**Description**

Given a binary tree, find the subtree with minimum sum. Return the root of the subtree.

```
LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with minimum sum and the given binary tree is not an empty tree.
```

**Example**

Example 1:

```
Input: {1,-5,2,1,2,-4,-5}
Output:1
Explanation:
The tree is look like this:
     1
   /   \
 -5     2
 / \   /  \
0   2 -4  -5 

The sum of whole tree is minimum, so return the root.
```

Example 2:

```
Input: {1}
Output:1
Explanation:
The tree is look like this:
   1
There is one and only one subtree in the tree. So we return 1.
```


**Traverse + Divide Conquer**

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
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        self.minimum = sys.maxsize
        self.minimum_node = None
        self._dfs(root)
        return self.minimum_node

    def _dfs(self, root):
        if root is None:
            return 0

        left_min = self._dfs(root.left)
        right_min = self._dfs(root.right)

        if left_min + right_min + root.val < self.minimum:
            self.minimum = left_min + right_min + root.val
            self.minimum_node = root

        return left_min + right_min + root.val
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
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # Divid and Conquer
        _, min_node, _ = self.min_tree(root)
        return min_node

    def min_tree(self, root):
        if root is None:
            return float("inf"), None, 0

        min_left, min_left_tree, sum_left = self.min_tree(root.left)
        min_right, min_right_tree, sum_right = self.min_tree(root.right)

        current_sum = sum_left + sum_right + root.val
        current_min = min(min_left, min_right, current_sum)

        if min_left == current_min:
            return current_min, min_left_tree, current_sum

        if min_right == current_min:
            return current_min, min_right_tree, current_sum

        return current_min, root, current_sum
```
