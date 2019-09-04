# 246. Binary Tree Path Sum II

**Description**

You are given a binary tree in which each node contains a value. Design an algorithm to get all paths which sum to a given value. The path does not need to start or end at the root or a leaf, but it must go in a straight line down.


**Example**

Example 1:

```
Input:
{1,2,3,4,#,2}
6
Output:
[[2, 4],[1, 3, 2]]
Explanation:
The binary tree is like this:
    1
   / \
  2   3
 /   /
4   2
for target 6, it is obvious 2 + 4 = 6 and 1 + 3 + 2 = 6.
```

Example 2:

```
Input:
{1,2,3,4}
10
Output:
[]
Explanation:
The binary tree is like this:
    1
   / \
  2   3
 /   
4   
for target 10, there is no way to reach it.
```


**Traverse + Divide Conquer**

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
    def binaryTreePathSum2(self, root, target):
        # write your code here
        if root is None: 
            return []

        left   = self.binaryTreePathSum2(root.left, target)
        right  = self.binaryTreePathSum2(root.right, target)
        middle = self.fromRootToAny(root, target)
        return left + right + middle

    def fromRootToAny(self, root, target):
        results = []
        path = []
        self._dfs(root, target, results, path)
        return results
    
    def _dfs(self, root, target, results, path):
        if root is None:
            return 

        path.append(root.val)
        if root.val == target:
            results.append(path[:])

        self._dfs(root.left, target - root.val, results, path)
        self._dfs(root.right, target - root.val, results, path)

        path.pop()
```


**Failed Solution**

先得到所有从 `root` 到 `leaf node` 的所有路径 然后枚举每一条路径 在枚举每一个 `Treenode` 作为起点 看能不能找到和为 `target` 的路径

*Why?*

出现了重边的情况，对于{1,1,#,1,1} 求和为2 的情况，你虽然是求到了根节点到叶子节点的每一条路径，但是对于根节点到下一层节点的那条路径被重复计算了两次。

Input

```
{1,1,#,1,1}
2
```

Output

```
[[1,1],[1,1],[1,1],[1,1]]
```

Expected

```
[[1,1],[1,1],[1,1]]
```

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
    def binaryTreePathSum2(self, root, target):
        # write your code here
        self.root2LeafPaths = []
        self._get_paths(root, [])

        results = []
        for path in self.root2LeafPaths:
            for i in range(len(path)):
                tmp = []
                start_idx = i
                while i < len(path):
                    tmp.append(path[i])
                    if sum(tmp) == target:
                        results.append(tmp[:])
                        break

                    i += 1
        return results


    def _get_paths(self, root, path):
        if root is None:
            return

        if root.left is None and root.right is None:
            path.append(root.val)
            self.root2LeafPaths.append(path[:])
            return

        if root.left:
            self._get_paths(root.left, path + [root.val])
        if root.right:
            self._get_paths(root.right, path + [root.val])
```

*Failed Testcase*

Input

```
{1,1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1}
3
```

Output

```
[[1,-1,1,1,1],[1,-1,1,1,1],[1,-1,1,1,1],[1,-1,1,1,1],[1,-1,1,1,1],[1,-1,1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1]]
```

Expect

```
[[1,-1,1,1,1],[1,-1,1,1,1],[1,-1,1,1,1],[1,-1,1,1,1],[1,-1,1,1,1],[1,-1,1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1],[1,1,1,1,-1]]
```

不知道哪有问题 求评论