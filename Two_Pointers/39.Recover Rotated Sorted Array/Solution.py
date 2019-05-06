class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return

        l = len(nums)
        for j in range(1, len(nums)):
            if nums[j - 1] > nums[j]:
                self.reverse(nums, 0, j - 1)
                self.reverse(nums, j, l - 1)
                self.reverse(nums, 0, l - 1)
                return nums
            
    def reverse(self, nums, start, end):
        i, j = start, end
        while i < j:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i += 1
            j -= 1
