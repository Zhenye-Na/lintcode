# 940. Maximum Absolute Value

**Description**

Given an array `A` of integers, select `n` numbers and makes the smallest absolute value of the difference between any two elements to largest. Find the maximum absolute value.

```
the length of array A.length <= 1000
0 <= n <= A.length
0 <= A[i] <= 2^31-1
```

**Example**

Example 1

```
Input: A = [1,2,8,4,9,3],  n = 3
Output: 3
Explanation:
Select either [1,4,8] or [1,4,9].
```

Example 2

```
Input: A = [1,2,3,4,5,6],  n = 2
Output: 5
Explanation:
Select [1,6]
```

**Binary Search**

```python
class Solution:
    """
    @param A: an array
    @param n: an integer
    @return: makes the smallest absolute value of the difference between any two elements to largest
    """
    def maximumAbsolutValue(self, A, n):
        # Write your code here
        if not A or len(A) == 0 or n <= 1 or n > len(A):
            return -1

        A.sort()
        lo, hi = 0, (A[-1] - A[0]) // (n - 1) + 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            if self._compute_N(A, mid) >= n:
                lo = mid
            else:
                hi = mid

        return lo

    def _compute_N(self, A, diff):

        count, val = 1, diff + A[0]
        for a in A[1:]:
            if a >= val:
                count += 1
                val = a + diff

        return count
```