142. O(1) Check Power of 2
Description
Using O(1) time to check whether an integer n is a power of 2.

O(1) 时间复杂度

Have you met this question in a real interview?  
Example
For n=4, return true;

For n=5, return false;

Challenge
O(1) time


## Solution

`N`如果是`2`的幂次，则`N`满足两个条件。

- `N > 0`
- N的二进制表示中只有一个`1`, 注意只能有`1`个。

因为`N`的二进制表示中只有一个`1`，所以使用`N & (N - 1)`将`N`唯一的一个`1`消去，应该返回`0`。

```java
x & (x - 1) // 用于消去x最后一位的1, 比如x = 12, 那么在二进制下就是(1100)2

x           = 1100
x - 1       = 1011
x & (x - 1) = 1000
```



```java
public class Solution {
    /**
     * @param n: An integer
     * @return: True or false
     */
    public boolean checkPowerOf2(int n) {
        // write your code here
        return (n > 0) && ((n & (n - 1)) == 0);
    }
}
```
