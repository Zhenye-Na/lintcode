# 472. Binary Tree Path Sum III

**Description**

Give a binary tree, and a target number, find all path that the sum of nodes equal to target, the path could be start and end at any node in the tree.

**Example**

Example 1

```
Input: {1,2,3,4},6
Output: [[2, 4],[2, 1, 3],[3, 1, 2],[4, 2]]
Explanation:
The tree is look like this:
    1
   / \
  2   3
 /
4
```

Example 2

```
Input: {1,2,3,4},3
Output: [[1,2],[2,1],[3]]
Explanation:
The tree is look like this:
    1
   / \
  2   3
 /
4
```

**思路**

现在的题意是可以从任何一点出发，而且有 `parent` 节点。

那么我们其实是 traverse 一遍这棵树, 在每一点, 我们出发找有没有符合条件的路径.

在每一点我们可以有三个方向: 左边, 右边, 和上面. 但是我们需要避免回头, 所以需要一个 `father` 节点的参数.


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
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum3(self, root, target):
        # write your code here
        results = []
        self._dfs(root, target, results)
        return results

    def _dfs(self, root, target, results):
        if root is None:
            return

        path = []
        self._findSum(root, None, target, path, results)

        self._dfs(root.left, target, results)
        self._dfs(root.right, target, results)

    def _findSum(self, root, father, target, path, results):
        path.append(root.val)
        target -= root.val

        if target == 0:
            results.append(path[:])

        if root.parent not in [None, father]:
            self._findSum(root.parent, root, target, path, results)

        if root.left not in [None, father]:
            self._findSum(root.left, root, target, path, results)

        if root.right not in [None, father]:
            self._findSum(root.right, root, target, path, results)

        path.pop()
```