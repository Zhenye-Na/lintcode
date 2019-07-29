# 633. Find the Duplicate Number

**Description**

Given an array nums containing `n + 1` integers where each integer is between `1` and `n` (inclusive), gaurentee that at least `one` duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

```
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n^2).
There is only one duplicate number in the array, but it could be repeated more than once.
```

**Example**


Example 1:

```
Input:
[5,5,4,3,2,1]
Output:
5
```

Example 2:

```
Input:
[5,4,4,3,2,1]
Output:
4
```


```python
class Solution:
    """
    @param nums: an array containing n + 1 integers which is between 1 and n
    @return: the duplicate one
    """
    def findDuplicate(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return 0

        lo, hi = 1, len(nums) - 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if self.count(nums, mid) <= mid:
                lo = mid
            else:
                hi = mid

        if self.count(nums, lo) <= lo:
            return hi
        return lo

    def count(self, nums, target):
        cnt = 0
        for num in nums:
            if num <= target:
                cnt += 1
        return cnt
```