class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        start, end = 0, len(nums) - 1
        target = nums[-1]
        while (start + 1 < end):
            mid = (start + end) // 2

            if (nums[mid] > target):
                start = mid
            elif (nums[mid] < target):
                end = mid


        if nums[start] < nums[end]:
            return nums[start]
        else:
            return nums[end]
