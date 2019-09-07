# 117. Jump Game II

**Description**

Given an array of *non-negative* integers, you are initially positioned at the `first` index of the array.

Each element in the array represents your *maximum* jump length at that position.

Your goal is to reach the `last` index in the minimum number of jumps.

**Example**

Given array `A = [2,3,1,1,4]`

The minimum number of jumps to reach the last index is `2`. (Jump `1` step from index `0` to `1`, then 3 steps to the last index.)


**Dynamic Programming (TLE)**

```python
class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """

    def jump(self, A):
        # write your code here
        # initialization: f[i] represents the min steps to reach i-th index
        f = [sys.maxsize for _ in range(len(A))]
        f[0] = 0

        # function f[i] = min(f[j] + 1) for j in [0, i), if constraints
        for i in range(1, len(A)):
            for j in range(0, i):
                if f[j] != sys.maxsize and j + A[j] >= i:
                    f[i] = min(f[i], f[j] + 1)

        # answer: f[-1] if we can jump to the last index else 0
        return f[-1] if f[-1] != sys.maxsize else 0

```

**Greedy**

```
这题是之前那道Jump Game 跳跃游戏 的延伸，那题是问能不能到达最后一个数字，而此题只让我们求到达最后一个位置的最少跳跃数，貌似是
默认一定能到达最后位置的? 此题的核心方法是利用贪婪算法Greedy的思想来解，想想为什么呢？ 为了较快的跳到末尾，我们想知道每一步能
跳的范围，这里贪婪并不是要在能跳的范围中选跳力最远的那个位置，因为这样选下来不一定是最优解，这么一说感觉又有点不像贪婪算法了。
我们这里贪的是一个能到达的最远范围，我们遍历当前跳跃能到的所有位置，然后根据该位置上的跳力来预测下一步能跳到的最远距离，贪出一
个最远的范围，一旦当这个范围到达末尾时，当前所用的步数一定是最小步数。
```

- C++

```cpp
// Author: Huahua, running time: 12 ms / 10.3 MB
class Solution {
public:
  int jump(vector<int>& nums) {
    int steps = 0;
    int near = 0;
    int far = 0;
    for (int i = 0; i < nums.size(); ++i) {
      if (i > near) {
        ++steps;
        near = far;
      }
      far = max(far, i + nums[i]);      
    }
    return steps;
  }
};
```

- Java

```java
// version 2: Greedy
public class Solution {
    public int jump(int[] A) {
        if (A == null || A.length == 0) {
            return -1;
        }

        int start = 0, end = 0, jumps = 0;
        while (end < A.length - 1) {
            jumps++;
            int farthest = end;
            for (int i = start; i <= end; i++) {
                if (A[i] + i > farthest) {
                    farthest = A[i] + i;
                }
            }
            start = end + 1;
            end = farthest;
        }

        return jumps;
    }
}
```


## References

- [花花酱 LeetCode 45. Jump Game II](https://zxi.mytechroad.com/blog/greedy/leetcode-45-jump-game-ii/)
- [[LeetCode] Jump Game II 跳跃游戏之二](https://www.cnblogs.com/grandyang/p/4373533.html)
