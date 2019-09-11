# 89. k Sum

**Description**

Given `n` distinct positive integers, integer `k (k <= n)` and a number target.

Find `k` numbers where sum is `target`. Calculate how many solutions there are?

**Example**

Example 1

```
Input:
List = [1,2,3,4]
k = 2
target = 5
Output: 2
Explanation: 1 + 4 = 2 + 3 = 5
```

Example 2

```
Input:
List = [1,2,3,4,5]
k = 3
target = 6
Output: 1
Explanation: There is only one method. 1 + 2 + 3 = 6
```

**三维数组DP**

```python
class Solution:
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """
    def kSum(self, A, k, target):
        # write your code here
        # state: f[i][j][t] 表示从前 i 个数里面取 j 个, 和能否为 t
        f = [[[0 for _ in range(target + 1)] for _ in range(k + 1)] for _ in range(len(A) + 1)]

        # initialization
        for i in range(len(A) + 1):
            f[i][0][0] = 1

        # function: f[i][j][t]: 是否取第 i 个数, 两种情况
        for i in range(1, len(A) + 1):
            for j in range(1, min(k + 1, i + 1)):
                for t in range(1, target + 1):
                    f[i][j][t] = f[i - 1][j][t]
                    if t - A[i - 1] >= 0:
                        f[i][j][t] += f[i - 1][j - 1][t - A[i - 1]]

        return f[-1][-1][-1]
```