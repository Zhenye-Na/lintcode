# 70. Binary Tree Level Order Traversal II

**Description**

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

**Example**

Example 1:

```
Input:
{1,2,3}
Output:
[[2,3],[1]]
Explanation:
    1
   / \
  2   3
it will be serialized {1,2,3}
level order traversal
```

Example 2:

```
Input:
{3,9,20,#,#,15,7}
Output:
[[15,7],[9,20],[3]]
Explanation:
    3
   / \
  9  20
    /  \
   15   7
it will be serialized {3,9,20,#,#,15,7}
level order traversal
```

**BFS**

```python
from collections import deque

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        # write your code here
        traversal = []
        if root is None:
            return traversal

        queue = deque([])
        queue.append(root)

        while queue:
            level = []
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            traversal.insert(0, level)

        return traversal
```
