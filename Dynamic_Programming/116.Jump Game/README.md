# 116. Jump Game

**Description**

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

This problem have two method which is `Greedy` and `Dynamic Programming`.

- The time complexity of Greedy method is `O(n)`.
- The time complexity of Dynamic Programming method is `O(n^2)`.

We manually set the small data set to allow you pass the test in both ways. This is just to let you learn how to use this problem in dynamic programming ways. If you finish it in dynamic programming ways, you can try greedy method to make it accept again.

**Example**

```
A = [2,3,1,1,4], return true.
```

```
A = [3,2,1,0,4], return false.
```

```python
class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """

    def canJump(self, A):
        # write your code here
        # initialization: we can jump to the first position
        # dp[i] represents whether we can jump to the i-th position
        dp = [False for _ in range(len(A))]
        dp[0] = True

        # Sequence DP
        # function: f[i] <- f[j] j < i, dp[j] == True, j + A[j] >= i
        for i in range(1, len(A)):
            for j in range(0, i):
                if dp[j] and j + A[j] >= i:
                    dp[i] = True
                    break  # no longer need to change value of dp[i], break

        # answer: dp[-1]
        return dp[-1]
```