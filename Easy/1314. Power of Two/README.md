# 1314. Power of Two

- **Description**
    - Given an integer, write a function to determine if it is a power of two.

## Solution

满足要求的`N`有两个条件：

- N > 0
- N 的二进制表示有且只有一个1

```java
x & (x - 1) // 消去 x 最后一位的 1，比如 x = 12，那么在二进制下就是 (1100)2
​
x           = 1100
x - 1       = 1011
x & (x - 1) = 1000
```

### Java

```java
public class Solution {
    /**
     * @param n: an integer
     * @return: if n is a power of two
     */
    public boolean isPowerOfTwo(int n) {
        // Write your code here
        return (n > 0) && ((n & (n - 1)) == 0);
    }
}
```
