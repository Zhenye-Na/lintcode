# 597. Subtree with Maximum Average

Description

Given a binary tree, find the subtree with maximum average. Return the root of the subtree.

```
LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with maximum average.
```

**Example**

Example 1

```
Input: {1,-5,11,1,2,4,-2}
Output: 11
Explanation:
The tree is look like this:
     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2 
The average of subtree of 11 is 4.3333, is the maximun.
```

Example 2

```
Input: {1,-5,11}
Output: 11
Explanation:
     1
   /   \
 -5     11
The average of subtree of 1,-5,11 is 2.333,-5,11. So the subtree of 11 is the maximun.
```



**Divide Conquer + Global variable**


```python
import sys

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        # write your code here
        self.max_avg = -sys.maxsize - 1
        self.node = None

        self._dfs(root)
        return self.node

    def _dfs(self, root):
        if root is None:
            return 0, 0

        # Devide Conquer
        left_sum, left_count = self._dfs(root.left)
        right_sum, right_count = self._dfs(root.right)

        avg = (left_sum + right_sum + root.val) / (left_count + right_count + 1)

        if avg > self.max_avg:
            self.node = root
            self.max_avg = avg

        return left_sum + right_sum + root.val, left_count + right_count + 1
```


**Divide Conquer**


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
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    # """
    def findSubtree2(self, root):
        max_avg, max_tree, _, _ = self.dfs(root)
        return max_tree
    
    def dfs(self, root):
        if root is None:
            return -sys.maxsize, None, 0, 0

        l_maxavg, l_maxtree, l_size, l_sum = self.dfs(root.left)
        r_maxavg, r_maxtree, r_size, r_sum = self.dfs(root.right)
        
        cur_size, cur_sum = l_size + r_size + 1, l_sum + r_sum + root.val
        cur_avg = cur_sum / cur_size

        if l_maxavg == max(l_maxavg, r_maxavg, cur_avg):
            return l_maxavg, l_maxtree, cur_size, cur_sum

        if r_maxavg == max(l_maxavg, r_maxavg, cur_avg):
            return r_maxavg, r_maxtree, cur_size, cur_sum

        return cur_avg, root, cur_size, cur_sum
```
