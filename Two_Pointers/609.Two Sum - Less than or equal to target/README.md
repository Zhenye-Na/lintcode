# 609. Two Sum - Less than or equal to target

**Description**

Given an array of integers, find how many pairs in the array such that their sum is less than or equal to a specific target number. Please return the number of pairs.

**Example**

Example 1:

```
Input: nums = [2, 7, 11, 15], target = 24. 
Output: 5. 
Explanation:
2 + 7 < 24
2 + 11 < 24
2 + 15 < 24
7 + 11 < 24
7 + 15 < 25
```

Example 2:

```
Input: nums = [1], target = 1. 
Output: 0. 
```



```python
class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def twoSum5(self, nums, target):
        # write your code here
        if not nums or len(nums) < 2:
            return 0

        nums.sort()
        count = 0
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] <= target:
                count += right - left
                left += 1

            elif nums[left] + nums[right] > target:
                right -= 1

        return count
```