class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return nums

        first_zero = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                first_zero = i
                break

        if first_zero == -1:
            return nums

        left = first_zero
        for right in range(first_zero, len(nums)):
            if nums[right] == 0:
                continue
            else:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
                right += 1

        return nums
