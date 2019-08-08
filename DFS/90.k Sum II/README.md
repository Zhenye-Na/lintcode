# 90. k Sum II

**Description**

Given `n` unique postive integers, number `k (1 <= k <= n)` and target.

Find *all possible* `k` integers where their `sum` is target.

**Example**

Example 1:

```
Input: [1,2,3,4], k = 2, target = 5
Output:  [[1,4],[2,3]]
```

Example 2:

```
Input: [1,3,4,6], k = 3, target = 8
Output:  [[1,3,4]]
```

**Backtracking**

```python
class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """

    def kSumII(self, A, k, target):
        # write your code here
        self.result = []
        if not A or len(A) == 0:
            return self.result

        if k > len(A) and sum(A) != target:
            return self.result

        self.dfs(A, k, [], 0, target)
        return self.result

    def dfs(self, A, k, curr, start, target):
        if len(curr) == k and target == 0:
            self.result.append(curr[:])
            return

        for idx in range(start, len(A)):
            if target >= A[idx]:
                curr.append(A[idx])
                self.dfs(A, k, curr, idx + 1, target - A[idx])
                curr.pop()
```