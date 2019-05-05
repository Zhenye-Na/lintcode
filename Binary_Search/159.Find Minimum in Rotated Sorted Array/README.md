# 159. Find Minimum in Rotated Sorted Array

**Description**

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., `0 1 2 4 5 6 7` might become `4 5 6 7 0 1 2`).

Find the minimum element.

> You can assume no duplicate exists in the array.

**Example**


Example 1:

```
Input: [4, 5, 6, 7, 0, 1, 2]
Output: 0

Explanation:
The minimum value in an array is 0.
```

Example 2:

```
Input: [2,1]
Output: 1

Explanation:
The minimum value in an array is 1.
```


```python
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return None

        start, end = 0, len(nums) - 1
        last_number = nums[-1]

        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > last_number:
                start = mid
            else:
                end = mid

        if nums[start] < nums[end]:
            return nums[start]
        return nums[end]
```
