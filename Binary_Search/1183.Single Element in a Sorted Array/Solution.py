class Solution:
    """
    @param nums: a list of integers
    @return: return a integer
    """

    def singleNonDuplicate(self, nums):
        # write your code here
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if mid % 2 == 0:
                if nums[mid + 1] == nums[mid]:
                    start = mid
                else:
                    end = mid
            else:
                if nums[mid - 1] == nums[mid]:
                    start = mid
                else:
                    end = mid

        return nums[start] if start % 2 == 0 else nums[end]
