# 413. Reverse Integer

- **Description**
    - Reverse digits of an integer.
    - Returns `0` when the reversed integer **overflows** (signed 32-bit integer).
    - Given a **32-bit signed integer**, reverse digits of an integer.
- **Example**

    ```c
    Example 1:
    Input: 123
    Output: 321
    
    Example 2:
    Input: -123
    Output: -321
    
    Example 3:
    Input: 120
    Output: 21
    ```

- **Note**
    - Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31 ,  2^31 − 1].
    - For the purpose of this problem, assume that your function returns `0` when the reversed integer overflows.

## Solution

### Stack

- Time `O(n)`
- Space `O(n)`

```python
class Solution:
    """
    @param x: the integer to be reversed
    @return: the reversed integer
    """
    def reverseInteger(self, x):
        # write your code here
        result = 0
        flag = 1 if x > 0 else -1
        x = abs(x)

        stack = []
        while x != 0:
            stack.append(x % 10)
            x /= 10

        while stack:
            result = (result * 10) + stack.pop(0)

        return result * flag if (result * flag) < 2 ** 31 - 1 and (result * flag) > -2 ** 31 else 0

```

### 直接做 + 位运算

- Time `O(n)`
- Space `O(1)`

```python
# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        if n == 0:
            return 0

        neg = 1
        if n < 0:
            neg, n = -1, -n

        reverse = 0
        while n > 0:
            reverse = reverse * 10 + n % 10
            n = n / 10

        reverse = reverse * neg
        if reverse < -(1 << 31) or reverse > (1 << 31) - 1:
            return 0
        return reverse
```
