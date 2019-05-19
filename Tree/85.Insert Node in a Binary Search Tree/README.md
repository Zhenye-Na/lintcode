# 85. Insert Node in a Binary Search Tree

Description

Given a binary search tree and a new tree node, insert the node into the tree. You should keep the tree still be a valid binary search tree.

```
You can assume there is no duplicate values in this tree + node.
```

Example

```
Example 1:
	Input:  tree = {}, node = 1
	Output:  1
	
	Explanation:
	Insert node 1 into the empty tree, so there is only one node on the tree.
```

```
Example 2:
	Input: tree = {2,1,4,3}, node = 6
	Output: {2,1,4,3,6}
	
	Explanation: 
	Like this:



	  2             2
	 / \           / \
	1   4   -->   1   4
	   /             / \ 
	  3             3   6
```

**Challenge**

Can you do it without recursion?


**Non-Recursion**

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
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        if root is None:
            return node

        parent, current = None, root
        while current is not None:
            parent = current
            if current.val <= node.val:
                current = current.right
            else:
                current = current.left

        if parent.val <= node.val:
            parent.right = node
        else:
            parent.left = node

        return root
```


在树上定位要插入节点的位置。

1. 如果它大于当前根节点，则应该在右子树中，如果没有右子树则将该点作为右儿子插入；若存在右子树则在右子树中继续定位。
2. 如果它小于当前根节点，则应该在左子树中，处理同上。

二叉查找树中保证不插入已经存在的值


```python
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        # write your code here
        return self.__helper(root, node)
    
     # helper函数定义成私有属性   
    def __helper(self, root, node):     
        if root is None:
            return node
        if node.val < root.val:
            root.left = self.__helper(root.left, node)
        else:
            root.right = self.__helper(root.right, node)
        return root
```
