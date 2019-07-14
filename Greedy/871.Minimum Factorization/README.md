# 871. Minimum Factorization

**Description**

Given a positive integer a, find the smallest positive integer b whose multiplication of each digit equals to a.

If there is no answer or the answer is not fit in 32-bit signed integer, then return 0.

**Example**

Example 1:

```
Input: 48
Output: 68
```

Example 2:

```
Input: 15
Output: 35
```

```python
class Solution:
    """
    @param a: a positive integer
    @return: the smallest positive integer whose multiplication of each digit equals to a
    """

    def smallestFactorization(self, a):
        # Write your code here
        res = ''
        for i in range(9, 1, -1):
            while a % i == 0:
                res = str(i) + res
                a //= i

        if a != 1:
            return 0

        res = int(res)

        if res > 0x7fffffff:
            return 0
        else:
            return res

```