# 824. Single Number IV

**Description**

Give an array, all the numbers appear twice except one number which appears once and all the numbers which appear twice are next to each other. Find the number which appears once.

```
1 <= nums.length < 10^4
In order to limit the time complexity of the program, your program will run 10^5 times.
```

**Example**

Example 1:

```
Input: [3,3,2,2,4,5,5]
Output: 4
Explanation: 4 appears only once.
```

Example 2:

```
Input: [2,1,1,3,3]
Output: 2
Explanation: 2 appears only once.
```

**Binary Search**

> 当然 XOR 一样可以做 O(n)

Single Number I 需要排序, 但是这道题不需要: 根据奇偶性找到答案, 跟排不排序无关

- 时间复杂度 O(logn)

```python
class Solution:
    """
    @param nums: The number array
    @return: Return the single number
    """
    def getSingleNumber(self, nums):
        # Write your code here
        if not nums or len(nums) == 0:
            return -1

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if mid % 2 == 0:
                if nums[mid] != nums[mid + 1]:
                    right = mid
                else:
                    left = mid
            else:
                if mid >= 1 and nums[mid] != nums[mid - 1]:
                    right = mid
                else:
                    left = mid

        return nums[left] if left % 2 == 0 else nums[right]
```