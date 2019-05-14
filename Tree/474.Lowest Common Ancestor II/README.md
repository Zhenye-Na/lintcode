# 474. Lowest Common Ancestor II

**Description**

Given the root and two nodes in a Binary Tree. Find the *lowest common ancestor(LCA)* of the two nodes.

The lowest common ancestor is the node with largest depth which is the ancestor of both nodes.

The node has an extra attribute `parent` which point to the father of itself. The root's `parent` is `null`.

**Example**

Example 1:

```
Input: {4,3,7,#,#,5,6},3,5
Output: 4
Explanation: 
      4
     / \
    3   7
       / \
      5   6
LCA(3, 5) = 4
```

Example 2:

```
Input: {4,3,7,#,#,5,6},5,6
Output: 7
Explanation:
      4
     / \
    3   7
       / \
      5   6
LCA(5, 6) = 7
```


有 `parent` 指针, 可求到 从 `A`, `B` 到 `root` 节点的路径. 从路径的 `root` 节点出发, 找到第一个不同的节点, 返回上一个结果.


```python
"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        # write your code here
        path_a = self._find_path(root, A)
        path_b = self._find_path(root, B)

        ancestor = root
        for (a, b) in zip(reversed(path_a), reversed(path_b)):
            if a.val == b.val:
                ancestor = a
            else:
                break
        return ancestor


    def _find_path(self, root, target):
        node = target
        path = []
        while node is not None:
            path.append(node)
            node = node.parent

        return path
```
