# 5. Kth Largest Element

**Description**

Find K-th largest element in an array.

You can swap elements in the array

**Example**

Example 1:

```
Input:
n = 1, nums = [1,3,4,2]
Output:
4
```

Example 2:

```
Input:
n = 3, nums = [9,3,2,4,8]
Output:
4
```

**Challenge**

`O(n)` time, `O(1)` extra memory.


**Quick Sort**

快排中 partition 的模板相关

```python
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
```
