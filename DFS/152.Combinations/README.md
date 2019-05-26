# 152. Combinations

**Description**

Given two integers `n` and `k`. Return all possible combinations of `k` numbers out of `1, 2, ... , n`.

You can return all combinations in any order, but numbers in a combination should be in **ascending order**.


**Example**

Example 1:

```
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
```

Example 2:

```
Input: n = 4, k = 1
Output: [[1],[2],[3],[4]]
```


**Backtracking**

```python
class Solution:
    """
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n
    """
    def combine(self, n, k):
        # write your code here
        if not n or n == 0 or not k or k == 0:
            return [[]]

        self.n = n
        self.k = k
        combinations = []
        self._find_combinations(combinations, [], 1)
        return combinations

    def _find_combinations(self, combinations, tmp, start):
        if len(tmp) == self.k:
            combinations.append(tmp[:])
            return

        for i in range(start, self.n + 1):
            tmp.append(i)
            self._find_combinations(combinations, tmp, i + 1)
            tmp.pop()
```
