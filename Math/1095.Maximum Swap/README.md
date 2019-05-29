# 1095. Maximum Swap

**Description**

Given a non-negative integer. You could choose to swap two digits of it. Return the maximum valued number you could get.

> The given number is in the range of `[0, 10^8]`


**Example**

Example 1:

```
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
```

Example 2:

```
Input: 9973
Output: 9973
Explanation: No swap.
```



```python
class Solution:
    """
    @param num: a non-negative intege
    @return: the maximum valued number
    """
    def maximumSwap(self, num):
        # Write your code here
        res, num = num, list(str(num))
        for i in range(len(num) - 1):
            for j in range(i + 1, len(num)):
                if int(num[j]) > int(num[i]):
                    # swap
                    tmp = int("".join(num[:i] + [num[j]] + num[i + 1:j] + [num[i]] + num[j + 1:]))
                    res = max(res, tmp)
        return res
```