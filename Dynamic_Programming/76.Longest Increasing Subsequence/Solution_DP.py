class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return 0

        # initialization
        # f[i] represents the max length of increasing subsequence which ends with nums[i]
        n = len(nums)
        f = [1 for _ in range(n)]

        # function: f[i] <- f[j] with contraints on j < i, nums[i] > nums[j]
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    f[i] = max(f[i], f[j] + 1)

        return max(f)
