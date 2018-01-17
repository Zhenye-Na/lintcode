# 179. Update Bits

- **Description**
    - Given two 32-bit numbers, `N` and `M`, and two bit positions, `i` and `j`. Write a method to set all bits between `i` and `j` in `N` equal to `M` (e g , `M` becomes a substring of `N` located at `i` and starting at `j`)
    - In the function, the numbers `N` and `M` will given in decimal, you should also return a decimal number.
- **Clarification**
    - You can assume that the bits `j` through `i` have enough space to fit all of `M`. That is, if `M=10011`， you can assume that there are at least 5 bits between j and i. You would not, for example, have `j=3` and `i=2`, because `M` could not fully fit between bit `3` and bit `2`.
- **Example**
    - Given `N=(10000000000)2`, `M=(10101)2`, `i=2`, `j=6`
    - return `N=(10001010100)2`
- **Challenge**
    - Minimum number of operations?


## Solution

### 九章微课堂解法：


```java
n = (1024)10 = (00000000000000000000010000000000)2; // 我们这里用32位表述
m =   (21)10 = (00000000000000000000000000010101)2; // 1 + 4 + 16 = 21, 这里同样我们用32位表述
i = 2, j = 6,
```

那么根据题目，我们希望最终得到的结果是 `(00000000000000000000010001010100)2` = `(1108)10`

根据题意，有一个想法，将n中第i位到第j位先置为0，然后，按位或上m << i即可。

现在问题是如何将n中第i位到第j位置为0 ? 可以考虑构造一个数，这个数从第i位到第j位是0，其他位都为1。然后这个数和n与一下，就可以把n的i~j位置成0了。
虽然这样的数并不是很好构造，反过来思考我们构造一个数从第i位到第j位都是1，其他位为0的数，然后将这个数取反，就可以得到从第i位到第j位是0，其他位是1的数。
-1的二进制表示是所有位为1 (这一点很重要，32位全是1的二进制对应整数-1.)，我们以这个数为起点，需要的做的是将高(31-j)位置0，将低i位置0. 按照例子中i = 2, j = 6, 所以我们需要把-1看成全是1的二进制表示，然后把高(31 - 6) = 25位全部置成0，低2位也置成0。

`(-1)10 = (11111111111111111111111111111111)2`, 把-1的前面25位和后面2位置成0之后，结果为 `=>(00000000000000000000000001111100)2`

**所以具体的操作应该是这样的：**

- **将-1先左移(31-j)位，因为高(31-j)位都是不需要的**：

    ```java
    (-1)10 << (31 - 6) = (-1) << 25 = (11111110000000000000000000000000)2 = (-33554432)10
    ```

- **然后再在这个基础上逻辑右移(31 - j + i)位，因为要将低i位置0**：

    ```java
    (-33554432)10 >>> (31 - 6 + 2) = (00000000000000000000000000011111)2 = (31)10
    ```


> 你可以思考一下为什么前面我们需要27个0？
> 你还可以思考一下，这里为什么要用逻辑右移？

- **最后我们左移i位，这里也就是左移2位，将1恢复到正确的位置即可。即得到第i位到第j位是1，其他位是0的数。**

    ```java
    (31)10 << 2 = (00000000000000000000000000011111)2 << 2 = (00000000000000000000000001111100)2 = (124)10
    ```

Java 代码如下：

```java
class Solution {
    /**
     *@param n, m: Two integer
     *@param i, j: Two bit positions
     *return: An integer
     */
    public int updateBits(int n, int m, int i, int j) {
        return ((~((((-1) << (31 - j)) >>> (31 - j + i)) << i)) & n) | (m << i);
    }
}
```

### CTCI

**Cracking The Coding Interview** 上的题，题意简单来讲就是使用 `M` 代替 `N` 中的第 `i` 位到第 `j` 位。很显然，我们需要借用掩码操作。大致步骤如下：

- 得到第`i`位到第`j`位的比特位为`0`，而其他位均为`1`的掩码`mask`。
- 使用`mask`与 `N` 进行按位与，清零 `N` 的第`i`位到第`j`位。
- 对 `M` 右移 `i` 位，将 `M` 放到 `N` 中指定的位置。
- 返回 `N | M` 按位或的结果。

获得掩码 `mask` 的过程可参考 CTCI 书中的方法，先获得掩码 `(1111...000...111)` 的左边部分，然后获得掩码的右半部分，最后左右按位或即为最终结果。


```cpp
class Solution {
public:
    /**
     *@param n, m: Two integer
     *@param i, j: Two bit positions
     *return: An integer
     */
    int updateBits(int n, int m, int i, int j) {
        int ones = ~0;
        int mask = 0;
        if (j < 31) {
            int left = ones << (j + 1);
            int right = ((1 << i) - 1);
            mask = left | right;
        } else {
            mask = (1 << i) - 1;
        }

        return (n & mask) | (m << i);
    }
};
```
