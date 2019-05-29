# 1106. Maximum Binary Tree

Description

Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

```
1. The root is the maximum number in the array.
2. The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
3. The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
4. Construct the maximum tree by the given array and return the root node of this tree.
```

> The size of the given array will be in the range of `[1,1000]`.


**Example**

Example 1:

```
Input: {3,2,1,6,0,5}
Output: Return the tree root node representing the following tree:
     6
   /   \
  3     5
   \   / 
    2 0   
     \
      1
```

Example 2:

```
Input: {1,2,3,4}
Output: Return the tree root node representing the following tree:
        4
       /
      3
     /
    2
   /
  1    
```

**DFS**


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
    @param nums: an array
    @return: the maximum tree
    """
    def constructMaximumBinaryTree(self, nums):
        # Write your code here
        if not nums or len(nums) == 0:
            return None

        return self._dfs(nums)

    def _dfs(self, nums):
        if not nums or len(nums) == 0:
            return

        rootNum = max(nums)
        left = nums[:nums.index(rootNum)]
        right = nums[nums.index(rootNum) + 1: ]

        root = TreeNode(rootNum)
        root.right = self._dfs(right)
        root.left = self._dfs(left)

        return root
```
