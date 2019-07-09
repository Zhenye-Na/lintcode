# 404. Subarray Sum II

**Description**

Given an positive integer array A and an interval. Return the number of subarrays whose sum is in the range of given interval.

Subarray is a part of origin array with continuous index.

**Example**

Example 1:

```
Input: A = [1, 2, 3, 4], start = 1, end = 3
Output: 4
Explanation: All possible subarrays: [1](sum = 1), [1, 2](sum = 3), [2](sum = 2), [3](sum = 3).
```

Example 2:

```
Input: A = [1, 2, 3, 4], start = 1, end = 100
Output: 10
Explanation: Any subarray is ok.
```

```python
class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, A, start, end):
        # write your code here
        if not A or len(A) == 0:
            return 0

        n = len(A)
        l, r = 0, 0
        l_sum, r_sum = 0, 0
        res = 0

        for i in range(len(A)):

            l = max(l, i)
            r = max(r, i)

            while l < n and l_sum + A[l] < start:
                l_sum += A[l]
                l += 1

            while r < n and r_sum + A[r] <= end:
                r_sum += A[r]
                r += 1

            if r - l > 0:
                res += r - l

            if l > i:
                l_sum = l_sum - A[i]

            if r > i:
                r_sum = r_sum - A[i]

        return res
```
