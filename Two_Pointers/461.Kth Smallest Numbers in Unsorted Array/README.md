# 461. Kth Smallest Numbers in Unsorted Array

**Description**

Find the `kth` smallest number in an *unsorted* integer array.


**Example**

Example 1:

```
Input: [3, 4, 1, 2, 5], k = 3
Output: 3
```

Example 2:

```
Input: [1, 1, 1], k = 2
Output: 1
```

**Challenge**

An `O(nlogn)` algorithm is acceptable, if you can do it in `O(n)`, that would be great.

**Quick Select**

Partition array

```python
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
```