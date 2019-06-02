class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers that's previous permuation
    """
    def previousPermuation(self, nums):
        # write your code here
        if not nums or len(nums) <= 1:
            return nums

        # Find longest non-decreasing suffix
        i = len(nums) - 1
        while i > 0 and nums[i - 1] <= nums[i]:
            i -= 1

        if i <= 0:
            list.reverse(nums)
            return nums

        pivot = i - 1

        # Find rightmost element that is below the pivot
        j = len(nums) - 1
        while nums[j] >= nums[pivot]:
            j -= 1

        # Swap the pivot with j
        nums[pivot], nums[j] = nums[j], nums[pivot]

        # Reverse the suffix
        nums[i:] = nums[len(nums) - 1 : pivot : -1]

        return nums
