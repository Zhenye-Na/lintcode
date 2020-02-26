class Solution:
    """
    @param: nums: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySum(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return [0, 0]

        prefix_sum, min_sum, max_sum = 0, 0, -sys.maxsize
        i, j, min_idx = -1, -1, -1
        for idx, num in enumerate(nums):
            prefix_sum += num
            if prefix_sum - min_sum > max_sum:
                max_sum = prefix_sum - min_sum
                i, j = min_idx + 1, idx
            if prefix_sum < min_sum:
                min_sum = prefix_sum
                min_idx = idx

        return [i, j]
