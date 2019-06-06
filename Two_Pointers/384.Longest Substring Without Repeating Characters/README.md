# 384. Longest Substring Without Repeating Characters

**Description**

Given a `string`, find the length of the longest substring without repeating characters.

**Example**

Example 1:

```
Input: "abcabcbb"
Output: 3
Explanation: The longest substring is "abc".
```

Example 2:

```
Input: "bbbbb"
Output: 1
Explanation: The longest substring is "b".
```

**Challenge**

time complexity `O(n)`


**同向双指针**

模板题, 用 set 来去重

```python
class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        unique_chars = set([])
        j = 0
        n = len(s)
        longest = 0

        for i in range(n):
            while j < n and s[j] not in unique_chars:
                unique_chars.add(s[j])
                j += 1
            longest = max(longest, j - i)
            unique_chars.remove(s[i])

        return longest
```


```python
class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        if not s or len(s) == 0:
            return 0

        char = [ch for ch in s]
        visited = [0 for _ in range(256)]
        visited[ord(s[0])] = 1
        max_string, current = [], [char[0]]
        right = 1

        for left in range(len(char)):
            while right < len(char) and self._isUnique(visited, char[right]):
                current.append(char[right])
                visited[ord(char[right])] = 1
                right += 1

            if len(current) > len(max_string):
                max_string = current[:]

            visited[ord(current[0])] = 0
            current = current[1:]

        return len(max_string)


    def _isUnique(self, visited, target_str):
        return visited[ord(target_str)] == 0
```
