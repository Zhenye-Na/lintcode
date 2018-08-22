# 763. Hex Conversion

- **Description**
    - Given a decimal number `n` and an integer `k`, Convert decimal number `n` to base-`k`.
    1. `0 <= n <= 2^31 - 1`, `2 <= k <= 16`
    2. Each letter over 9 is indicated in uppercase
- **Example**

    ```java
    Example 1:
    Given n = 5, k = 2
    return "101"
    ```
    
    ```java
    Example 2:
    Given n = 30, k = 16
    return "1E"
    ```

## Solution


### Java

```java
public class Solution {
    /**
     * @param n: a decimal number
     * @param k: a Integer represent base-k
     * @return: a base-k number
     */

    char[] dict = {'0', '1', '2', '3', '4', '5', '6', '7',
                   '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'
                  };
    public String hexConversion(int n, int k) {
        // write your code here

        char[] digits = new char[k];
        System.arraycopy(dict, 0, digits, 0, k);

        int q = n / k;
        int r = n % k;
        LinkedList<Character> l = new LinkedList<>();
        l.add(0, digits[r]);

        while (q != 0) {
            n = q;
            q = n / k;
            r = n % k;
            l.add(0, digits[r]);
        }

        StringBuilder sb = new StringBuilder();
        for (char d : l) {
            sb.append(d);
        }

        return sb.toString();
    }
}
```
