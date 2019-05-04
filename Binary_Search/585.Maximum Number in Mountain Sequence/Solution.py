class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return None

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return nums[mid]
            elif nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1]:
                start = mid
            else:
                end = mid

        if nums[start] > nums[end]:
            return nums[start]
        return nums[end]
