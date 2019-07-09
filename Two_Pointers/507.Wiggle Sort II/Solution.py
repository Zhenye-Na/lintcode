class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """

    def wiggleSort(self, nums):
        # write your code here
        median = self.findMedian(nums)
        n = len(nums)
        i = 0
        even, odd = n - 1 if (n - 1) % 2 == 0 else n - 2, 1

        while i < n:
            if nums[i] > median and (i % 2 != 1 or i > odd):
                nums[i], nums[odd] = nums[odd], nums[i]
                odd += 2
                continue

            if nums[i] < median and (i % 2 != 0 or even > i):
                nums[i], nums[even] = nums[even], nums[i]
                even -= 2
                continue

            i += 1

    def findMedian(self, nums):
        n = len(nums)
        if n % 2 == 0:
            return (self.findKth(nums, n // 2, 0, n - 1) + self.findKth(nums, n // 2 + 1, 0, n - 1)) / 2
        else:
            return self.findKth(nums, n // 2, 0, n - 1)

    def findKth(self, nums, k, start, end):
        if start == end:
            return nums[start]

        pivot = nums[(start + end) // 2]

        left, right = start, end
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1

            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if start <= k - 1 <= right:
            return self.findKth(nums, k, start, right)
        elif left <= k - 1 <= end:
            return self.findKth(nums, k, left, end)
        else:
            return nums[k - 1]
