# 91. Minimum Adjustment Cost

**Description**

Given an integer `array`, adjust each integers so that the difference of every adjacent integers are not greater than a given number `target`.

If the array before adjustment is `A`, the array after adjustment is `B`, you should minimize the sum of `|A[i]-B[i]|`

```
You can assume each number in the array is a positive integer and not greater than 100.
```

**Example**

Example 1:

```
Input: [1,4,2,3], target=1
Output: 2
```

Example 2:

```
Input: [3,5,4,7], target=2
Output: 1
```

**Dynamic Programming**


`f[i][k]` 表示第 `i` 个数变成 `k` 时, 前 `i` 个数调整的代价和最小值

枚举第 `i - 1` 个数调整成的数字 `j`, 再枚举第 `i` 个数调整成 `k`


```python
import sys

class Solution:
    """
    @param: A: An integer array
    @param: target: An integer
    @return: An integer
    """
    def MinAdjustmentCost(self, A, target):
        # write your code here
        if not A or len(A) == 0:
            return 0

        n, l = len(A), 100

        # state: f[i][k] 表示 A[i] 调整到 k 时的最小调整代价
        f = [[sys.maxsize for _ in range(l + 1)] for _ in range(n + 1)]

        # initialization
        for col in range(l + 1):
            f[0][col] = 0

        # function
        for i in range(1, n + 1):
            for k in range(1, l + 1):
                if f[i - 1][k] != sys.maxsize:
                    for t in range(l + 1):
                        if abs(k - t) <= target:
                            f[i][t] = min(f[i][t], f[i - 1][k] + abs(A[i - 1] - k))

        # find results
        ans = f[n][l]
        for i in range(l + 1):
            if f[n][i] < ans:
                ans = f[n][i]       

        return ans
```