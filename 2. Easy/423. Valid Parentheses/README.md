# 423. Valid Parentheses

- **Description**
    - Given a string containing just the characters `'('`, `')'`, `'{'`, `'}'`, `'['` and `']'`, determine if the input string is valid.
- **Example**
    - The brackets **must close** in the correct order, `"()"` and `"()[]{}"` are all valid but `"(]"` and `"([)]"` are not.
- **Challenge**
    - `O(n)`的时间，n为括号的个数


## Solution

用到 `Stack` 这个数据结构 `FILO`，如果传进来的是 `")}]"` 的任何一个，和栈顶元素进行比较后，如果括号匹配上了，就 `pop` 掉所有的元素，如果匹配不上或者 `Stack` 空了，就返回 false

### Python

```python
class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        if s is None or len(s) == 0:
            return True
        if len(s) % 2 != 0:
            return False

        stack = []
        for symbol in s:
            if symbol == '(' or symbol == '[' or symbol == '{':
                stack.append(symbol)
            else:
                if not stack:
                    return False

                if (symbol == ')' and stack[-1] != '(') or (symbol == '}' and stack[-1] != '{') or (symbol == ']' and stack[-1] != '['):
                    return False

                stack.pop()

        return not stack
```
