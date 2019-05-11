# 93. Balanced Binary Tree

**Description**

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than `1`.

**Example**

Example 1:

```
Input: tree = {1,2,3}
Output: true

Explanation:
This is a balanced binary tree.
	  1  
	 / \                
	2   3
```

	
Example 2:

```
Input: tree = {3,9,20,#,#,15,7}
Output: true

Explanation:
This is a balanced binary tree.

	  3  
	 / \                
	9  20                
	  /  \                
	 15   7 
```
	
Example 3:

```
Input: tree = {1,#,2,3,4}
Output: false

Explanation:
This is not a balanced tree. 
The height of node 1's right sub-tree is 2 but left sub-tree is 0.

	 1  
	  \                
	   2                
	  / \                
	 3   4
```



**Divide and Conquer**

分治的思想解决:

- 整颗二叉树是否平衡在于
    - 1) 左子树是不是平衡二叉树
    - 2) 右子树是不是平衡二叉树
    - 3) 如果左右子树都是, 那么高度差是不是小于等于1
- 用两个返回值分别代表当前高度以及当前层数是否平衡


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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):
        # write your code here
        height, balanced = self._isBalanced(root)
        return balanced

    def _isBalanced(self, root):
        if not root:
            return 0, True

        left_height, left_is_balanced = self._isBalanced(root.left)
        right_height, right_is_balanced = self._isBalanced(root.right)

        if not left_is_balanced or not right_is_balanced:
            return 0, False

        if abs(left_height - right_height) > 1:
            return 0, False

        return max(left_height, right_height) + 1, True
```
