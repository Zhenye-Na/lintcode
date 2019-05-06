# 39. Recover Rotated Sorted Array

**Description**

Given a rotated sorted array, recover it to sorted array in-place.

**Clarification**

What is rotated array?

For example, the orginal array is `[1,2,3,4]`, The rotated array of it can be `[1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]`


**Example**

Example1:

```
[4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]
```

Example2:

```
[6,8,9,1,2] -> [1,2,6,8,9]
```

**Challenge**

In-place, `O(1)` extra space and `O(n)` time.



**双指针 + 三部翻转法**


```python
class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return

        l = len(nums)
        for j in range(1, len(nums)):
            if nums[j - 1] > nums[j]:
                self.reverse(nums, 0, j - 1)
                self.reverse(nums, j, l - 1)
                self.reverse(nums, 0, l - 1)
                return nums
            
    def reverse(self, nums, start, end):
        i, j = start, end
        while i < j:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            i += 1
            j -= 1
```
