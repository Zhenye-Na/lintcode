# 1617. Array Maximum Difference

- **Description**
    - Given an array a, output the maximum value of `a[j] - a[i]`, where `i < j`, `a[i]<a[j]`, `a[i]` is an odd number, and `a[j]` is an even number
- **Example**
    - `a = [1,2,3,4]`
    - return `3`


## Solution


```python
import sys

class Solution:
    """
    @param a: the array a
    @return: return the maximum value
    """
    def getAnswer(self, a):
        # Write your code here
        if not a:
            return 0
        length, minimum, max_diff = len(a), sys.maxint, 0
        for i in xrange(length):
            if a[i] % 2 != 0:
                minimum = min(minimum, a[i])
            else:
                max_diff = max(a[i] - minimum, max_diff)
        return max_diff
```