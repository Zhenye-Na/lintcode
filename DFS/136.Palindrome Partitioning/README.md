# 136. Palindrome Partitioning

**Description**

Given a string s. Partition s such that every substring in the partition is a palindrome.

Return all possible palindrome partitioning of s.

```
Different partitionings can be in any order.
Each substring must be a continuous segment of s.
```

**Example**

Example 1:

```
Input: "a"
Output: [["a"]]
Explanation: Only 1 char in the string, only 1 way to split it (itself).
```

Example 2:

```
Input: "aab"
Output: [["aa", "b"], ["a", "a", "b"]]
Explanation: There are 2 ways to split "aab".
    1. Split "aab" into "aa" and "b", both palindrome.
    2. Split "aab" into "a", "a", and "b", all palindrome.
```


**分割回文字符串**

- 本题和 `subsets` 以及 `combination sum` 基本类似，只不过不是很明显。字符串每一个字母之间都是可以拆开的候选位置 (高中数学)
- 同时，跟 permutations 不同，不可以选择之前的字母（需要一个 `startIndex`）
- 其他就是套模板即可


```python
class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        # write your code here
        results = []
        if not s or len(s) == 0:
            return results

        self._dfs(s, [], results)
        return results

    def _dfs(self, s, tmp, results):
        if len(s) == 0:
            results.append(tmp[:])
            return

        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                tmp.append(s[:i])
                self._dfs(s[i:], tmp, results)
                tmp.pop()

    def isPalindrome(self, s):
        return s == s[::-1]
```
