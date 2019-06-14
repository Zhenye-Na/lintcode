# 586. Sqrt(x) II

**Description**

Implement `double sqrt(double x)` and `x >= 0`.

Compute and return the square root of `x`.

```
You do not need to care about the accuracy of the result, we will help you to output results.
```

**Example**

Example 1:

```
Input: n = 2 
Output: 1.41421356
```

Example 2:

```
Input: n = 3
Output: 1.73205081
```

**Binary Search**

```python
class Solution:
    """
    @param x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        # write your code here
        if not x:
            return

        left, right = 0, max(1, x)
        while right - left > 1e-10:
            mid = left + (right - left) / 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid
            else:
                right = mid

        return left
```