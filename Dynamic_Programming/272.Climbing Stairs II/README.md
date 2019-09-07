# 272. Climbing Stairs II

**Description**

A child is running up a staircase with `n` steps, and can hop either `1` step, `2` steps, or `3` steps at a time. Implement a method to count how many possible ways the child can run up the stairs.


**Clarification**

For `n=0`, we think the answer is `1`.

**Example**

Example 1:

```
Input: 3
Output: 4
Explanation: 1 + 1 + 1 = 2 + 1 = 1 + 2 = 3 = 3 , there are 4 ways.
```

Example 2:

```
Input: 4
Output: 7
Explanation: 1 + 1 + 1 + 1 = 1 + 1 + 2 = 1 + 2 + 1 = 2 + 1 + 1 = 2 + 2 = 1 + 3 = 3 + 1 = 4 , there are 7 ways.
```


**DP**

```python
class Solution:
    """
    @param n: An integer
    @return: An Integer
    """

    def climbStairs2(self, n):
        # write your code here
        # initialization:
        if n == 0 or n == 1:
            return 1

        if n == 2:
            return 2

        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2

        # state: dp[i] represents how many steps can reach step i
        # function: dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]
```

**Backpack**

```python
class Solution:

    def climbStairs2(self, num_of_stairs):

        different_steps_could_be_taken = [1, 2, 3]

        num_of_ways = [1] + [0 for _ in range(num_of_stairs)]
        for stairs_to_climb in range(1, len(num_of_ways)):
            for steps in different_steps_could_be_taken:
                if stairs_to_climb < steps:
                    continue
                num_of_ways[stairs_to_climb] += num_of_ways[stairs_to_climb - steps]

        return num_of_ways[-1]
```
