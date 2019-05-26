class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return [[]]
        subsets = []
        nums.sort()
        self._find_subsets(nums, subsets, [], 0)
        return subsets

    def _find_subsets(self, nums, subsets, subset, start):
        subsets.append(subset[:])

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue

            subset.append(nums[i])
            self._find_subsets(nums, subsets, subset, i + 1)
            subset.pop()
