class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        if nums == None or len(nums) == 0 or target == None:
            return 0

        start, end = 0, len(nums) - 1
        while (start + 1 < end):
            mid = (start + end) // 2

            if nums[mid] >= target:
                end = mid
            elif nums[mid] < target:
                start = mid

        if nums[start] == target:
            return start
        elif nums[end] == target:
            return end
        else:
            return -1
