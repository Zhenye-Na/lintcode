class Solution:
    """
    @param nums: the list of salary
    @param target: the target of the sum
    @return: the cap it should be
    """
    def getCap(self, nums, target):
        # Write your code here.
        if not nums or len(nums) == 0:
            return -1

        nums.sort()
        lo, hi = 0, target // len(nums)
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if self._sumSalaries(nums, mid) >= target:
                hi = mid
            else:
                lo = mid

        if self._sumSalaries(nums, lo) >= target:
            return lo
        elif self._sumSalaries(nums, hi) >= target:
            return hi
        else:
            return hi + 1

    def _sumSalaries(self, nums, cap):
        total = 0
        for num in nums:
            total += max(cap, num)

        return total
