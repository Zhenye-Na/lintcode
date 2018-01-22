# 181. Flip Bits

- **Description**
    - Determine the number of bits required to flip if you want to convert integer n to integer m.
    - Both n and m are 32-bit integers.
- **Example**
    - Given `n = 31(11111)`, `m = 14(01110)`, return `2`.
- **Challenge**
    - 你能想出几种方法？


## Solution

思考将整数A转换为B，如果A和B在第i（0 <=i < 32）个位上相等，则不需要改变这个BIT位，如果在第i位上不相等，则需要改变这个BIT位。

所以问题转化为了A和B有多少个BIT位不相同！

联想到位运算有一个异或操作，相同为0，相异为1，所以问题转变成了计算A异或B之后这个数中1的个数!

### 1. Built-in `Java` Function

```java
public class Solution {
    /**
     * @param a: An integer
     * @param b: An integer
     * @return: An integer
     */
    public int bitSwapRequired(int a, int b) {
        // write your code here
        String bit = Integer.toBinaryString(a ^ b);
        int num = 0;
        for (int i = 0; i < bit.length(); i++) {
            num += (bit.charAt(i) - '0');
        }
        return num;
    }
}
```

### 2. `XOR` Operator

```java
class Solution {
    /**
     *@param a, b: Two integer
     *return: An integer
     */
    public int countOnes(int num) {
        int count = 0;
        while (num != 0) {
            num = num & (num - 1);
            count++;
        }
        return count;
    }

    public int bitSwapRequired(int a, int b) {
        // write your code here
        return countOnes(a ^ b);
    }
};
```
