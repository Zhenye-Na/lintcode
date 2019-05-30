class Solution:
    """
    @param: nums: an array of integers
    @return: nothing
    """
    def partitionArray(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return nums

        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and not self.isEven(nums[left]):
                left += 1
            while left <= right and self.isEven(nums[right]):
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return nums


    def isEven(self, num):
        return num % 2 == 0
