# 2. Trailing Zeros

- **Description**
    - Write an algorithm which computes the number of trailing zeros in `n` factorial.
- **Example**
    - `11! = 39916800`, so the out should be `2`

Challenge
O(log N) time

## Solution

思考一个数尾部的零是怎么得来的，乘以10对吧，所以n的阶乘尾部有多少零就可以看成它有多少个10这个因子，而10又可分解为两个质因数相乘 $ 2\times5 $ 。将 n! 分解为质因数相乘的形式，大概是这样：

$$ n!=1\times2\times3\times(2\times2)\times5\times(2\times3)\times7\times(2\times2\times2)\times(3\times3)\times(2\times5)...n!=1×2×3×(2×2)×5×(2×3)×7×(2×2×2)×(3×3)×(2×5)... $$

显然，2的个数会比5的个数多，所以有多少个5就会有多少个10。故而问题就转化为寻找 n!n! 的结果有多少个5这个因子。

那么这个怎么找呢？我们看一下上边的等式，现在已经乘到10了，出现了2个5，想象一下继续乘下去的情况，到15时会再出现一个，到20时又会再出现一个，到25时则会出现2个，继续看下去，就会发现一个规律：

1. 每逢遇到5的倍数，就会出现一个；
1. 每逢遇到5的幂次方的倍数，就会出现5的幂次方的指数个，为了便于计算，我们把遇到5的幂次方的倍数时也算到5的倍数里，这时遇到5的幂次方的倍数就会出现(5的幂次方的指数-(5的幂次方的指数-1))个，也就是1个。

### Python

```python
class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        # write your code here, try to do it without arithmetic operators.
        count = 0
        while n != 0:
            n /= 5
            count += n
        return count
```
