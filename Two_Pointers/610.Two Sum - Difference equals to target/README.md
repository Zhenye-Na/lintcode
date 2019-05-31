# 610. Two Sum - Difference equals to target

**Description**

Given an array of integers, find two numbers that their difference equals to a target value.
where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are NOT zero-based.

```
It's guaranteed there is only one available solution
```

**Example**

Example 1:

```
Input: nums = [2, 7, 15, 24], target = 5 
Output: [1, 2] 
Explanation:
(7 - 2 = 5)
```

Example 2:

```
Input: nums = [1, 1], target = 0
Output: [1, 2] 
Explanation:
(1 - 1 = 0)
```

**同向双指针**

```python
class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum7(self, nums, target):
        # write your code here
        nums = [(num, i) for i, num in enumerate(nums)]
        target = abs(target)    
        n, indexs = len(nums), []

        nums = sorted(nums, key=lambda x: x[0])

        j = 0
        for i in range(n):
            if i == j:
                j += 1
            while j < n and nums[j][0] - nums[i][0] < target:
                j += 1
            if j < n and nums[j][0] - nums[i][0] == target:
                indexs = [nums[i][1] + 1, nums[j][1] + 1]
                return sorted(indexs)

        return [-1, -1]
```