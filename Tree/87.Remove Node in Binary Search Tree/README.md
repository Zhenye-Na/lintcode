# 87. Remove Node in Binary Search Tree

**Description**

Given a root of Binary Search Tree with unique value for each node. Remove the node with given value. If there is no such a node with given value in the binary search tree, do nothing. You should keep the tree still a binary search tree after removal.

**Example**

Example 1

```
Input: 
Tree = {5,3,6,2,4}
k = 3

Output: {5,2,6,#,4} or {5,4,6,2}

Explanation:
Given binary search tree:
    5
   / \
  3   6
 / \
2   4

Remove 3, you can either return:

    5
   / \
  2   6
   \
    4

or

    5
   / \
  4   6
 /
2
```

Example 2

```
Input: 
Tree = {5,3,6,2,4}
k = 4

Output: {5,3,6,2}

Explanation:
Given binary search tree:

    5
   / \
  3   6
 / \
2   4

Remove 4, you should return:

    5
   / \
  3   6
 /
2
```


**References**

1. http://www.mathcs.emory.edu/~cheung/Courses/171/Syllabus/9-BinTree/BST-delete.html
2. https://www.youtube.com/watch?v=wcIRPqTR3Kc


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
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def removeNode(self, root, value):
        # write your code here
        if root is None:
            return root

        # check if node to delete is in left/right subtree
        if value < root.val:
            root.left = self.removeNode(root.left, value)
        elif value > root.val:
            root.right = self.removeNode(root.right, value)
        else:
            # if root is has 2 childs/only one child/leaf node
            if root.left and root.right:
                maxNode = self.findMax(root)
                root.val = maxNode.val
                root.left = self.removeNode(root.left, maxNode.val)
            elif root.left:
                root = root.left
            elif root.right:
                root = root.right
            else:
                root = None

        return root

    # find max node in left subtree of root
    def findMax(self, root):
        node = root.left
        while node.right:
            node = node.right
        return node
```
