# 578. Lowest Common Ancestor III

**Description**

Given the root and two nodes in a Binary Tree. Find the lowest common ancestor (LCA) of the two nodes.

The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.
Return `null` if `LCA` does not exist.

```
node A or node B may not exist in tree.
```

**Example**

Example 1

```
Input: 
{4, 3, 7, #, #, 5, 6}
3 5
5 6
6 7 
5 8
Output: 
4
7
7
null
Explanation:
  4
 / \
3   7
   / \
  5   6

LCA(3, 5) = 4
LCA(5, 6) = 7
LCA(6, 7) = 7
LCA(5, 8) = null
```

Example 2

```
Input:
{1}
1 1
Output: 
1
Explanation:
The tree is just a node, whose value is 1.
```

**思路**

因为有可能 A, B 并不在树上, 所以用两个变量 tracking 一下是否能在树上找到这两个点, 最后返回的时候, 如果两个点都存在就正常返回就好, 如果有不存在任何一个就直接返回 `null`

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""

class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        self.a = False
        self.b = False
        node = self._dfs(root, A, B)
        if self.a and self.b:
            return node
        return None

    def _dfs(self, root, A, B):
        if root is None:
            return None

        left = self._dfs(root.left, A, B)
        right = self._dfs(root.right, A, B)

        if root == A or root == B:
            if root == A:
                self.a = True
            else:
                self.b = True
            return root

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