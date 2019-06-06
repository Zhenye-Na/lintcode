# 32. Minimum Window Substring

**Description**

Given a string `source` and a string `target`, find the *minimum window* in `source` which will contain *all* the characters in `target`.

```
1. If there is no such window in source that covers all characters in target, return the emtpy string "".
2. If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in source.
3. The target string may contain duplicate characters, the minimum window should cover all characters including the duplicate characters in target.
```


**Clarification**

*Should the characters in minimum window has the same order in target?*

Not necessary.


**Example**

Example 1:

```
Input:
""
""
Output:
""
```

Example 2:

```
Input:
"ADOBECODEBANC"
"ABC"
Output:
"BANC"
```

**Challenge**

Can you do it in time complexity `O(n)` ?

**同向双指针**

- 左指针 `left` 主指针, for loop, 每次移动 1 格
- 右指针 `right` 辅指针, while loop, 每次移动格数未知, 但是不会向左移动

```python
class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source , target):
        # write your code here
        if not source or len(source) == 0:
            return ""

        if not target or len(target) == 0:
            return ""

        countS = [0 for _ in range(256)]
        countT = [0 for _ in range(256)]

        s = [_s for _s in source]
        t = [_t for _t in target]

        k = len(set(list(t)))
        for _t in t:
            countT[ord(_t)] += 1

        c, right = 0, 0
        l, r = -1, -1
        for left in range(len(s)):
            while right < len(s) and c < k:
                countS[ord(s[right])] += 1
                if countS[ord(s[right])] == countT[ord(s[right])]:
                    c += 1

                right += 1

            if c == k:
                if l == -1 or r - l > right - left:
                    l, r = left, right

            countS[ord(s[left])] -= 1
            if countS[ord(s[left])] == countT[ord(s[left])] - 1:
                c -= 1

        return "".join(s[l:r]) if l != -1 else ""
```