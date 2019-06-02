# 83. Single Number II

- **Description**
    - Given `3 * n + 1` numbers, every numbers occurs triple times except one, find it.
- **Example**
    - Given `[1,1,2,3,3,3,2,2,4,1]` return `4`
- **Challenge**
    - One-pass, constant extra space.


## Solution

### Solution 1

由于 `x^x^x = x`，无法直接利用 `I` 的方法来解。但可以应用类似的思路，即利用位运算来消除重复3次的数。以一个数组`[14 14 14 9]`为例，将每个数字以二进制表达：

1110  
1110  
1110  
1001  

* * *

4331 对每一位进行求和  
1001 对每一位的和做`%3`运算，来消去所有重复`3`次的数  

`Java` 代码如下：

```java
public class Solution {
    /**
     * @param A: An integer array
     * @return: An integer
     */
    public int singleNumberII(int[] A) {
        // write your code here
        int result = 0, length = A.length, bit;
        for (int i = 0; i < 32; i++) {
            bit = 0;
            for (int k = 0; k < length; k++) {
                bit += (A[k] >>> i) & 1;
            }
            bit = bit % 3;
            result = result | (bit << i);
        }
        return result;
    }
}
```

### Solution 2

因为其他数是出现三次的，也就是说，对于每一个二进制位，如果只出现一次的数在该二进制位为1，那么这个二进制位在全部数字中出现次数无法被3整除。对于每一位，我们让Two，One表示当前位的状态。

我们看Two和One里面的每一位的定义，对于`ith`(表示第i位)：

```
如果Two里面`ith`是1，则`ith`当前为止出现1的次数模3的结果是2
如果One里面`ith`是1，则`ith`目前为止出现1的次数模3的结果是1
```

注意Two和One里面不可能`ith`同时为1，因为这样就是3次，每出现3次我们就可以抹去（消去）。那么最后One里面存储的就是每一位模3是1的那些位，综合起来One也就是最后我们要的结果。

如果B表示输入数字的对应位，Two+和One+表示更新后的状态, 那么新来的一个数B，此时跟原来出现1次的位做一个异或运算，&上~Two的结果(也就是不是出现2次的)，那么剩余的就是当前状态是1的结果。
同理Two ^ B （2次加1次是3次，也就是Two里面`ith`是1，B里面`ith`也是1，那么`ith`应该是出现了3次，此时就可以消去，设置为0），我们相当于会消去出现3次的位。

但是Two ^ B也可能是`ith`上Two是0，B的`ith`是1，这样Two里面就混入了模3是1的那些位！！！怎么办？我们得消去这些！我们只需要保留不是出现模3余1的那些位`ith`，而One是恰好保留了那些模3余1次数的位，取反不就是不是模3余1的那些位`ith`么？最终对(~One+)取一个&即可。

综合起来就是：

```
One+ = (One ^ B) & (~Two)
Two+ = (~One+) & (Two ^ B)
```


```java
public class Solution {
    /**
     * @param A: An integer array
     * @return: An integer
     */
    public int singleNumberII(int[] A) {
        // write your code here
        int ones = 0, twos = 0;
        for(int i = 0; i < A.length; i++){
            ones = (ones ^ A[i]) & ~twos;
            twos = (twos ^ A[i]) & ~ones;
        }
        return ones;
    }
}

```
