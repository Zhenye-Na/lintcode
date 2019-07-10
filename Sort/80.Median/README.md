# 80. Median

**Description**

Given a unsorted array with integers, find the `median` of it.

A median is the middle number of the array after it is sorted.

If there are even numbers in the array, return the `N/2-th` number after sorted.

> The size of array is not exceed `10000`

**Example**

Example 1:

```
Input: [4, 5, 1, 2, 3]
Output: 3
Explanation:
After sorting, [1,2,3,4,5], the middle number is 3
```

Example 2:

```
Input: [7, 9, 4, 5]
Output: 5
Explanation:
After sorting，[4,5,7,9], the second(4/2) number is 5
```

**Challenge**

`O(n)` time.


**Quick Sort**

考点:

区间第 `k` 大元素的查找

题解:

Quick Select 算法, 基于快排的分治思想, 递归实现, 从而复杂度接近 `O(n)`


```python
class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """

    def median(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return

        return self.sortQuick(nums, 0, len(nums) - 1, (len(nums) + 1) // 2)

    def sortQuick(self, nums, start, end, k):
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
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if start + k - 1 <= right:
            return self.sortQuick(nums, start, right, k)
        if start + k - 1 >= left:
            return self.sortQuick(nums, left, end, k - (left - start))

        return nums[right + 1]
```
