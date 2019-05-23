# 1626. Salary Adjustment

**Description**

Given a list of `salaries`, find the smallest `cap` which makes the sum of adjusted salary be equal to or larger than the given `target`. `cap` is defined as: **if the current salary is smaller than `cap`, then `cap` is used as the new salary, otherwise keep the original salary**

```
The length of the list does not exceed 100000100000
The salaries do not exceed 1000010000
```

**Example**

Example 1

```
Give a=[1,2,3,4], target=13,
return `3`.
Input:
1 2 3 4
13
Output:3

Explanation:
If cap=3, the list will change into [3,3,3,4].
```

Example 2

```
Give a=[1,2,3,4], target=16,
return `4`.
Input:
1 2 3 4
16
Output:4

Explanation:
If cap=4, the list will change into [4,4,4,4].
```

**Binary Search**

```python
class Solution:
    """
    @param nums: the list of salary
    @param target: the target of the sum
    @return: the cap it should be
    """
    def getCap(self, nums, target):
        # Write your code here.
        if not nums or len(nums) == 0:
            return -1

        nums.sort()
        lo, hi = 0, target // len(nums)
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if self._sumSalaries(nums, mid) >= target:
                hi = mid
            else:
                lo = mid

        if self._sumSalaries(nums, lo) >= target:
            return lo
        elif self._sumSalaries(nums, hi) >= target:
            return hi
        else:
            return hi + 1

    def _sumSalaries(self, nums, cap):
        total = 0
        for num in nums:
            total += max(cap, num)

        return total
```