# 459. Closest Number in Sorted Array

**Description**

Given a target number and an integer array `A` sorted in ascending order, find the index `i` in `A` such that `A[i]` is closest to the given target.

Return `-1` if there is no element in the array.

There can be duplicate elements in the array, and we can return any of the indices with same value.

**Example**

Example 1:

```
Input: [1, 2, 3] , target = 2
Output: 1.
```

Example 2:

```
Input: [1, 4, 6], target = 3
Output: 1.
```

Example 3:

```
Input: [1, 4, 6], target = 5,
Output: 1 or 2.
```

**Challenge**

`O(logn)` time complexity.


**Binary Search**


```python
class Solution:
    """
    @param A: an integer array sorted in ascending order
    @param target: An integer
    @return: an integer
    """
    def closestNumber(self, A, target):
        # write your code here
        if not A or len(A) == 0:
            return -1

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2

            if A[mid] == target:
                end = mid
            elif A[mid] > target:
                end = mid
            else:
                start = mid

        if A[start] == target:
            return start
        if A[end] == target:
            return end

        if abs(A[start] - target) < abs(A[end] - target):
            return start
        else:
            return end
```
