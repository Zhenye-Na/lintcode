# 125. Backpack II

**Description**

There are `n` items and a backpack with size `m`. Given array `A` representing the size of each item and array `V` representing the value of each item.

What's the maximum value can you put into the backpack?

```
A[i], V[i], n, m are all integers.
You can not split an item.
The sum size of the items you want to put into backpack can not exceed m.
Each item can only be picked up once
```

**Example**

Example 1:

```
Input: m = 10, A = [2, 3, 5, 7], V = [1, 5, 2, 4]
Output: 9
Explanation: Put A[1] and A[3] into backpack, getting the maximum value V[1] + V[3] = 9 
```

Example 2:

```
Input: m = 10, A = [2, 3, 8], V = [2, 5, 8]
Output: 10
Explanation: Put A[0] and A[2] into backpack, getting the maximum value V[0] + V[2] = 10 
```

**Challenge**

`O(nm)` memory is acceptable, can you do it in `O(m)` memory? 滚动数组优化


```python
class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        n = len(A)

        # state: f[i][j] 表示前 i 个数, 取出一些, 能够拼成体积为 j 的最大价值
        f = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        # function: f[i][j] = max(f[i - 1][j - A[i - 1]] + V[i - 1], f[i - 1][j])
        # 决策就是第 i 个物品装不装入背包
        for i in range(1, n + 1):
            f[i][0] = 0
            for j in range(1, m + 1):
                if j >= A[i - 1]:
                    f[i][j] = max(f[i - 1][j - A[i - 1]] + V[i - 1], f[i - 1][j])
                else:
                    f[i][j] = f[i - 1][j]

        return max(f[-1])
```