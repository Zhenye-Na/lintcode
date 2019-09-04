# 1183. Single Element in a Sorted Array

**Description**


Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

**Example**

Example 1:

```
Input: [1,1,2,3,3,4,4,8,8]
Output: 2
```

Example 2:

```
Input: [3,3,7,7,10,11,11]
Output: 10
```

Your solution should run in `O(log n)` time and `O(1)` space.

```python
class Solution:
    """
    @param nums: a list of integers
    @return: return a integer
    """

    def singleNonDuplicate(self, nums):
        # write your code here
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if mid % 2 == 0:
                if nums[mid + 1] == nums[mid]:
                    start = mid
                else:
                    end = mid
            else:
                if nums[mid - 1] == nums[mid]:
                    start = mid
                else:
                    end = mid

        return nums[start] if start % 2 == 0 else nums[end]

```