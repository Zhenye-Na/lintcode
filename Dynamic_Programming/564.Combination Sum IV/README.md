# 564. Combination Sum IV (Backpack VI)

**Description**

Given an integer array nums with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

```
A number in the array can be used multiple times in the combination.
Different orders are counted as different combinations.
```

**Example**

Example 1

```
Input: nums = [1, 2, 4], and target = 4
Output: 6
Explanation:
The possible combination ways are:
[1, 1, 1, 1]
[1, 1, 2]
[1, 2, 1]
[2, 1, 1]
[2, 2]
[4]
```

Example 2

```
Input: nums = [1, 2], and target = 4
Output: 5
Explanation:
The possible combination ways are:
[1, 1, 1, 1]
[1, 1, 2]
[1, 2, 1]
[2, 1, 1]
[2, 2]
```



**Backtracking**

巨慢无比 ...

```python
class Solution:
    """
    @param nums: an integer array and all positive numbers, no duplicates
    @param target: An integer
    @return: An integer
    """
    def backPackVI(self, nums, target):
        # write your code here
        if not nums or len(nums) == 0 or target <= 0:
            return 0

        nums.sort()
        self.combinations = []
        self.target = target

        self._find_combination_sum(nums, 0, [])
        return len(self.combinations)

    def _find_combination_sum(self, nums, start, tmp):
        if sum(tmp) == self.target:
            if tmp not in self.combinations:
                self.combinations.append(tmp[:])
            return

        for i in range(start, len(nums)):
            
            if sum(tmp) + nums[i] > self.target:
                break
            
            tmp.append(nums[i])
            self._find_combination_sum(nums, 0, tmp)
            tmp.pop()
```
