class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return None

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            while nums[start] == nums[end]:
                end -= 1

            mid = start + (end - start) // 2
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid

        if nums[start] < nums[end]:
            return nums[start]
        return nums[end]
