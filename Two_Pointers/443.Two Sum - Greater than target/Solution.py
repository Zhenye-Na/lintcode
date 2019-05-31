class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        # write your code here
        if not nums or len(nums) < 2:
            return 0

        nums.sort()
        count = 0
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] <= target:
                left += 1
            else:
                count += right - left
                right -= 1

        return count
