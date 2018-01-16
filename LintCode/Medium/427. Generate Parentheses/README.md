# 427. Generate Parentheses

- **Description**
    - Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
- **Example**
    - Given `n = 3`, a solution set is:

    ```java
    "((()))", "(()())", "(())()", "()(())", "()()()"
    ```


## Solution

Backtracking


### Java

```java
public class Solution {
    /**
     * @param n: n pairs
     * @return: All combinations of well-formed parentheses
     */
    public List<String> generateParenthesis(int n) {
        // write your code here
        List<String> result = new ArrayList<>();
        if (n <= 0) return result;
        helper(result, "", n, n);
        return result;
    }

    private static void helper(List<String> result, String chosen, int left, int right) {
        // If remaining left is greater than right -> # ")" is greater than #"(", return
        if (left > right) {
            return;
        }

        // Remaining "(" and ")" are 0 -> valid pairs, return
        if (left == 0 && right == 0) {
            result.add(chosen);
            return;
        }

        // add "("
        if (left > 0) {
            helper(result, chosen + "(", left - 1, right);
        }

        // add ")"
        if (right > 0) {
            helper(result, chosen + ")", left, right - 1);
        }
    }
}
```
