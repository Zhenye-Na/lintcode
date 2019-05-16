# 11. Search Range in Binary Search Tree

**Description**

Given a binary search tree and a range [k1, k2], return node values within a given range in ascending order.

**Example**

Example 1:

```
Input: {5},6,10
Output: []
        5
it will be serialized {5}
No number between 6 and 10
```

Example 2:

```
Input: {20,8,22,4,12},10,22
Output: [12,20,22]
Explanation：
        20
       /  \
      8   22
     / \
    4   12
it will be serialized {20,8,22,4,12}
[12,20,22] between 10 and 22
```

减少不在范围内的搜索, 避免搜索全部数据, 保证数据按照先序顺序存储返回

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
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        ret = []
        self.search(root, k1, k2, ret)
        return ret

    def search(self, root, k1, k2, ret):
        if root is None:
            return

        if root.val > k2:
            self.search(root.left, k1, k2, ret)
        elif root.val < k1:
            self.search(root.right, k1, k2, ret)
        else:
            self.search(root.left, k1, k2, ret)
            ret.append(root.val)
            self.search(root.right, k1, k2, ret)
```
