# 84. Single Number III
Description
Given 2*n + 2 numbers, every numbers occurs twice except two, find them.

Have you met this question in a real interview?  
Example
Given [1,2,2,3,4,4,5,3] return 1 and 5

Challenge
O(n) time, O(1) extra space.

## Solution

[leetcode 算法解析（一）：260. Single Number III](https://segmentfault.com/a/1190000004886431)

注意 Note 中的第一个条件：**`The order of the result is not important.`**，这个条件非常重要，这关系到算法的正确性。

然后给出整个算法的具体思路，假设数组中两个不同的数字为 A 和 B；

1. 通过遍历整个数组并求整个数组所有数字之间的 XOR，根据 XOR 的特性可以得到最终的结果为 AXORB = A XOR B；
2. 通过某种特定的方式，我们可以通过 AXORB 得到在数字 A 和数字 B 的二进制下某一位不相同的位；因为A 和 B 是不相同的，所以他们的二进制数字有且至少有一位是不相同的。我们将这一位设置为 1，并将所有的其他位设置为 0，我们假设我们得到的这个数字为 bitFlag；
3. 那么现在，我们很容易知道，数字 A 和 数字 B 中必然有一个数字与上 bitFlag 为 0；因为bitFlag 标志了数字 A 和数字 B 中的某一位不同，那么在数字 A 和 B 中的这一位必然是一个为 0，另一个为 1；而我们在 bitFlag 中将其他位都设置为 0，那么该位为 0 的数字与上 bitFlag 就等于 0，而该位为 1 的数字与上 bitFlag 就等于 bitFlag
4. 现在问题就简单了，我们只需要在循环一次数组，将与上 bitFlag 为 0 的数字进行 XOR 运算，与上 bitFlag 不为 0 的数组进行独立的 XOR 运算。那么最后我们得到的这两个数字就是 A 和 B。

```java
//pick one bit as flag
int bitFlag = (AXORB & (~ (AXORB - 1)));
```

这一行代码的作用是：`找到数字 A 和数字 B 中不相同的一位，并将该位设置为 1，其他位设置为 0；`

> 根据 XOR 的定义，我们知道，在 AXORB 中，为 1 的位即 A 和 B 不相同的位，AXORB 中为 0 的位即 A 和 B 中相同的位
>
> 所以，要找到 A 和 B 中不相同的位，只需要找到在 AXORB 中从右往左第一个为 1 的位，保留该位并将其他位置为 0 即可。


```python
class Solution:
    """
    @param A: An integer array
    @return: An integer array
    """
    def singleNumberIII(self, A):
        # write your code here
        if A is None or len(A) % 2 != 0:
            return []

        xor = 0
        for num in A:
            xor ^= num

        diff = xor & (~ (xor - 1))
        res = [0] * 2
        for num in A:
            if num & diff == 0:
                res[0] ^= num
            else:
                res[1] ^= num

        return res
```
