# 1. A + B Problem

**Description**

Write a function that add two numbers `A` and `B`.

**Clarification**

Are a and b both 32-bit integers? Yes.  

Can I use bit operation? Sure you can.

**Example**

Given `a=1` and `b=2` return `3`.

**Challenge**

Of course you can just return a + b to get accepted. But Can you challenge not do it like that?(You should not use + or any arithmetic operators.)

> There is no need to read data from standard input stream. Both parameters are given in function `aplusb`, you job is to calculate the sum and return it.

**位运算**

Explanation

- `int result = a ^ b;`: `XOR` plus operation without carry.
- `int carry = (a & b) << 1;` : if `a` and `b` have `1` at the same position, it will give a `0` at that position, `carrry << 1` will have the same effect of giving one carry out.
- `aplusb(result, carry);` add carry to result.


```java
public class Solution {
    /**
     * @param a: An integer
     * @param b: An integer
     * @return: The sum of a and b
     */
    public int aplusb(int a, int b) {
        // write your code here
        int result = a ^ b;         // `sum` without carry 0+0=0, 0+1=1+0=1, 1+1=0
        int carry = (a & b) << 1;   // 1 + 1 = 2
        if (carry != 0) {
            return aplusb(result, carry);
        }
        return result;
    }
}
```


主要利用异或运算来完成，异或运算有一个别名叫做：不进位加法，我们在前面的基本运算第二章中有提到过。
那么 `a ^ b` 就是 `a` 和 `b` 相加之后，该进位的地方不进位的结果，相信这一点大家没有疑问，但是需要注意的是，这个加法是在二进制下完成的加法。
然后下面考虑哪些地方要进位？

什么地方需要进位呢？ 自然是a和b里都是1的地方
`a & b` 就是 `a` 和 `b` 里都是 `1` 的那些位置，那么这些位置左边都应该有一个进位 `1`，`a & b << 1` 就是进位的数值(`a & b`的结果所有左移一位)。

那么我们把不进位的结果和进位的结果加起来，就是实际中a + b的和。

```
a + b = (a ^ b) + (a & b << 1)
```

令

```
a' = a ^ b, b' = (a & b) << 1 => a + b = (a ^ b) + (a & b << 1) = a' + b'
```

然后反复迭代，这个过程是在二进制下模拟加法的运算过程，进位不可能一直持续，所以b最终会变为0，也就是没有需要进位的了，因此重复做上述操作就可以
最终求得 `a + b` 的值



```java
public class Solution {
    /**
     * @param a: An integer
     * @param b: An integer
     * @return: The sum of a and b
     */
    public int aplusb(int a, int b) {
        // write your code here
        int sum = a, carry = 0;
        while (b != 0) {
            // sum of (a, b) without carry
            sum =  a ^ b;

            // carry bits
            carry = (a & b) << 1;

            a = sum;
            b = carry;
        }
        return sum;
    }
}
```
