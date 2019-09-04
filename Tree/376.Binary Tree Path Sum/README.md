# 376. Binary Tree Path Sum

**Description**

Given a binary tree, find all paths that sum of the nodes in the path equals to a given number `target`.

A valid path is *from root node to any of the leaf nodes*.

**Example**

Example 1:

```
Input:
{1,2,4,2,3}
5
Output: [[1, 2, 2],[1, 4]]
Explanation:
The tree is look like this:
	     1
	    / \
	   2   4
	  / \
	 2   3
For sum = 5 , it is obviously 1 + 2 + 2 = 1 + 4 = 5
```

Example 2:

```
Input:
{1,2,4,2,3}
3
Output: []
Explanation:
The tree is look like this:
	     1
	    / \
	   2   4
	  / \
	 2   3
Notice we need to find all paths from root node to leaf nodes.
1 + 2 + 2 = 5, 1 + 2 + 3 = 6, 1 + 4 = 5 
There is no one satisfying it.
```

**Divide Conquer / DFS**

要从根节点到任意一个叶子结点才算一条合法路径

思路:

1. 在左子树/右子树分别去找这样的路径
2. 每次递归传递的 `target` 主次减小, 实际传入 `target - root.val`
3. 当发现叶子结点同时该叶子节点的值与传入的 `target` 相等时, 就把这个 leaf node 加入到 path 中, 并将整个 path 记录下来


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
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum(self, root, target):
        # write your code here
        self.paths = []
        self._dfs(root, target, [])
        return self.paths

    def _dfs(self, root, target, path):
        if root is None:
            return

        if target == root.val and root.left is None and root.right is None:
            path.append(root.val)
            self.paths.append(path[:])
            return

        self._dfs(root.left, target - root.val, path + [root.val])
        self._dfs(root.right, target - root.val, path + [root.val])
```
