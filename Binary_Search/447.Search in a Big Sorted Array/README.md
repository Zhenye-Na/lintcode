# 447. Search in a Big Sorted Array


**Description**

Given a big sorted array with non-negative integers sorted by non-decreasing order. The array is so big so that you can not get the length of the whole array directly, and you can only access the kth number by `ArrayReader.get(k)` (or `ArrayReader->get(k)` for C++).

Find the first index of a target number. Your algorithm should be in `O(log k)`, where `k` is the first index of the target number.

Return `-1`, if the number doesn't exist in the array.

> If you accessed an inaccessible index (outside of the array), `ArrayReader.get` will return `2,147,483,647`.


**Example**

```
Example 1:

Input: [1, 3, 6, 9, 21, ...], target = 3
Output: 1

Example 2:

Input: [1, 3, 6, 9, 21, ...], target = 4
Output: -1
```

**Challenge**

`O(logn)` time, `n` is the first index of the given target number.




二倍跳跃边界搜索, 二分查找答案

```python
while reader.get(end) < target:
    end *= 2
```

本题是找到第一个出现的位置，所以先查找 `start` 是否返回，再查找 `end` 是否返回



```python
"""
Definition of ArrayReader
class ArrayReader(object):
    def get(self, index):
    	# return the number on given index, 
        # return 2147483647 if the index is invalid.
"""
class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        n = 1
        while reader.get(n) < target:
            n *= 2

        start, end = 0, n
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            if reader.get(mid) == target:
                end = mid
            elif reader.get(mid) > target:
                end = mid
            else:
                start = mid

        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1

```
