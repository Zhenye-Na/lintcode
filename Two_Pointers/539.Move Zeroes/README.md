# 539. Move Zeroes

**Description**

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

```
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
```

**Example**

Example 1:

```
Input: nums = [0, 1, 0, 3, 12],
Output: [1, 3, 12, 0, 0].
```

Example 2:

```
Input: nums = [0, 0, 0, 3, 1],
Output: [3, 1, 0, 0, 0].
```


```python
class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return nums

        first_zero = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                first_zero = i
                break

        if first_zero == -1:
            return nums

        left = first_zero
        for right in range(first_zero, len(nums)):
            if nums[right] == 0:
                continue
            else:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
                right += 1

        return nums
```
