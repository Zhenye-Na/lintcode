# 79. Longest Common Substring

- **Description**
    - Given two strings, find the **longest common substring**.
    - Return the length of it.
    - The characters in substring should occur continuously in original string. This is different with subsequence.
- **Example**
    - Given `A = "ABCD"`, `B = "CBCE"`, return `2`.
- **Challenge**
    - `O(n x m)` time and memory.


## Solution

### Dynamic Programming

同样推荐 Tushar 的 讲解视频：

- [Longest Common Substring by Tushar](https://www.youtube.com/watch?v=BysNXJHzCEs)


```java
public class Solution {
    /**
     * @param A: A string
     * @param B: A string
     * @return: the length of the longest common substring.
     */
    public int longestCommonSubstring(String A, String B) {
        // write your code here

        if (A == null || B == null || A.length() == 0 || B.length() == 0) {
            return 0;
        }

        int m = A.length();
        int n = B.length();
        int[][] dp = new int[m + 1][n + 1];
        char[] a = A.toCharArray();
        char[] b = B.toCharArray();

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (a[i - 1] == b[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = 0;
                }
            }
        }

        return getMaxLength(dp);
    }

    private int getMaxLength(int[][] dp) {
        int m = dp.length;
        int n = dp[0].length;
        int max = 0;
        for(int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                max = Math.max(max, dp[i][j]);
            }
        }
        return max;
    }

}
```