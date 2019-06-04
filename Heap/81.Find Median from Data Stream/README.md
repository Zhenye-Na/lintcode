# 81. Find Median from Data Stream

**Description**

Numbers keep coming, return the median of numbers at every time a new number added.

**Clarification**

What's the definition of Median?

The median is not equal to median in math.
Median is the number that in the middle of a sorted array. If there are n numbers in a sorted array A, the median is A[(n - 1) / 2]A[(n−1)/2].
For example, if A=[1,2,3], median is 2. If A=[1,19], median is 1.

**Example**

Example 1

```
Input: [1,2,3,4,5]
Output: [1,1,2,2,3]
Explanation:
The medium of [1] and [1,2] is 1.
The medium of [1,2,3] and [1,2,3,4] is 2.
The medium of [1,2,3,4,5] is 3.
```

Example 2

```
Input: [4,5,1,3,2,6,0]
Output: [4,4,4,3,3,3,3]
Explanation:
The medium of [4], [4,5], [4,5,1] is 4.
The medium of [4,5,1,3], [4,5,1,3,2], [4,5,1,3,2,6] and [4,5,1,3,2,6,0] is 3.
```

**Challenge**

Total run time in `O(nlogn)`.

**Min Heap and Max Heap**

用 maxheap 保存左半部分的数，用 minheap 保存右半部分的数。

把所有的数一左一右的加入到每个部分。左边部分最大的数就一直都是 median。

这个过程中，可能会出现左边部分并不完全都 `<=` 右边部分的情况。这种情况发生的时候，交换左边最大和右边最小的数即可。

```
把比 median 小的放在 maxheap 里，把比 median 大的放在 minheap 里。median 单独放在一个变量里。
每次新增一个数的时候，先根据比当前的 median 大还是小丢到对应的 heap 里。

丢完以后，再处理左右两边的平衡性:
    如果左边太少了，就把 median 丢到左边，从右边拿一个最小的出来作为 median。
    如果右边太少了，就把 median 丢到右边，从左边拿一个最大的出来作为新的 median。
```


```python
from heapq import heappush, heappop, heappushpop

class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return nums

        # medians -> return lists
        # min_heap -> elements that are greater than median
        # max_heap -> elements that are less than median
        min_heap, max_heap, medians = [], [], []

        medians.append(nums[0])
        heappush(max_heap, - nums[0])

        for i in range(1, len(nums)):

            if nums[i] <= - max_heap[0]:
                heappush(max_heap, - nums[i])
            else:
                heappush(min_heap, nums[i])

            if len(max_heap) > len(min_heap) + 1:
                heappush(min_heap, - heappop(max_heap))
            elif len(max_heap) < len(min_heap):
                heappush(max_heap, - heappop(min_heap))

            medians.append(- max_heap[0])

        return medians
```


**Min Heap**

*Time Limit Exceeded*

> 89% test cases passed

```python
import math
import heapq

class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return nums

        heap = []
        medians = []
        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])
            medians.append(self._findMedian(heap))

        return medians

    def _findMedian(self, heap):
        k = (len(heap) - 1) // 2 + 1
        return heapq.nsmallest(k, heap)[-1]
```