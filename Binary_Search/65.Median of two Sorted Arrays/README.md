# 65. Median of two Sorted Arrays


**Description**

There are two sorted arrays A and B of size `m` and `n` respectively. Find the median of the two sorted arrays.

**Clarification**


中位数的定义:

- 这里的中位数等同于数学定义里的**中位数**.
- 中位数是排序后数组的中间值.
- 如果有数组中有 `n` 个数且 `n` 是奇数，则中位数为 $A[(n-1)/2]A[(n−1)/2]$.
- 如果有数组中有 `n` 个数且 `n` 是偶数，则中位数为 $(A[n / 2] + A[n / 2 + 1]) / 2(A[n/2]+A[n/2+1])/2$.
- 比如：数组 `A=[1,2,3]` 的中位数是 `2`, 数组 `A=[1,19]` 的中位数是 `10`。


**Example**

Example 1

```
Input:
A = [1,2,3,4,5,6]
B = [2,3,4,5]
Output: 3.5
```

Example 2

```
Input:
A = [1,2,3]
B = [4,5]
Output: 3
```

**Challenge**

The overall run time complexity should be `O(log (m+n))`.




**分析:**

1. 从时间复杂度推算法
    - 题目要求 `O(log(m+n))`，`m` 和 `n` 分别是两个数组的长度，所以我们要在 `O(1)` 的时间，将整个问题缩小
2. 也就是要将数组大小减小 `(m+n)/2`，以达到要求
    - 比较 `A` 和 `B` 第 `(m+n)/2` 个数的大小，然后选择性将其中一个数组的 startIndex 后移 `k/2` 即可
3. 注意数组总长度



```java
public class Solution {
    /*
     * @param A: An integer array
     * @param B: An integer array
     * @return: a double whose format is *.5 or *.0
     */
    public double findMedianSortedArrays(int[] A, int[] B) {
        // write your code here
        int total = A.length + B.length;
        if (total % 2 == 0) {
            return (findKth(A, 0, B, 0, total / 2) + findKth(A, 0, B, 0, total / 2 + 1)) / 2.0;
        } else {
            return findKth(A, 0, B, 0, total / 2 + 1);
        }
    }

    private int findKth(int[] A, int indexA, int[] B, int indexB, int k) {

        // A is empty
        if (indexA >= A.length) {
            return B[indexB + k - 1];
        }

        // B is empty
        if (indexB >= B.length) {
            return A[indexA + k - 1];
        }

        if (k == 1) {
            return Math.min(A[indexA], B[indexB]);
        }

        // 防止数组不够长，用 Integer.MAX_VALUE 来填充
        int keyA = Integer.MAX_VALUE;
        int keyB = Integer.MAX_VALUE;

        if (indexA + k / 2 - 1 < A.length) {
            keyA = A[indexA + k / 2 - 1];
        }

        if (indexB + k / 2 - 1 < B.length) {
            keyB = B[indexB + k / 2 - 1];
        }

        if (keyA < keyB) {
            return findKth(A, indexA + k / 2, B, indexB, k - k / 2);
        } else {
            return findKth(A, indexA, B, indexB + k / 2, k - k / 2);
        }

    }

}
```
