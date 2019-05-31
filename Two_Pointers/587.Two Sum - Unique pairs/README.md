# 587. Two Sum - Unique pairs

**Description**

Given an array of integers, find how many unique pairs in the array such that their sum is equal to a specific target number. Please return the number of pairs.

**Example**

Example 1:

```
Input: nums = [1,1,2,45,46,46], target = 47 
Output: 2
Explanation:
1 + 46 = 47
2 + 45 = 47
```

Example 2:

```
Input: nums = [1,1], target = 2 
Output: 1
Explanation:
1 + 1 = 2
```



```python
class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        if not nums or len(nums) < 2:
            return 0

        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        while left < right:
            if nums[left] + nums[right] == target:
                count += 1
                right -= 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            else:
                right -= 1

        return count
```
