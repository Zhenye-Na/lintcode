# 108. Palindrome Partitioning II

**Description**

Given a string `s`, cut `s` into some *substrings* such that every *substring* is a palindrome.

Return the *minimum cuts* needed for a palindrome partitioning of `s`.

**Example**

Example 1:

```
Input: "a"
Output: 0
Explanation: "a" is already a palindrome, no need to split.
```

Example 2:

```
Input: "aab"
Output: 1
Explanation: Split "aab" once, into "aa" and "b", both palindrome.
```

**Dynamic Programming**

可以看作序列型动态规划问题, 设定 `dp[i]` 表示原串的前 `i` 个字符最少分割多少次可以使得到的都是回文子串.

如果 `s` 前 `i` 个字符组成的子串本身就是回文串, 则 `dp[i] = 0`, 否则:

```
dp[i] = min{dp[j] + 1} (j < i 并且 s[j + 1], s[j + 2], ... , s[i] 是回文串)
```

如果想要是 $O(n^2)$ 的时间复杂度 (`n` 是 `s` 的长度), 需要事先求出来回文串信息, 在状态转移时可以 $O(1)$ 地知道一段子串是否回文的.



```java
public class Solution {
    /**
     * @param s: A string
     * @return: An integer
     */
    public int minCut(String s) {
        // write your code here
        if (s == null || s.length() == 0) {
            return 0;
        }

        // preparation
        boolean[][] isPalindrome = getIsPalindrome(s);

        // initialize
        int[] f = new int[s.length() + 1];
        for (int i = 0; i <= s.length(); i++) {
            f[i] = i - 1;
        }

        // main
        for (int i = 1; i <= s.length(); i++) {
            for (int j = 0; j < i; j++) {
                if (isPalindrome[j][i - 1]) {
                    f[i] = Math.min(f[i], f[j] + 1);
                }
            }
        }

        return f[s.length()];

    }

    private boolean[][] getIsPalindrome(String s) {
        boolean[][] isPalindrome = new boolean[s.length()][s.length()];

        for (int i = 0; i < s.length(); i++) {
            isPalindrome[i][i] = true;
        }
        for (int i = 0; i < s.length() - 1; i++) {
            isPalindrome[i][i + 1] = (s.charAt(i) == s.charAt(i + 1));
        }

        for (int length = 2; length < s.length(); length++) {
            for (int start = 0; start + length < s.length(); start++) {
                isPalindrome[start][start + length] = isPalindrome[start + 1][start + length - 1]
                        && s.charAt(start) == s.charAt(start + length);
            }
        }

        return isPalindrome;
    }

}
```