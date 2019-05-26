# 652. Factorization

**Description**

A non-negative numbers can be regarded as product of its factors.

Write a function that takes an integer n and return all possible combinations of its factors.

```
Elements in a combination (a1, a2, ... , ak) must be in non-descending order. (ie, a1 <= a2 <= ... <= ak).
The solution set must not contain duplicate combination.
```

**Example**

Example 1

```
Input: 8
Output: [[2,2,2],[2,4]]
Explanation:
8 = 2 x 2 x 2 = 2 x 4
```

Example 2

```
Input: 1
Output: []
```

**DFS with Backtracking**

```python
class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """
    def getFactors(self, n):
        # write your code here
        self.results = []
        if not n or n <= 1:
            return self.results

        self._find_factors(n, 2, [])
        return self.results

    def _find_factors(self, n, start, factor):
        if factor:
            factor.append(n)
            self.results.append(factor[:])
            factor.pop()

        for i in range(start, int(math.sqrt(n) + 1)):
            if n % i != 0:
                continue

            factor.append(i)
            self._find_factors(n // i, i, factor)
            factor.pop()
```