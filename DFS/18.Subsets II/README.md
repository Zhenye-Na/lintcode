# 18. Subsets II

**Description**

Given a collection of integers that might contain duplicates, `nums`, return all possible subsets (the power set).

```
1. Each element in a subset must be in non-descending order.  
2. The ordering between two subsets is free.  
3. The solution set must not contain duplicate subsets.
```

**Example**

Example 1:

```
Input: [0]
Output:
[
  [],
  [0]
]
```

Example 2:

```
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```

**Challenge**

Can you do it in both recursively and iteratively?


```python
class Solution:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return [[]]
        subsets = []
        nums.sort()
        self._find_subsets(nums, subsets, [], 0)
        return subsets

    def _find_subsets(self, nums, subsets, subset, start):
        subsets.append(subset[:])

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue

            subset.append(nums[i])
            self._find_subsets(nums, subsets, subset, i + 1)
            subset.pop()
```
