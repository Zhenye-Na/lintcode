# 64. Merge Sorted Array
Description
Given two sorted integer arrays A and B, merge B into A as one sorted array.

You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.

Have you met this question in a real interview?  
Example
A = [1, 2, 3, empty, empty], B = [4, 5]

After merge, A will be filled as [1, 2, 3, 4, 5]



## Solution

### `java.lang.System.arraycopy()`

```java
public static void arraycopy(Object src,
                             int srcPos,
                             Object dest,
                             int destPos,
                             int length)
```

```java
public class Solution {
    /*
     * @param A: sorted integer array A which has m elements, but size of A is m+n
     * @param m: An integer
     * @param B: sorted integer array B which has n elements
     * @param n: An integer
     * @return: nothing
     */
    public void mergeSortedArray(int[] A, int m, int[] B, int n) {
        // write your code here

        int idx = m + n - 1;
        int pa = m - 1, pb = n - 1;
        while (pa >= 0 && pb >= 0) {
            if (B[pb] > A[pa]) {
                A[idx--] = B[pb--];
            } else {
                A[idx--] = A[pa--];
            }
        }

        if (pb >= 0) {
            System.arraycopy(B, 0, A, 0, pb + 1);
        }


        if (pa >= 0) {
            System.arraycopy(A, 0, A, 0, pa + 1);
        }

    }


}
```

### While

```java
public class Solution {
    /*
     * @param A: sorted integer array A which has m elements, but size of A is m+n
     * @param m: An integer
     * @param B: sorted integer array B which has n elements
     * @param n: An integer
     * @return: nothing
     */
    public void mergeSortedArray(int[] A, int m, int[] B, int n) {
        // write your code here

        int idx = m + n - 1;
        int pa = m - 1, pb = n - 1;
        while (pa >= 0 && pb >= 0) {
            if (B[pb] > A[pa]) {
                A[idx--] = B[pb--];
            } else {
                A[idx--] = A[pa--];
            }
        }

        while (pb >= 0) {
            A[idx--] = B[pb--];
        }

        while (pa >= 0) {
            A[idx--] = A[pa--];
        }

    }


}
```
