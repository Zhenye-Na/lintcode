"""
    47. Majority Element II
"""

# O(n logn) time
# O(1) extra space

class Solution:
    """
    @param: nums: a list of integers
    @return: The majority number that occurs more than 1/3
    """
    def majorityNumber(self, nums):
        # write your code here
        nums.sort()

        step = len(nums) / 3
        for idx, val in enumerate(nums):
            if val == nums[idx + step]:
                return val



# O(n) time
# O(n) space

class Solution:
    """
    @param: nums: a list of integers
    @return: The majority number that occurs more than 1/3
    """
    def majorityNumber(self, nums):
        # write your code here
        mapping = {}
        limit = len(nums) / 3

        for num in nums:
            mapping[num] = mapping.get(num, 0) + 1

            if mapping[num] > limit:
                return num
