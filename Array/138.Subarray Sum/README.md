# 138. Subarray Sum

**Description**

Given an integer array, find a subarray where the sum of numbers is `zero`. Your code should return `the index of the first number` and `the index of the last number`.

There is at least one subarray that it's sum equals to `zero`.


Example

```
Example 1:
	Input:  [-3, 1, 2, -3, 4]
	Output: [0, 2] or [1, 3].
	
	Explanation:
	return anyone that the sum is 0.

Example 2:
	Input:  [-3, 1, -4, 2, -3, 4]
	Output: [1,5]
```

**Prefix Sum**

算出前缀和, 然后在 hashmap 里面之前有过这个和, 那么就找到了和为 0 的 subarray

```python
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        prefix_sum = {0: -1}
        total = 0
        for i, num in enumerate(nums):
            total += num
            if total in prefix_sum:
                return prefix_sum[total] + 1, i
            prefix_sum[total] = i
            
        return -1, -1
```