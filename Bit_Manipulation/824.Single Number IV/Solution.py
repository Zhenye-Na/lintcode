class Solution:
    """
    @param nums: The number array
    @return: Return the single number
    """
    def getSingleNumber(self, nums):
        # Write your code here
        if not nums or len(nums) == 0:
            return -1

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if mid % 2 == 0:
                if nums[mid] != nums[mid + 1]:
                    right = mid
                else:
                    left = mid
            else:
                if mid >= 1 and nums[mid] != nums[mid - 1]:
                    right = mid
                else:
                    left = mid

        return nums[left] if left % 2 == 0 else nums[right]
