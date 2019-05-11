# 453. Flatten Binary Tree to Linked List

**Description**

Flatten a binary tree to a fake "linked list" in pre-order traversal.

Here we use the *right* pointer in `TreeNode` as the *next* pointer in `ListNode`.

```
Don't forget to mark the left child of each node to null. Or you will get Time Limit Exceeded or Memory Limit Exceeded.
```

**Example**

Example 1:

```
Input:
{1,2,5,3,4,#,6}
     1
    / \
   2   5
  / \   \
 3   4   6
Output:
{1,#,2,#,3,#,4,#,5,#,6}
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
```

Example 2:

```
Input:
{1}
1
Output:
{1}
1
```


**Challenge**

Do it in-place without any extra memory.


**DFS**

1. 将左子树变成 Linked List, 右子树变成 Linked List
2. 将右子树接在左子树的尾部, 并用新的左子树替换原来的右子树
3. 左子树赋值为 None


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
        if root is None:
            return None

        self.flatten(root.left)
        self.flatten(root.right)

        if root.left is None:
            return None

        node = root.left
        while node.right is not None:
            node = node.right

        node.right = root.right
        root.right = root.left
        root.left = None
```
