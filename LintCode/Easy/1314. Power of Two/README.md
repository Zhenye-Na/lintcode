# 1314. Power of Two

Description
Given an integer, write a function to determine if it is a power of two.

## Solution

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
