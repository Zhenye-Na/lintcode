# 402. Continuous Subarray Sum

**Description**

Given an integer array, find a *continuous subarray* where the sum of numbers is the biggest. Your code should return the index of the *first number* and the index of the *last number*. (If their are duplicate answer, return the minimum one in lexicographical order)

**Example**

Example 1:

```
Input: [-3, 1, 3, -3, 4]
Output: [1, 4]
```

Example 2:

```
Input: [0, 1, 0, 1]
Output: [0, 3]
Explanation: The minimum one in lexicographical order.
```

```python
class Solution:
    """
    @param: nums: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySum(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return [0, 0]

        prefix_sum, min_sum, max_sum = 0, 0, -sys.maxsize
        i, j, min_idx = -1, -1, -1
        for idx, num in enumerate(nums):
            prefix_sum += num
            if prefix_sum - min_sum > max_sum:
                max_sum = prefix_sum - min_sum
                i, j = min_idx + 1, idx
            if prefix_sum < min_sum:
                min_sum = prefix_sum
                min_idx = idx

        return [i, j]

```