import sys

class Solution:
    """
    @param nums: an array
    @return: the minimum number of moves required to make all array elements equal
    """
    def minMoves(self, nums):
        # Write your code here
        result = 0
        minimum = min(nums)
        result = sum([num - minimum for num in nums])
        return result
