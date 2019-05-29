class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        prefix_sum = {0: -1}
        total = 0
        for i, num in enumerate(nums):
            total += num
            if total in prefix_sum:
                return prefix_sum[total] + 1, i
            prefix_sum[total] = i
            
        return -1, -1