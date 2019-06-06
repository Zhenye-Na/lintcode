# 406. Minimum Size Subarray Sum406. Minimum Size Subarray Sum

**Description**

Given an array of `n` positive integers and a positive integer `s`, find the minimal length of a subarray of which the `sum >= s`. If there isn't one, return `-1` instead.

**Example**

Example 1:

```
Input: [2,3,1,2,4,3], s = 7
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
```

Example 2:

```
Input: [1, 2, 3, 4, 5], s = 100
Output: -1
```

**Challenge**

If you have figured out the `O(nlog n)` solution, try coding another solution of which the time complexity is `O(n)`.

**同向双指针**



```python
class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):
        # write your code here
        length = sys.maxsize
        total, right = 0, 0

        for left in range(len(nums)):
            while right < len(nums) and total < s:
                total += nums[right]
                right += 1

            if total >= s:
                length = min(length, right - left)

            total -= nums[left]

        return -1 if length == sys.maxsize else length
```

枚举右端点，左端点不回头

```python
# 模版 2: 枚举右端点，左端点不回头
class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """                
    def minimumSize(self, nums, s):

        ans = sys.maxsize 
        left = 0 
        addup = 0 
        
        for right in range(len(nums)):
            
            addup += nums[right]
            while addup >= s:
                
                ans = min(ans, right - left + 1)
                addup -= nums[left]
                left += 1 

        return ans if ans != sys.maxsize else -1
```