# 117. Jump Game II

Description
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example
Given array `A = [2,3,1,1,4]`

The minimum number of jumps to reach the last index is `2`. (Jump 1 step from index `0` to `1`, then `3` steps to the last index.)


## Solution

### Dynamic Programming

O(n^2) Time
O(n) Space

会超时...

```python
class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        # write your code here
        jumps = [len(A)] * len(A)
        jumps[0] = 0

        for i in range(1, len(A)):
            for j in range(i):
                if A[j] + j >= i:
                    jumps[i] = min(jumps[i], jumps[j] + 1)

        return jumps[-1]
```

### Greedy Algorithm

O(n) Time
O(1) Space

```java
public class Solution {
    /**
     * @param A: A list of integers
     * @return: An integer
     */
    public int jump(int[] A) {
        // write your code here
        if (A == null || A.length == 0) {
            return -1;
        }

        int jumps = 0, curMax = 0, glbMax = 0;
        for (int i = 0; i < A.length - 1; i++) {
            glbMax = Math.max(glbMax, i + A[i]);
            if (i == curMax) {
                jumps++;
                curMax = glbMax;
            }
        }
        return jumps;
    }
}
```

## Follow up

Could you find the path which has minimum jumps reaching the end?

```python
class Solution:
    """
    @param A: A list of integers
    @return: An integer
    """
    def jump(self, A):
        # write your code here
        jumps = [len(A)] * len(A)
        jumps[0] = 0

        ancestor = [len(A)] * len(A)

        for i in range(1, len(A)):
            for j in range(i):
                if A[j] + j >= i:
                    jumps[i] = min(jumps[i], jumps[j] + 1)
                    ancestor[i] = j

        path = []
        idx = len(A) - 1
        path.insert(0, idx)
        while idx >= 0:
            path.insert(0, ancestor[-1])
            idx = ancestor[-1]

        print(path)
        return jumps[-1]
```
