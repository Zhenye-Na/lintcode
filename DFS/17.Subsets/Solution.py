class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return [[]]

        subsets = []
        nums.sort()
        self._find_subsets(subsets, [], nums, 0)
        return subsets

    def _find_subsets(self, subsets, subset, nums, start):
        subsets.append(subset[:])

        for i in range(start, len(nums)):
            subset.append(nums[i])
            self._find_subsets(subsets, subset, nums, i + 1)
            subset.pop()
