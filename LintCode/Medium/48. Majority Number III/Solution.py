"""
    48. Majority Number III
"""

# O(n) time
# O(n) extra space

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The majority number
    """
    def majorityNumber(self, nums, k):
        # write your code here
        limit = len(nums) / k
        dict = {}

        for num in nums:
            dict[num] = dict.get(num, 0) + 1

            if dict[num] > limit:
                return num
