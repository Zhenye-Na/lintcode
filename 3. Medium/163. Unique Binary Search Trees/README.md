# 163. Unique Binary Search Trees

- **Description**
    - Given n, how many structurally unique BSTs (binary search trees) that store values `1...n`?
- **Example**
    - Given `n = 3`, there are a total of `5` unique BST's.

    ```
    1           3    3       2      1
     \         /    /       / \      \
      3      2     1       1   3      2
     /      /       \                  \
    2     1          2                  3
    ```


## Solution

**n^th Catalan Number + Dynamic Programming**

**Recommended video:**

- Understand what is Catalan Numbers:
  - [![Program for Nth Catalan Number | GeeksforGeeks](https://img.youtube.com/vi/2NZF2UKyh0g/0.jpg)](https://www.youtube.com/watch?v=2NZF2UKyh0g)
- Understand why we can use Catalan Numbers to solve this problem:
  - [![Count Number of Binary Search Tree Possible given n keys Dynamic Programming](https://img.youtube.com/vi/YDf982Lb84o/0.jpg)](https://www.youtube.com/watch?v=YDf982Lb84o)

Catalan numbers are a sequence of natural numbers that occurs in many interesting counting problems like following.

1. Count the **number of expressions containing n pairs of parentheses which are correctly matched**. For `n = 3`, possible expressions are `((()))`, `()(())`, `()()()`, `(())()`, `(()())`.
2. Count the **number of possible Binary Search Trees with n keys**
3. Count the **number of full binary trees** (A rooted binary tree is full if every vertex has either *two children or no children*) with `n+1` leaves.
4. Triangulation of (`n+2`)gon
5. Handshake Problem

The first few Catalan numbers for `n = 0, 1, 2, 3, ...` are `1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, ...`

**Recursive Solution:**
Catalan numbers satisfy the following recursive formula.

![](https://www.geeksforgeeks.org/wp-content/ql-cache/quicklatex.com-5caf1032c7225d073dd41cd7a9fa4e38_l3.svg)

**Explanation using Formula catalan[3]:**

> Suppose we have **3 nodes**, and **values are 5, 6, 7**, then

- If 5 is selected as a root, nodes at left side = `0` and nodes at right side = `2`. `catalan[0] * catalan[2] = 1 * 2 = 2`
- If 6 is selected as a root, nodes at left side = `1` and nodes at right side = `1`. `catalan[1] * catalan[1] = 1 * 1 = 1`
- If 7 is selected as a root, nodes at left side = `2` and nodes at right side = `0`. `catalan[2] * catalan[0] = 2 * 1 = 2`
- `catalan[3] = 2 + 1 + 2 = 5`

**Q&A**

- When am I know this problem is solved by Catalan Numbers?
  - Just remember the numbers `"1,1,2,5,14,42,132,..."` and if you see them you apply for the formula


### Python

```python
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def numTrees(self, n):
        # write your code here
        if n <= 0:
            return 1

        # Table to store results of subproblems
        catalan = [0 for i in range(n + 1)]

        # Initialize first two values in table
        catalan[0] = 1
        catalan[1] = 1

        # Fill entries in catalan[] using recursive formula
        for i in range(2, n + 1):
            catalan[i] = 0
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i - j - 1]

        # Return last entry
        return catalan[n]
```

### C++

```cpp
class Solution {
public:
    /**
     * @param n: An integer
     * @return: An integer
     */
    int numTrees(int n) {
        // write your code here
        // Table to store results of subproblems
        unsigned long int catalan[n+1];

        // Initialize first two values in table
        catalan[0] = catalan[1] = 1;

        // Fill entries in catalan[] using recursive formula
        for (int i=2; i<=n; i++)
        {
            catalan[i] = 0;
            for (int j=0; j<i; j++)
                catalan[i] += catalan[j] * catalan[i-j-1];
        }

        // Return last entry
        return catalan[n];
    }
};

```
