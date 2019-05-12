# 88. Lowest Common Ancestor of a Binary Tree

**Description**

Given the root and two nodes in a Binary Tree. Find the lowest common ancestor(LCA) of the two nodes.

The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.

```
Assume two nodes exist in the given tree.
```

**Example**

Example 1:

```
Input: {1},1,1
Output: 1
Explanation:
 For the following binary tree（only one node）:
         1
 LCA(1,1) = 1
```

Example 2:

```
Input: {4,3,7,#,#,5,6},3,5
Output: 4
Explanation:
 For the following binary tree:

      4
     / \
    3   7
       / \
      5   6
			
 LCA(3, 5) = 4
```


使用分法法, 每次都返回一个可能的 LCA, 返回的时候分几种情况

1. 如果两边返回的都不是 `null`
    - 如果相等，那么就是 LCA, 返回其中任意一个即可
    - 如果不相等, 那么root 为 LCA
2. 如果 `left != null && right == null` , 返回left
3. 如果 `right != null && left == null` , 返回right
4. 最后两边都是 `null` , 则返回 `null`


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
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        node =  self._dfs(root, A, B)
        return node

    def _dfs(self, root, A, B):
        if root is None:
            return None

        if root == A or root == B:
            return root

        left = self._dfs(root.left, A, B)
        right = self._dfs(root.right, A, B)


        # A 和 B 一边一个
        if left and right: 
            return root
        
        # 左子树有一个点或者左子树有LCA
        if left:
            return left
        
        # 右子树有一个点或者右子树有LCA
        if right:
            return right
        
        # 左右子树啥都没有
        return None
```
