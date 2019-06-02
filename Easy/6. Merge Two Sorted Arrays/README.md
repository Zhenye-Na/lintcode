# 6. Merge Two Sorted Arrays

- **Description**
    - Merge two given sorted integer array A and B into a new sorted integer array.
- **Example**

    ```
    A=[1,2,3,4]
    B=[2,4,5,6]
    ```

    - return `[1,2,2,3,4,4,5,6]`
- **Challenge**
    - How can you optimize your algorithm if one array is very large and the other is very small?


## Solution

### 遍历 + 比较

```java
public class Solution {
    /**
     * @param A: sorted integer array A
     * @param B: sorted integer array B
     * @return: A new sorted integer array
     */
    public int[] mergeSortedArray(int[] A, int[] B) {
        // write your code here
        if (A == null || B == null) {
            return null;
        }

        int alength = A.length;
        int blength = B.length;

        int[] result = new int[alength + blength];
        int i = 0, j = 0, index = 0;

        while (i < alength && j < blength) {
            if (A[i] < B[j]) {
                result[index++] = A[i++];
            } else {
                result[index++] = B[j++];
            }
        }

        while (i < alength) {
            result[index++] = A[i++];
        }
        while (j < blength) {
            result[index++] = B[j++];
        }

        return result;

    }
}
```

### Follow up Question
#### How can you optimize your algorithm if one array is very large and the other is very small?

**Binary Search**

```java
public class Solution {
    /**
     * @param A: sorted integer array A
     * @param B: sorted integer array B
     * @return: A new sorted integer array
     */
    public int[] mergeSortedArray(int[] A, int[] B) {
        if (A == null || A.length == 0) return B;
        if (B == null || B.length == 0) return A;
        int[] res = new int[A.length + B.length];

        int idx = 0;
        int pa = 0;
        for (int i = 0; i < B.length; i++) {
            int position = binarySearch(A, B[i]);
            while (pa < position) {
                res[idx++] = A[pa++];
            }
            res[idx++] = B[i];
        }

        while (pa < A.length) {
            res[idx++] = A[pa++];
        }
        return res;
    }

    private int binarySearch(int[] A, int target) {
        int left = 0;
        int right = A.length - 1;

        while (left <= right) {
            int mid = (right - left) / 2 + left;
            if (A[mid] == target) return mid;
            if (target < A[mid]) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }

}
```
