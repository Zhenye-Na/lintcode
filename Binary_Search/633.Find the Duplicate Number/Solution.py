class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    def findDuplicate(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return 0

        lo, hi = 1, len(nums) - 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if self.count(nums, mid) <= mid:
                lo = mid
            else:
                hi = mid

        if self.count(nums, lo) <= lo:
            return hi
        return lo

    def count(self, nums, target):
        cnt = 0
        for num in nums:
            if num <= target:
                cnt += 1
        return cnt
