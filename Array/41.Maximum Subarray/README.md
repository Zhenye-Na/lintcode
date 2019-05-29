# 41. Maximum Subarray

**Description**

Given an array of integers, find a contiguous subarray which has the largest sum.

The subarray should contain at least one number.

**Example**

Example 1:

```
Input: [−2,2,−3,4,−1,2,1,−5,3]
Output: 6
Explanation: the contiguous subarray [4,−1,2,1] has the largest sum = 6.
```

Example 2:

```
Input: [1,2,3,4]
Output: 10
Explanation: the contiguous subarray [1,2,3,4] has the largest sum = 10.
```

**Challenge**

Can you do it in time complexity O(n)?

**Prefix Sum**

```python
class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return None

        min_sum, max_sum = 0, -sys.maxsize
        prefix_sum = 0
        
        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)

        return max_sum
```
