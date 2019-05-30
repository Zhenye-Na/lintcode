class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return 0

        # O(n) Time, O(n) Space
        left, right = 0, 0
        hist = set()
        while right < len(nums):
            if nums[right] not in hist:
                hist.add(nums[right])
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
            else:
                # nums[right] in history
                while right < len(nums) and nums[right] in hist:
                    right += 1

        return left
