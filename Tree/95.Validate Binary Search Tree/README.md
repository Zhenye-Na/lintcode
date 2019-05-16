# 95. Validate Binary Search Tree

**Description**

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

```
The left subtree of a node contains only nodes with keys **less than** the node's key.
The right subtree of a node contains only nodes with keys **greater than** the node's key.
Both the left and right subtrees must also be binary search trees.
A single node tree is a BST
```

**Example**

Example 1:

```
Input:  {-1}
Output: true
Explanation:
For the following binary tree（only one node）:
	      -1
This is a binary search tree.
```

Example 2:

```
Input: {2,1,4,#,#,3,5}
Output: true
For the following binary tree:
	  2
	 / \
	1   4
	   / \
	  3   5
This is a binary search tree.
```

**Divide Conquer 1**

```python
import sys

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    
    def isValidBST(self, root):
        # write your code here
        if root is None:
            return True

        leftMax = sys.maxsize
        rightMin = -sys.maxsize - 1
        return self.dfs(root, rightMin, leftMax)
        
    def dfs(self, root, Min, Max): 
        if root is None:
            return True

        if root.val >= Max or root.val <= Min :
            return False
        
        return self.dfs(root.left, Min, root.val) and self.dfs(root.right, root.val, Max)
```


**Divide Conquer 2**

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
        isBST, _, _ = self._validate(root)
        return isBST

    def _validate(self, root):
        if not root:
            return True, None, None

        leftIsBST, leftMin, leftMax = self._validate(root.left)
        rightIsBST, rightMin, rightMax = self._validate(root.right)

        # 左右子树不是 BST 直接返回不是
        if not leftIsBST or not rightIsBST:
            return False, None, None

        # left max 要大于根节点
        if leftMax is not None and leftMax >= root.val:
            return False, None, None

        # right min 要小于根节点
        if rightMin is not None and rightMin <= root.val:
            return False, None, None

        # is BST
        minNode = leftMin if leftMin is not None else root.val
        maxNode = rightMax if rightMax is not None else root.val

        return True, minNode, maxNode
```