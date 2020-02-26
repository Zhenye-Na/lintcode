class Solution:
    """
    @param: nums: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySumII(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return [-1, -1]

        max_start, max_end, max_sum = self.maximumSubaarray(nums)
        min_start, min_end, min_sum = self.maximumSubaarray([- num for num in nums])

        n = len(nums)
        if min_start > 0 and min_end < n - 1:
            return [min_end + 1, min_start - 1]
        else:
            return [max_start, max_end]

    def maximumSubaarray(self, nums):
        prefix_sum, min_sum, max_sum = 0, 0, -sys.maxsize
        l, r, minidx = -1, -1, -1
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum - min_sum > max_sum:
                max_sum = prefix_sum - min_sum
                l, r = minidx + 1, i
            if prefix_sum < min_sum:
                min_sum = prefix_sum
                minidx = i

        return l, r, max_sum
