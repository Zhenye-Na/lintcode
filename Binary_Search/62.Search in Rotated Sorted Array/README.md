# 62. Search in Rotated Sorted Array

**Description**

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., `0 1 2 4 5 6 7` might become `4 5 6 7 0 1 2`).

You are given a target value to search. If found in the array **return its index**, otherwise return `-1`.

> You may assume no duplicate exists in the array.


**Example**

Example 1:

```
Input: [4, 5, 1, 2, 3] and target=1, 
Output: 2.
```

Example 2:

```
Input: [4, 5, 1, 2, 3] and target=0, 
Output: -1.
```

**Challenge**

`O(logN)` time



One pass binary search, use `target` and `A[start]` as "baseline" to compare

```python
class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if not A or len(A) == 0 or not target:
            return -1

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] >= A[start]:
                if A[start] <= target <= A[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if A[mid] <= target <= A[end]:
                    start = mid
                else:
                    end = mid

        if target == A[start]:
            return start
        if target == A[end]:
            return end
        return -1

```


This problem could also be solved using two pass binary search

- first, find the minimum of the rotated sorted array
- second, according to the position (left / right) of `target`, binary search again


```python
class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        if not A:
            return -1
            
        index = self._find_min_index(A)
        if A[index] <= target <= A[-1]:
            return self._binary_search(A, index, len(A) - 1, target)
        return self._binary_search(A, 0, index - 1, target)
        
    def _find_min_index(self, A):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < A[end]:
                end = mid
            else:
                start = mid
        
        if A[start] < A[end]:
            return start
        return end

    def _binary_search(self, A, start, end, target):
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1
```
