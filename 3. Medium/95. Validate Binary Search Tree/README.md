# 95. Validate Binary Search Tree

Description
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
A single node tree is a BST
Have you met this question in a real interview?  
Example
An example:

```
  2
 / \
1   4
   / \
  3   5
```

The above binary tree is serialized as {2,1,4,#,#,3,5} (in level order).


## Solution

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
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        if root is None:
            return True

        MAX = sys.maxsize
        MIN = -sys.maxsize-1

        return self.dfs(root, MIN, MAX)

    def dfs(self, root, Min, Max):

        if root is None:
            return True
        if root.val >= Max or root.val <= Min :
            return False

        return self.dfs(root.left, Min, root.val) and self.dfs(root.right, root.val, Max)

```
