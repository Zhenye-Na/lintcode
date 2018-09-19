# 87. Remove Node in Binary Search Tree

- **Description**
    - Given a root of Binary Search Tree with unique value for each node. Remove the node with given value.
    - If there is no such a node with given value in the binary search tree, do nothing.
    - You should keep the tree still a binary search tree after removal.
- **Example**
    - Given binary search tree:

    ```
        5
       / \
      3   6
     / \
    2   4
    ```
    
    Remove `3`, you can either return:
    
    ```
        5
       / \
      2   6
       \
        4
    ```
    
    or
    
    ```
        5
       / \
      4   6
     /
    2
    ```


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
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def removeNode(self, root, value):
        # write your code here
        if root is None:
            return root

        # find target node
        if value < root.val:
            # left subtree
            root.left = self.removeNode(root.left, value)
        elif value > root.val:
            # right subtree
            root.right = self.removeNode(root.right, value)
        else:
            # if root is has 2 childs
            if root.left and root.right:
                maxNode = self.findMax(root)
                root.val = maxNode.val
                root.left = self.removeNode(root.left, maxNode.val)
            # left child
            elif root.left:
                root = root.left
            # right child
            elif root.right:
                root = root.right
            # leaf node
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