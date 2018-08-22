# 428. Pow(x, n)

- **Description**
    - Implement `pow(x, n)`.
    - You don't need to care about the precision of your answer, it's acceptable if the expected answer and your answer 's difference is smaller than `1e-3`.
- **Example**
    - `Pow(2.1, 3) = 9.261`
    - `Pow(0, 1) = 0`
    - `Pow(1, 0) = 1`
- **Challenge**
    - `O(logn)` time


## Solution

Divide & Conquer

### Python

```python
class Solution:
    """
    @param: x: the base number
    @param: n: the power number
    @return: the result
    """
    def myPow(self, x, n):
        # write your code here
        if (x == 0):
            return 0

        if (n == 0):
            return 1

        if (n == 1):
            return x

        if n < 0:
            x = 1 / x
            n = - n

        tmp = self.myPow(x, n / 2)

        if (n % 2 == 0):
            return tmp * tmp
        else:
            return x * tmp * tmp
```
