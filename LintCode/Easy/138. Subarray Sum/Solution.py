class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        # First prefix sum is 0, index is -1
        mapping = {0: -1}
        prefixSum = 0

        for idx, num in enumerate(nums):
            prefixSum += num
            if prefixSum in mapping:
                # subarray start from first index + 1
                return [mapping[prefixSum] + 1, idx]
            else:
                mapping[prefixSum] = idx
        # if not found, return [-1, -1]
        return [-1, -1]
