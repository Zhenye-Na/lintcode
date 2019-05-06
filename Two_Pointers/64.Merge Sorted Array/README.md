# 64. Merge Sorted Array

**Description**

Given two sorted integer arrays A and B, merge B into A as one sorted array.

You may assume that A has enough space (size that is greater or equal to `m + n`) to hold additional elements from B. The number of elements initialized in A and B are `m` and `n` respectively.


**Example**

Example 1:

```
Input：[1, 2, 3] 3  [4,5]  2
Output：[1,2,3,4,5]
Explanation:
After merge, A will be filled as [1, 2, 3, 4, 5]
```

Example 2:
```
Input：[1,2,5] 3 [3,4] 2
Output：[1,2,3,4,5]
Explanation:
After merge, A will be filled as [1, 2, 3, 4, 5]
```


分析: 涉及两个有序数组合并, 设置i和j双指针, 分别从两个数组的尾部想头部移动,并判断 `A[i]` 和 `B[j]` 的大小关系, 从而保证最终数组有序, 同时每次 `index` 从尾部向头部移动

```python
class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        ap, bp = m - 1, n - 1
        idx = m + n - 1

        while ap >= 0 and bp >= 0 and idx >= 0:
            if A[ap] > B[bp]:
                A[idx] = A[ap]
                ap -= 1
            else:
                A[idx] = B[bp]
                bp -= 1
            idx -= 1

        while ap >= 0:
            A[idx] = A[ap]
            ap -= 1
            idx -= 1

        while bp >= 0:
            A[idx] = B[bp]
            bp -= 1
            idx -= 1
```

### `java.lang.System.arraycopy()`

```java
public static void arraycopy(Object src,
                             int srcPos,
                             Object dest,
                             int destPos,
                             int length)
```

这道题是要求 **merge in place**，而且 `A` 里面的空位个数等于 `B.size()` 

两根指针 -> 剩下的用 `System.arraycopy()` 加进去

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

两根指针，余下的用 while 放进去

```java
class Solution {
    /**
     * @param A: sorted integer array A which has m elements, 
     *           but size of A is m+n
     * @param B: sorted integer array B which has n elements
     * @return: void
     */
    public void mergeSortedArray(int[] A, int m, int[] B, int n) {
        int i = m-1, j = n-1, index = m + n - 1;
        while (i >= 0 && j >= 0) {
            if (A[i] > B[j]) {
                A[index--] = A[i--];
            } else {
                A[index--] = B[j--];
            }
        }
        while (i >= 0) {
            A[index--] = A[i--];
        }
        while (j >= 0) {
            A[index--] = B[j--];
        }
    }
}
```
