class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def __init__(self):
        self.results = []
        self.length = 0

    def permute(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            self.results.append([])
            return self.results

        self.length = len(nums)
        self.backtracking(0, nums, [])
        return self.results


    def backtracking(self, startIndex, nums, permutation):
        if len(permutation) == len(nums):
            self.results.append(permutation[:])
            return

        for idx in xrange(startIndex, self.length):

            if nums[idx] in permutation:
                continue

            # add new element
            permutation.append(nums[idx])

            # explore
            self.backtracking(0, nums, permutation)

            # remove element
            permutation.pop(-1)
