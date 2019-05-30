# 521. Remove Duplicate Numbers in Array

**Description**

Given an array of integers, remove the duplicate numbers in it.

You should:

```
Do it in place in the array.
Move the unique numbers to the front of the array.
Return the total number of the unique numbers.
You don't need to keep the original order of the integers.
```

**Example**

Example 1:

```
Input:
nums = [1,3,1,4,4,2]

Output:
[1,3,4,2,?,?]
4

Explanation:
Move duplicate integers to the tail of nums => nums = [1,3,4,2,?,?].
Return the number of unique integers in nums => 4.
Actually we don't care about what you place in ?, we only care about the part which has no duplicate integers.
```

Example 2:

```
Input:
nums = [1,2,3]

Output:
[1,2,3]
3
```

**Challenge**

- Do it in `O(n)` time complexity.
- Do it in `O(nlogn)` time without extra space.

**Set**

`O(n)`

```python
class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return 0

        # O(n) Time, O(n) Space
        left, right = 0, 0
        hist = set()
        while right < len(nums):
            if nums[right] not in hist:
                hist.add(nums[right])
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
            else:
                # nums[right] in history
                while right < len(nums) and nums[right] in hist:
                    right += 1

        return left

```


**Two Pointers**

`O(nlogn)`

```python
class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return 0

        # O(nlogn) Time, O(1) Space
        nums.sort()
        result = 1
        for i in range(1, len(nums)):
            if nums[i - 1] != nums[i]:
                nums[result] = nums[i]
                result += 1
                
        return result
```
