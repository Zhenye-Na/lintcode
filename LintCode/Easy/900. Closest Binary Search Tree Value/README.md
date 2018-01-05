# 900. Closest Binary Search Tree Value

- **Description**
    - Given a non-empty binary search tree and a target value, find the value in the **BST** that is closest to the 
    - Given target value is a **floating point**.
    - You are guaranteed to have only one unique value in the BST that is closest to the target. 
- **Example**
    - Given `root = {1}`, `target = 4.428571`, return `1`.


## Solution

### lowerBound and upperBound

算法很简单，求出 `lowerBound` 和 `upperBound`。即 `< target` 的最大值和 `>= target` 的最小值。然后在两者之中去比较谁更接近，然后返回即可。

时间复杂度为 `O(h)`，注意如果你使用 in-order traversal，时间复杂度会是 `O(n)` 并不是最优的。另外复杂度也不是 `O(logn)` 因为 BST 并不保证树高是 `logn` 的。

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
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        if not root:
            return
        lowerBound = self.lower(root, target)
        upperBound = self.upper(root, target)

        if lowerBound is None:
            return upperBound.val

        if upperBound is None:
            return lowerBound.val

        if abs(lowerBound.val - target) < abs(upperBound.val - target):
            return lowerBound.val
        else:
            return upperBound.val

    def lower(self,root,target):
        if root is None:
            return None

        if root.val > target:
            return self.lower(root.left, target)

        lowerNode = self.lower(root.right, target)
        if lowerNode:
            return lowerNode

        return root

    def upper(self,root,target):
        if root is None:
            return None

        if root.val < target:
            return self.upper(root.right, target)

        upperNode = self.upper(root.left, target)
        if upperNode:
            return upperNode

        return root
```

### Traverse + Compare

- Time  `O(n)`
- Space `O(n)`

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
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        val = self.traverse(root)
        return self.closest(val, target)

    def traverse(self, root):
        val = []
        q   = []

        q.append(root)
        while q:
            size = len(q)

            for i in range(size):
                node = q.pop(0)
                val.append(node.val)

                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)

        return val

    def closest(self, val, target):
        diff = max(val) + target
        close = val[0]
        for v in val:
            if abs(v - target) < diff:
                diff  = abs(v - target)
                close = v

        return close

```
