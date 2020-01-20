from bisect import bisect_left

class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return 0

        arr = [0 for _ in range(len(nums))]

        length = 0
        for num in nums:
            idx = bisect_left(arr, num, 0, length)

            arr[idx] = num

            if idx == length:
                length += 1

        return length
