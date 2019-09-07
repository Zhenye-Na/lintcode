# 1259. Integer Replacement

**Description**

Given a positive integer `n` and you can do operations as follow:


1. If `n` is `even`, replace `n` with `n/2`.
2. If `n` is `odd`, you can replace `n` with either `n + 1` or `n - 1`.

What is the *minimum number of replacements* needed for `n` to become `1`?

**Example**

Example 1:

```
Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1
```

Example 2:

```
Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1
```

**BFS**

```python
from collections import deque


class Solution:
    """
    @param n: a positive integer 
    @return: the minimum number of replacements
    """

    def integerReplacement(self, n):
        # Write your code here
        steps = 0
        if n == 1:
            return steps

        queue = deque([n])
        while queue:
            size = len(queue)
            print(queue, steps)
            for _ in range(size):
                num = queue.popleft()
                if num == 1:
                    return steps
                if num % 2 == 0:
                    queue.append(num // 2)
                else:
                    queue.append(num + 1)
                    queue.append(num - 1)
            steps += 1

        return 0

```


**Dynamic Programming**

*Memoization DFS*

```python
class Solution:
    """
    @param n: a positive integer 
    @return: the minimum number of replacements
    """

    def integerReplacement(self, n):
        # Write your code here
        ans = {}
        return self.dfs(ans, n)

    def dfs(self, ans, n):
        if n == 1:
            return 0

        if n in ans:
            return ans[n]

        if n % 2 == 0:
            ans[n] = self.dfs(ans, n // 2) + 1
        else:
            ans[n] = min(self.dfs(ans, n + 1), self.dfs(ans, n - 1)) + 1

        return ans[n]
```
