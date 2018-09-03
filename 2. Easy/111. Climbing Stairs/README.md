# 111. Climbing Stairs

- **Description**
- You are climbing a stair case. It takes n steps to reach to the top.
- Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
- **Example**
- Given an example n=3 , 1+1+1=2+1=1+2=3
- return 3


## Solution

### Dynamic Programming

```python
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        if n == 1:
            return 1

        if n == 0:
            return 0

        dp = [sys.maxint] * (n + 1)
        dp[1], dp[2] = 1, 2

        for i in xrange(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]

```


### Follow up

爬楼梯 多一个 base 可以是 1步 2步 3步

```java
static long countSteps(int n) { 
    if(n == 0) {
        return 0;
    }
    int m = 3;
    long res[] = new long[n+1];
    res[0] = 1;
    res[1] = 1;
    
    for(int i = 2; i < n + 1; i++){
        res[i] = 0;
        for(int j = 1; j <= m && j <=i; j++){
            res[i] += res[i-j];
        }
    }
    return res[n];
}

notes:

public class Solution {
    public int climbStairs(int n) {
        if (n <= 1) {
            return n;
        }
        int last = 1, lastlast = 1;
        int now = 0;
        
        for (int i = 2; i <= n; i++) {
            now = last + lastlast;
            lastlast = last;
            last = now;
        }
        return now;

    }

}

m = 2, ways(n) = ways(n-1) + ways(n-2) 

generalization: ways(n, m) = ways(n-1, m) + ways(n-2, m) + ... + ways(n-m, m) 

// a recursive function used by countWays 

static int countWaysUtil(int n, int m) {
    int res[] = new int[n];
    res[0] = 1;
    res[1] = 1;
    for(int i = 2; i < n; i++) {
        res[i] = 0;
        for(int j = 1; j <= m && j <=i; j++){
            res[i] += res[i-j];
        }
    }
    return res[n-1];

} 

//returns number of ways to reach s'th stair 
int countWays(int s, int m){
    return countWaysUtil(s + 1, m);
}
```