# 6. Merge Two Sorted Arrays

**Description**

Merge two given sorted ascending integer array A and B into a new sorted integer array.

**Example**

Example 1:

```
Input:  A=[1], B=[1]
Output: [1,1]	
Explanation:  return array merged.
```

Example 2:

```
Input:  A=[1,2,3,4], B=[2,4,5,6]
Output: [1,2,2,3,4,4,5,6]	
Explanation: return array merged.
```

**Challenge**

How can you optimize your algorithm if one array is very large and the other is very small?


solution to challenge:

for 循环数组长度小的, binary search 数组长度大的, 找到 "第一个比 target 大的位置" 插进去

```python
class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        if len(A) < len(B):
            temp = A
            A = B
            B = temp

        # binary search and insert
        for ele in B:
            left = 0
            right = len(A) - 1
            while left + 1 < right:
                mid = int(left + (right - left) / 2)
                if ele < A[mid]:
                    right = mid
                else:
                    left = mid

            if ele < A[left]:
                A.insert(left, ele)
            elif ele > A[right]:
                A.insert(right + 1, ele)
            else:
                A.insert(right, ele)

        return A
```



**正常解法**

使用两个指针分别对数组从小到大遍历，每次取二者中较小的放在新数组中。直到某个指针先到结尾，另一个数组中剩余的数字直接放在新数组后面。

时间复杂度O(n)


```python
class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        i, j = 0, 0
        C = []
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        while i < len(A):
            C.append(A[i])
            i += 1
        while j < len(B):
            C.append(B[j])
            j += 1
            
        return C
```
