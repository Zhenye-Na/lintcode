#842. Origami

**Description**

Origami, each time the paper is folded from right to left, the dent is `0`, the bump is `1`. After the `n` times of folds, find the `01` sequence of the creases formed with the paper unrolling.

- `1 <= n <= 20`

Example

Example 1:

```
Input: 1
Output: "0"
```

Example 2:

```
Input: 2
Output: "001"
```

本题考查寻找规律的能力, 通过折纸可以发现如下规律.

第 `1` 次折纸的折痕为 `"0"`.

设第 `i - 1 `次折纸的折痕为 `s`, 则第 `i` 次折纸的折痕为 `s + "0" + s.reverse().flip()`

其中 `reverse` 代表字符串前后反转, `flip` 代表字符串内 `01` 互换

```python
class Solution:
    """
    @param n: The folding times
    @return: the 01 string
    """
    def getString(self, n):
        # Write your code here
        ans = "0"
        for i in range(2, n + 1):
            length = len(ans)
            ans += "0"

            for j in range(length - 1, -1, -1):
                ans += "0" if ans[j] == "1" else "1"

        return ans
```