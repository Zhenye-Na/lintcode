# 375. Clone Binary Tree

**Description**

For the given binary tree, return a deep copy of it.

```
You'd better not just return root to solve the problem.
```

**Example**

Example 1:

```
Input: {1,2,3,4,5}
Output: {1,2,3,4,5}
Explanation:
The binary tree is look like this:
     1
   /  \
  2    3
 / \
4   5
```

Example 2:

```
Input: {1,2,3}
Output: {1,2,3}
Explanation:
The binary tree is look like this:
   1
 /  \
2    3
```

**DFS**

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
    @param {TreeNode} root: The root of binary tree
    @return {TreeNode} root of new tree
    """
    def cloneTree(self, root):
        # Write your code here
        if root is None:
            return None

        clone_root = TreeNode(root.val)
        clone_root.left = self.cloneTree(root.left)
        clone_root.right = self.cloneTree(root.right)

        return clone_root
```

**BFS**

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
    @param root: The root of binary tree
    @return: root of new tree
    """
    def cloneTree(self, root):
        # write your code here
        if not root:
            return root

        # copy nodes
        nodes = self._getNodes(root)
        mapping = {}
        for node in nodes:
            mapping[node] = TreeNode(node.val)


        # copy edges
        for node in nodes:
            if node.left:
                mapping[node].left = mapping[node.left]
            if node.right:
                mapping[node].right = mapping[node.right]

        return mapping[root]


    def _getNodes(self, root):
        from collections import deque

        queue = deque([root])
        nodes = []
        while queue:
            node = queue.popleft()
            nodes.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return nodes
```