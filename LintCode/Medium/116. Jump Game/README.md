# 116. Jump Game

- **Description**
    - Given an array of non-negative integers, you are initially positioned at the first index of the array.
    - Each element in the array represents your maximum jump length at that position.
    - Determine if you are able to reach the last index.
- **Example**
    - `A = [2,3,1,1,4]`, return `true`.
    - `A = [3,2,1,0,4]`, return `false`.
- **Clarifications**
    - This problem have two method which is `Greedy` and `Dynamic Programming`.
    - The time complexity of `Greedy` method is O(n).
    - The time complexity of `Dynamic Programming` method is O(n^2).
    - We manually set the small data set to allow you pass the test in both ways. This is just to let you learn how to use this problem in dynamic programming ways. If you finish it in dynamic programming ways, you can try greedy method to make it accept again.

## Solution

- The time complexity of `Greedy` method is `O(n)`.
- The time complexity of `Dynamic Programming` method is `O(n^2)`.

### Dynamic Programming

```python
class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        dp = [False] * (len(A))
        dp[0] = True

        for i in range(1, len(A)):
            dp[i] = False

            for j in range(i):
                if (dp[j] == True and j + A[j] >= i):
                    dp[i] = True
                    break

        return dp[-1]

```

```java
/**
 *  Dynamic Prgramming
 *  Time Complexity: O(n^2)
 */

public class Solution {
    /**
     * @param A: A list of integers
     * @return: A boolean
     */
    public boolean canJump(int[] A) {
        // write your code here

        int n = A.length;
        boolean[] f = new boolean[n];

        f[0] = true;

        for (int j = 1; j < n; j++) {

            // Initialization
            f[j] = false;

            for (int i = 0; i < n; i++) {

                if (f[i] && i + A[i] >= j) {
                    f[j] = true;
                    break;
                }

            }

        }

        return f[n - 1];
    }
}
```

### Greedy Algorithm

注意题目中 `A[i]` 表示的是在位置 `i`，"最大"的跳跃距离，而并不是指在位置 `i` 只能跳 `A[i]` 的距离。所以当跳到位置 `i` 后，能达到的最大的距离至少是 `i + A[i]`。

用greedy来解，记录一个当前能达到的最远距离 `maxIndex`：

- 能跳到位置`i`的条件：`i <= maxIndex`。  
- 一旦跳到 `i`，则 `maxIndex = max(maxIndex, i+A[i])`。  
- 能跳到最后一个位置 `n-1` 的条件是：`maxIndex >= n-1`

```java
/**
 *  Greedy Algorithm
 *  Time Complexity: O(n)
 */


 public class Solution {
     /**
      * @param A: A list of integers
      * @return: A boolean
      */
     public boolean canJump(int[] A) {
         // write your code here
         int maxStep = 0, length = A.length;
         for (int index = 0; index < length; index++) {
             // Current position in beyond the maxStep, we cannot reach this position from previous jump
             if (index > maxStep) return false;
             // Update maxStep, select maximum of current index plus the jump step at position index and previous maxStep
             maxStep = Math.max(maxStep, index + A[index]);
         }
         return true;
     }
 }
```
