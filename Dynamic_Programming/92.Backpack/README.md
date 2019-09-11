# 92. Backpack

**Description**

Given `n` items with size `A[i]`, an integer `m` denotes the size of a backpack. How full you can fill this backpack?

You can not divide any item into small pieces.

**Example**

Example 1:

```
Input:  [3,4,8,5], backpack size=10
Output:  9
```

Example 2:

```
Input:  [2,3,5,7], backpack size=12
Output:  12
```

**Challenge**

- `O(n x m)` time and `O(m)` memory.
- `O(n x m)` memory is also acceptable if you do not know how to optimize memory.

**背包问题**

将背包装到体积最大且不超过 `m`

- 求 max, 也不能排序打乱 -> 动态规划

`f[i][j]` 从前 `i` 个数取出若干个, 拼成总和为 `j`

背包问题都牵扯到第 `i` 个数, 是否要取?

- 取的话, 要满足什么条件
- 不取, 要满足什么条件

数组中有一维被"和/sum"限制住, 即第二维

```python
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # write your code here
        # state: f[i][j] 从前 i 个取出若干个, 拼成总和为 j
        f = [[False for _ in range(m + 1)] for _ in range(len(A) + 1)]

        # initialization
        f[0][0] = True

        # function: f[i][j]: f[i- 1][j] or f[i][j - A[i]]
        # 取第 i 个数, 那么前 i - 1 个数就要能够拼成 j - A[i]
        # 不取第 i 个数, 那么前 i 个数 已经能够拼成 j

        for i in range(1, len(A) + 1):
            f[i][0] = True
            for j in range(1, m + 1):
                if j - A[i - 1] >= 0:
                    f[i][j] = f[i - 1][j - A[i - 1]] or f[i - 1][j]
                else:
                    f[i][j] = f[i - 1][j]

        for idx in range(m, -1, -1):
            if f[-1][idx]:
                return idx
        return 0
```