# 1038. Jewels and Stones

- **Description**
    - You're given strings `J` representing the types of stones that are jewels, and `S` representing the stones you have. Each character in `S` is a type of stone you have. You want to know how many of the stones you have are also jewels.
    - The letters in `J` are guaranteed distinct, and all characters in `J` and `S` are letters. Letters are case sensitive, so `"a"` is considered a different type of stone from `"A"`.
    - `S` and `J` will consist of letters and have length at most `50`.
    - The characters in `J` are distinct.
- **Example**

    ```
    Example 1:
    Input: J = "aA", S = "aAAbbbb"
    Output: 3
    ```

    ```
    Example 2:
    Input: J = "z", S = "ZZ"
    Output: 0
    ```

## Solution

### `HashSet` in Java

```java
public class Solution {
    /**
     * @param J: the types of stones that are jewels
     * @param S: representing the stones you have
     * @return: how many of the stones you have are also jewels
     */
    public int numJewelsInStones(String J, String S) {
        // Write your code here
        if (J == null || J.length() == 0) {
            return 0;
        }

        Set<Character> set = new HashSet<>();
        for (int i = 0; i < J.length(); i++) {
            set.add(J.charAt(i));
        }

        int num = 0;
        for (int j = 0; j < S.length(); j++) {
            if (set.contains(S.charAt(j))) {
                num++;
            }
        }

        return num;
    }
}
```


### Python in one-line

```python
class Solution:
    """
    @param J: the types of stones that are jewels
    @param S: representing the stones you have
    @return: how many of the stones you have are also jewels
    """
    def numJewelsInStones(self, J, S):
        # Write your code here
        J = set(J)
        return sum(c in J for c in S)

```

### JavaScript

```javascript
const numJewelsInStones = function (J, S) {
    let [jewels, cnt] = [new Set(J), 0]
    for (let i in S) {
        if (jewels.has(S[i])) cnt++
    }
    return cnt
}

```
