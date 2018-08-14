# 141. Sqrt(x)

- **Description**
    - Implement int sqrt(int x).
    - Compute and return the square root of x.
- **Example**

    ```java
    sqrt(3) = 1
    sqrt(4) = 2
    sqrt(5) = 2
    sqrt(10) = 3
    ```

- **Challenge**
    - O(log(x))


## Solution

Binary Search



### Python

```python
class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        if (x == 0): return x

        start, end = 1, x

        while (start + 1 < end):
            mid = (end - start) // 2 + start

            if (mid ** 2 == x):
                return mid
            elif (mid ** 2 > x):
                end = mid
            else:
                start = mid

        if (start ** 2 <= x):
            return start
        else:
            return end
```

### Java


```java
public class Solution {
    /**
     * @param x: An integer
     * @return: The sqrt of x
     */
    public int sqrt(int x) {
        // write your code here
        if (x < 0) return -1;
        if (x == 0) return 0;

        long start = 1, end = x;

        while (start + 1 < end) {

            long mid = (end - start) / 2 + start;
            long mul = mid * mid;

            if (mul < x) {
                start = mid;
            } else if (mul > x) {
                end = mid;
            } else if (mul == x) {
                return (int)mid;
            }
        }

        if (start * start <= x) {
            return (int)start;
        } else {
            return (int)end;
        }

    }
}
```
