# 101. Remove Duplicates from Sorted Array II

**Description**

Given a sorted array, remove the duplicates in place such that each element appear at most **twice** and return the new length.

If a number appears more than two times, then keep the number appears twice in array after remove.

> Need to operate in the original array


**Example**

Example 1:

```
Input: []
Output: 0
```

Example 2:

```
Input:  [1,1,1,2,2,3]
Output: 5

Explanation: 
the length is 5: [1,1,2,2,3]
```


从重复的第三个开始删除即可


```python
class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return 0

        j = 0
        counter = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
                counter = 1
            else:
                # nums[i] == nums[j]
                if counter < 2:
                    j += 1
                    nums[j] = nums[i]
                    counter += 1
        return j + 1

```

或者, 把 `left - 1` 换成 `left - 2` 即可

```python
class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        left, right = 2, 2
        
        while right < len(nums):
            while right < len(nums) and nums[right] == nums[left - 2]:
                right += 1
            if right < len(nums):
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
                
        return left
```