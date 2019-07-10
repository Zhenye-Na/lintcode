class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """

    def kthLargestElement(self, n, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return None

        return self._findK(0, len(nums) - 1, nums, len(nums) + 1 - n)

    def _findK(self, start, end, nums, n):
        if start == end:
            return nums[start]

        left, right = start, end
        pivot = nums[left + (right - left) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp
                left += 1
                right -= 1

        if start + n - 1 <= right:
            return self._findK(start, right, nums, n)
        if start + n - 1 >= left:
            return self._findK(left, end, nums, n - (left - start))

        return nums[right + 1]
