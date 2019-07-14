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

**DFS with Backtracking 1**

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


**DFS with Backtracking 2**

当 DFS 至 `num=1` 时，将当前的 `list` 存入答案。

```python
class Solution:
    """
    @param n: a integer
    @return: return a 2D array
    """

    def getFactors(self, n):
        # write your code here
        self.combinations = []
        if not n or n < 0:
            return []

        self.dfs(2, [], n)
        return self.combinations

    def dfs(self, start, current, target):
        if target <= 1 and len(current) > 1:
            self.combinations.append(current[:])
            return

        for factor in range(start, int(math.sqrt(target) + 1)):
            if target % factor != 0:
                continue

            current.append(factor)
            self.dfs(factor, current, target // factor)
            current.pop()

        if target >= start:
            current.append(target)
            self.dfs(target, current, 1)
            current.pop()

```