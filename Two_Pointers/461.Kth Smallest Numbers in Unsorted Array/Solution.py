class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        # write your code here
        if not nums or len(nums) < k:
            return None

        return self._quickSelect(nums, 0, len(nums) - 1, k)

    def _quickSelect(self, nums, startIndex, endIndex, k):
        if startIndex == endIndex:
            return nums[startIndex]

        lo, hi = startIndex, endIndex
        pivot = nums[startIndex + (endIndex - startIndex) // 2]
        while lo <= hi:
            while lo <= hi and nums[lo] < pivot:
                lo += 1
            while lo <= hi and nums[hi] > pivot:
                hi -= 1
            if lo <= hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi -= 1

        if startIndex + k - 1 >= lo:
            return self._quickSelect(nums, lo, endIndex, k - (lo - startIndex))
        if startIndex + k - 1 <= hi:
            return self._quickSelect(nums, startIndex, hi, k)
        return nums[hi + 1]
