class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
