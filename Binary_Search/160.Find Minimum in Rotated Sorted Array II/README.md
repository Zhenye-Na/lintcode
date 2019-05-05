# 160. Find Minimum in Rotated Sorted Array II

**Description**

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

> The array may contain duplicates.

**Example**

Example 1:

```
Input :[2,1]
Output : 1.
```

Example 2:

```
Input :[4,4,5,6,7,0,1,2]
Output : 0.
```


**Solution**

```
分析

// 这道题目在面试中不会让写完整的程序
// 只需要知道最坏情况下 [1,1,1....,1] 里有一个0
// 这种情况使得时间复杂度必须是 O(n)
// 因此写一个for循环就好了。
// 如果你觉得，不是每个情况都是最坏情况，你想用二分法解决不是最坏情况的情况，那你就写一个二分吧。
// 反正面试考的不是你在这个题上会不会用二分法。这个题的考点是你想不想得到最坏情况。
```

在每次循环中, 让 `nums[start] != nums[end]` 就可以, 原来的模板不用变


```python
class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return None

        start, end = 0, len(nums) - 1

        while start + 1 < end:
            while nums[start] == nums[end]:
                end -= 1
            
            mid = start + (end - start) // 2
            if nums[mid] > nums[end]:
                start = mid
            else:
                end = mid

        if nums[start] < nums[end]:
            return nums[start]
        return nums[end]
```

