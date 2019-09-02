class Solution:
    """
    @param nums: 
    @param sub: 
    @return: return a Integer array
    """

    def SimpleQueries(self, nums, sub):
        # write your code here
        if len(sub) == 0:
            return []

        if len(nums) == 0:
            return [0 for _ in range(len(sub))]

        # O(n logn)
        self.nums = nums
        self.nums.sort()
        results = []
        for target in sub:
            res = self._binarySearch(target)
            results.append(res)

        return results

    def _binarySearch(self, target):
        start, end = 0, len(self.nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.nums[mid] <= target:
                start = mid
            else:
                end = mid

        if self.nums[end] <= target:
            return end + 1
        if self.nums[start] <= target:
            return start + 1

        return 0
