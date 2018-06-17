# 1. A + B Problem

## Description
Write a function that add two numbers A and B.

> There is no need to read data from standard input stream. Both parameters are given in function `aplusb`, you job is to calculate the sum and return it.
 
### Clarification
Are a and b both 32-bit integers? Yes.  
Can I use bit operation? Sure you can.

### Example
Given `a=1` and `b=2` return `3`.

### Challenge
Of course you can just return a + b to get accepted. But Can you challenge not do it like that?(You should not use + or any arithmetic operators.)


## Solution

```java
public class Solution {
    /**
     * @param a: An integer
     * @param b: An integer
     * @return: The sum of a and b 
     */
    public int aplusb(int a, int b) {
        // write your code here
        int result = a ^ b;         // + without carry 0+0=0, 0+1=1+0=1, 1+1=0
        int carry = (a & b) << 1;   // 1 + 1 = 2
        if (carry != 0) {
            return aplusb(result, carry);
        }
        return result;
    }
}
```

### Explanation


- `int result = a ^ b;`: `XOR` plus operation without carry.
- `int carry = (a & b) << 1;` : if `a` and `b` have `1` at the same position, it will give a `0` at that position, `carrry << 1` will have the same effect of giving one carry out.
- `aplusb(result, carry);` add carry to result.