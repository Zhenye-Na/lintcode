class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        # write your code here
        if not nums or len(nums) < 2:
            return 0

        nums.sort()
        diff = sys.maxsize
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                diff = min(diff, abs(nums[left] + nums[right] - target))
                left += 1
            else:
                diff = min(diff, abs(nums[left] + nums[right] - target))
                right -= 1

        return diff
