# 543. Kth Largest in N Arrays

**Description**

Find `K-th` largest element in `N` arrays.

You can swap elements in the array

**Example**

Example 1:

```
Input:
k = 3, [[9,3,2,4,7],[1,2,3,4,8]]
Output:
7
Explanation:
the 3rd largest element is 7
```

Example 2:

```
Input:
k = 2, [[9,3,2,4,8],[1,2,3,4,2]]
Output:
8
Explanation:
the 1st largest element is 9, 2nd largest element is 8, 3rd largest element is 4 and etc.
```

**Min Heap**

把所有元素丢进去, 保持 heap 大小是 k, 最后堆顶就是答案

```python
from heapq import heappush, heapreplace

class Solution:
    """
    @param arrays: a list of array
    @param k: An integer
    @return: an integer, K-th largest element in N arrays
    """
    def KthInArrays(self, arrays, k):
        # write your code here
        if not arrays or len(arrays) == 0:
            return None

        heap = []
        for array in arrays:
            if not array or len(array) == 0:
                continue

            for num in array:
                if len(heap) >= k:
                    if num > heap[0]:
                        heapreplace(heap, num)
                else:
                    heappush(heap, num)

        return heap[0]
```


**Max Heap**

把数组排好序后把最大的取反都先扔进去, 然后经过 k 次循环, (相当于从大到小找答案用了 k 次), 把每次 pop 出来的元素 在数组中的前一个丢进 heap 里, 原因: 当前 pop 出去的是heap里最小的 (数组里当前循环最大的), 那么下一个最大的可能是其他数组当前最大的, 或者该数组中第二大 (也就是后一个元素)

```python
import heapq

class Solution:
    """
    @param arrays: a list of array
    @param k: An integer
    @return: an integer, K-th largest element in N arrays
    """
    def KthInArrays(self, arrays, k):
        if not arrays:
            return None

        # in order to avoid directly changing the original arrays
        # and remove the empty arrays, we need a new sortedArrays
        sortedArrays = []
        for arr in arrays:
            if not arr:
                continue
            sortedArrays.append(sorted(arr, reverse=True))

        maxheap = [
            (-arr[0], index, 0)
            for index, arr in enumerate(sortedArrays)
        ]
        heapq.heapify(maxheap)

        num = None
        for _ in range(k):
            num, x, y = heapq.heappop(maxheap)
            num = - num
            if y + 1 < len(sortedArrays[x]):
                heapq.heappush(maxheap, (-sortedArrays[x][y + 1], x, y + 1))

        return num
```