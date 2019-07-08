# 58. 4Sum

**Description**

Given an array `S` of n integers, are there elements `a`, `b`, `c`, and `d` in `S` such that `a + b + c + d = target`?

Find all *unique* quadruplets in the array which gives the sum of target.

```
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a <= b <= c <= d)
The solution set must not contain duplicate quadruplets.
```

**Example**

Example 1:

```
Input:[2,7,11,15],3
Output:[]
```

Example 2:

```
Input:[1,0,-1,0,-2,2],0
Output:
[[-1, 0, 0, 1]
,[-2, -1, 1, 2]
,[-2, 0, 0, 2]]
```

固定两个端点, 套用 Two Sum

```python
from collections import defaultdict

class Solution:
    """
    @param nums: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, nums, target):
        # write your code here
        quadruplets = []
        nums.sort()
        quadruplets = []
        length = len(nums)

        for i in range(0, length - 3):
            if i and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, length - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue

                total = target - nums[i] - nums[j]
                left, right = j + 1, length - 1
                while left < right:
                    if nums[left] + nums[right] == total:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] > total:
                        right -= 1
                    else:
                        left += 1

        return quadruplets
```
