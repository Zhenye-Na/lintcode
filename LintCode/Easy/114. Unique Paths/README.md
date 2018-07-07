# 114. Unique Paths

- **Description**
    - A robot is located at the top-left corner of a `m` x `n` grid.
    - The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid.
    - How many possible unique paths are there?
    - `m` and `n` will be at most 100.
- **Example**
    - Given `m = 3` and `n = 3`, return `6`.
    - Given `m = 4` and `n = 5`, return `35`.



## Solution

### Combination

![](http://mathworld.wolfram.com/images/equations/Combination/NumberedEquation1.gif)

In this problem:

$$ C_{m+n-2}^{m-1} = \frac{(m+n-2)!}{(m-1)!(n-1)!} $$



### Dynamic Programming

![](http://2.bp.blogspot.com/-dz54gwDNkH4/U3y0an9k9jI/AAAAAAAAAsI/0OFqXLEKmxY/s1600/1111.png)


There are only two options for the robot to reach the target position:

- from (x - 1, y) to (x, y)
- from (x, y - 1) to (x, y)

#### Code

```java
public class Solution {
    /**
     * @param m: positive integer (1 <= m <= 100)
     * @param n: positive integer (1 <= n <= 100)
     * @return: An integer
     */
    public int uniquePaths(int m, int n) {
        // write your code here

        int[][] f = new int[m][n];
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                
                if (i == 0 || j == 0) {
                    f[i][j] = 1;
                    continue;
                } 
                
                f[i][j] = f[i - 1][j] + f[i][j - 1];
            }
        }

        return f[m - 1][n - 1];
    }

}
```
