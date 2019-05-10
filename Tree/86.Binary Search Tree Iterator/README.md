# 86. Binary Search Tree Iterator

**Description**

Design an iterator over a binary search tree with the following rules:

```
Elements are visited in ascending order (i.e. an in-order traversal)
next() and hasNext() queries run in O(1) time in average.
```

**Example**

Example 1

```
Input: {10,1,11,#,6,#,12}
Output: [1, 6, 10, 11, 12]
Explanation:
The BST is look like this:
  10
  /\
 1 11
  \  \
   6  12
You can return the inorder traversal of a BST [1, 6, 10, 11, 12]
```

Example 2

```
Input: {2,1,3}
Output: [1,2,3]
Explanation:
The BST is look like this:
  2
 / \
1   3
You can return the inorder traversal of a BST tree [1,2,3]
```

**Challenge**

Extra memory usage `O(h)`, `h` is the height of the tree.

*Super Star:* Extra memory usage `O(1)`



**考点: 非递归的中序遍历 stack**

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        self.current_node = root

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        # write your code here
        return self.current_node is not None or len(self.stack) > 0

    """
    @return: return next node
    """
    def next(self):
        # write your code here
        while self.current_node is not None:
            self.stack.append(self.current_node)
            self.current_node = self.current_node.left

        self.current_node = self.stack.pop()
        next_node = self.current_node
        self.current_node = self.current_node.right # current_node could be None
        return next_node
```
