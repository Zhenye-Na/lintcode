# 1797. optimalUtilization

**Description**

Give two sorted arrays. To take a number from each of the two arrays, the sum of the two numbers needs to be less than or equal to `k`, and you need to find the index combination with the largest sum of the two numbers. Returns a pair of indexes containing two arrays. If you have multiple index answers with equal sum of two numbers, you should choose the index pair with the smallest index of the first array.

- The sum of the two numbers `<= k`
- The sum is the biggest
- Both array indexes are kept to a minimum

**Example**

Example 1:

```
A = [1, 4, 6, 9], B = [1, 2, 3, 4], K = 9
return [2, 2]
```

Example 2:

```
Input: 
A = [1, 4, 6, 8], B = [1, 2, 3, 5], K = 12
Output:
[2, 3]
```

```java
public class Solution {
    /**
     * @param A: a integer sorted array
     * @param B: a integer sorted array
     * @param K: a integer
     * @return: return a pair of index
     */
    public int[] optimalUtilization(int[] A, int[] B, int K) {
        // write your code here
        if (A == null || A.length == 0) {
            return new int[0];
        }
        if (B == null || B.length == 0) {
            return new int[0];
        }

        int indexA = 0;
        int indexB = 0;

        for (int i = 0; i < A.length; i++) {
            int currentSum = A[indexA] + B[indexB];

            for (int j = 0; j < B.length; j++) {
                if (A[i] + B[j] == K) {
                    return new int[] { i, j };
                } else if (A[i] + B[j] < K) {
                    if (A[i] + B[j] > currentSum) {
                        indexA = i;
                        indexB = j;
                        currentSum = A[indexA] + B[indexB];
                    }
                } else { // A[i] + B[J] > K
                    break;
                }
            }
        }

        return new int[] { indexA, indexB };

    }
}
```