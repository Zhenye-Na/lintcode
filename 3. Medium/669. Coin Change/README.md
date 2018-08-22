# 669. Coin Change

- **Description**
    - You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return `-1`.
    - You may assume that you have an infinite number of each kind of coin.
- **Example**
    - Given `coins = [1, 2, 5]`, `amount = 11`
        - return `3` (11 = 5 + 5 + 1)
    - Given `coins = [2]`, `amount = 3`
        - return `-1`.


## Solution

1. 确定状态
    - 状态在动态规划中的作用属于定海神针, 
    - 确定最后一步 --- 最优策略中使用的最后一枚硬币 `A(k)` 
    - 化成子问题 --- 最少的硬币拼出更小的面值 `27-A(k)`
2. 转移方程
    - `f(x)` = 最少用多少枚硬币拼出 `X`
    - `f(27) = min {f(27-2) + 1, f(27-5) + 1, f(27-7) + 1}`
3. 初始条件和边界条件
    - 如果不能拼出Y，就定义 `F[Y]=正无穷`，
    - `x-2`, `x-5`，`x-7` 少于0怎么办
    - `f[0] = 0`
4. 拼出X所需要的最少硬币数
    - 计算 `f[1],f[2],...,f[7]`

**消除冗余，加速计算**



### Code

```java
public class Solution {
    /**
     * @param coins: a list of integer
     * @param amount: a total amount of money amount
     * @return: the fewest number of coins that you need to make up
     */
    public int coinChange(int[] coins, int amount) {
        // write your code here
        
        int[] f = new int[amount + 1];
        int n = coins.length;
        
        // Initialization
        f[0] = 0;
        
        for (int i = 1; i <= amount; i++) {
            
            f[i] = Integer.MAX_VALUE;
            
            for (int j = 0; j < n; j++) {
                
                if (i - coins[j] >= 0 && f[i - coins[j]] != Integer.MAX_VALUE) {
                    f[i] = Math.min(f[i], f[i - coins[j]] + 1);
                }
                
            }
            
        }
        
        // Double check
        if (f[amount] != Integer.MAX_VALUE) {
            return f[amount];
        } else {
            return -1;
        }
        
    }
}
```