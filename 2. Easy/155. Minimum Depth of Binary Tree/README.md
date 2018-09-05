# 155. Minimum Depth of Binary Tree

- **Description**
    - Given a binary tree, find its **minimum depth**.
    - The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
- **Example**
    - Given a binary tree as follow:

    ```
      1
     / \
    2   3
       / \
      4   5  
    ```

    - The minimum depth is `2`.


## Solution

### Recursion

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys
class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        if not root:
            return 0
        return self.helper(root)


    def helper(self, root):
        # base case
        if not root:
            return sys.maxint

        # recursive case
        else:
            # leaf node
            if not root.left and not root.right:
                return 1

            # recursively compare minDepth of left and right subtree
            return min(self.helper(root.left), self.helper(root.right)) + 1
```
