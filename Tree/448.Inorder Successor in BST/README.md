# 448. Inorder Successor in BST

**Description**

Given a binary search tree (See Definition) and a node in it, find the in-order successor of that node in the BST.

If the given node has no in-order successor in the tree, return `null`.

```
It's guaranteed p is one node in the given tree. (You can directly compare the memory address to find p)
```

**Example**

Example 1:

```
Input: {1,#,2}, node with value 1
Output: 2
Explanation:
  1
   \
    2
```

Example 2:

```
Input: {2,1,3}, node with value 1
Output: 2
Explanation: 
    2
   / \
  1   3
Binary Tree Representation
```

**Challenge**

`O(h)`, where `h` is the height of the BST.

用 `successor` 维护前一位, 左子树如果一直比 `p` 值大则一直向左找, 一旦左节点值大于 `p` 则 `p` 一定在右子树上


```python
"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        successor = None
        while root:
            if root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right
        
       
        return successor
```



首先要确定中序遍历的后继:

- 如果该节点有右子节点, 那么后继是其右子节点的子树中最左端的节点
- 如果该节点没有右子节点, 那么后继是离它最近的祖先, 该节点在这个祖先的左子树内.

使用循环实现:

- 查找该节点, 并在该过程中维护上述性质的祖先节点
- 查找到后, 如果该节点有右子节点, 则后继在其右子树内; 否则后继就是维护的那个祖先节点

使用递归实现:

- 如果根节点小于或等于要查找的节点, 直接进入右子树递归
- 如果根节点大于要查找的节点, 则暂存左子树递归查找的结果, 如果是 `null`, 则直接返回当前根节点; 反之返回左子树递归查找的结果.

在递归实现中, 暂存左子树递归查找的结果就相当于循环实现中维护的祖先节点.


```python
"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here
        if root is None:
            return None

        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        
        left = self.inorderSuccessor(root.left, p)
        if left is not None:
            return left
        return root
```
