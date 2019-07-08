# 533. Two Sum - Closest to target

**Description**

Given an array nums of `n` integers, find two integers in nums such that the sum is closest to a given number, `target`.

```
Return the absolute value of difference between the sum of the two integers and the target.
```

**Example**

Example 1

```
Input:  nums = [-1, 2, 1, -4] and target = 4
Output: 1
Explanation:
The minimum difference is 1. (4 - (2 + 1) = 1).
```

Example 2

```
Input:  nums = [-1, -1, -1, -4] and target = 4
Output: 6
Explanation:
The minimum difference is 6. (4 - (- 1 - 1) = 6).
```

**Challenge**

Do it in `O(nlogn)` time complexity.


**Two Pointers**

```python
class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        # write your code here
        if not nums or len(nums) < 2:
            return 0

        nums.sort()
        diff = sys.maxsize
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                diff = min(diff, abs(nums[left] + nums[right] - target))
                left += 1
            else:
                diff = min(diff, abs(nums[left] + nums[right] - target))
                right -= 1

        return diff
```
