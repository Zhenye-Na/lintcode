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