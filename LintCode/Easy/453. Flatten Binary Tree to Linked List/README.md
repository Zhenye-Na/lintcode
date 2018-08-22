# 453. Flatten Binary Tree to Linked List
Description
Flatten a binary tree to a fake "linked list" in pre-order traversal.

Here we use the right pointer in TreeNode as the next pointer in ListNode.

Have you met this question in a real interview?  
Example

```
              1
               \
     1          2
    / \          \
   2   5    =>    3
  / \   \          \
 3   4   6          4
                     \
                      5
                       \
                        6
```

Challenge
Do it in-place without any extra memory.

> Don't forget to mark the left child of each node to null. Or you will get Time Limit Exceeded or Memory Limit Exceeded.

## Solution

### Divide & Conquer

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
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root):
        # write your code here
        self.flattenHelper(root)


    def flattenHelper(self, root):
        if not root:
            return root

        left  = self.flattenHelper(root.left)
        right = self.flattenHelper(root.right)

        # Re-connect leftmost leaf to root.right
        if left:
            left.right = root.right
            root.right = root.left
            root.left = None

        # Return rightmost leaf for next recursion
        if right:
            return right

        # Return leftmost if there is no right subtree
        if left:
            return left

        # Reached leaf node, return leaf
        return root

```
