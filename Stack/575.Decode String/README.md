# 575. Decode String

**Description**

Given an expression `s` contains `numbers`, `letters` and `brackets`. Number represents the number of repetitions inside the brackets (can be a string or another expression). Please expand expression to be a string.

**Example**

Example 1

```
Input: S = abc3[a]
Output: "abcaaa"
```

Example 2

```
Input: S = 3[2[ad]3[pf]]xyz
Output: "adadpfpfpfadadpfpfpfadadpfpfpfxyz"
```

**Challenge**

Can you do it without recursion?


**Stack**

```python
class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        stack = []
        if not s or len(s) == 0:
            return s

        word = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                rep = 0
                while s[i].isdigit():
                    rep = rep * 10 + int(s[i])
                    i += 1
                stack.append(str(rep))

            elif s[i] == "[":
                i += 1
                continue

            elif s[i] == "]":
                while not stack[-1].isdigit():
                    word.append(stack.pop())

                s_prime = ""
                while word:
                    s_prime += word.pop()

                s_prime = int(stack[-1]) * s_prime
                stack.pop()
                stack.append(s_prime)

                i += 1

            else:
                stack.append(s[i])
                i += 1

        return "".join(stack)
```

**DFS**

```python
class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """

    def expressionExpand(self, s):
        # write your code here
        if s is None or len(s) == 0:
            return ""

        return self.dfs(s)

    def dfs(self, s):
        res = ""
        i = 0

        while i < len(s):
            if not s[i].isdigit():
                res += s[i]
                i += 1
                continue
            digit = ""

            while i < len(s) and s[i].isdigit():
                digit += s[i]
                i += 1
            left, right = i, i + 1
            left_p, right_p = 1, 0

            while right < len(s) and left_p != right_p:
                if s[right] == "[":
                    left_p += 1
                if s[right] == "]":
                    right_p += 1
                right += 1

            res += int(digit) * self.dfs(s[left + 1:right - 1])
            i = right

        return res
```
