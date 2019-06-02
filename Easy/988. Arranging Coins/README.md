# 988. Arranging Coins

- **Description**
    - You have a total of `n` coins that you want to form in a staircase shape, where every k-th row must have exactly `k` coins.
    - Given `n`, find the total number of full staircase rows that can be formed.
    - `n` is a non-negative integer and fits within the range of a 32-bit signed integer.
- **Example**
    - Example 1:
    
    ```
    n = 5
    
    The coins can form the following rows:
    ¤
    ¤ ¤
    ¤ ¤
    
    Because the 3rd row is incomplete, we return 2.
    ```
    
    - Example 2:
    
    ```
    n = 8
    
    The coins can form the following rows:
    ¤
    ¤ ¤
    ¤ ¤ ¤
    ¤ ¤
    
    Because the 4th row is incomplete, we return 3.
    ```


## Solution

### Binary Search + Arithmetic Sequence

#### Python

```python
class Solution:
    """
    @param n: a non-negative integer
    @return: the total number of full staircase rows that can be formed
    """
    def arrangeCoins(self, n):
        # Write your code here
        start, end = 0, n
        while start + 1 < end:
            mid = (end - start) / 2 + start

            if n - self.summation(1, mid) == mid or n - self.summation(1, mid) == mid - 1:
                return mid
            elif n - self.summation(1, mid) > mid:
                start = mid
            else:
                end = mid

        if n - self.summation(1, start) == start or n - self.summation(1, start) == start - 1:
            return start
        else:
            return end


    def summation(self, start, end):
        return (start + end) * (end - start + 1) / 2;
```


#### Java

```java
public class Solution {
    /**
     * @param n: a non-negative integer
     * @return: the total number of full staircase rows that can be formed
     */
    public int arrangeCoins(int n) {
        // Write your code here

        if (n < 0) return 0;
        if (n == 1) return 1;
        long start = 1, end = n;

        // Binary Search
        while (start + 1 < end) {

            long mid = (end - start) / 2 + start;
            long summation = sum(1, mid);

            if (summation > n) {
                end = mid;
            } else {
                start = mid;
            }

        }

        if (sum(1, end) > n) {
            return (int) start;
        } else {
            return (int) end;
        }
    }

    private long sum(long start, long end) {
        return (start + end) * (end - start + 1) / 2;
    }

}
```
