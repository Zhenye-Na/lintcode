# 81. Find Median from Data Stream

**Description**

Numbers keep coming, return the median of numbers at every time a new number added.

**Clarification**

What's the definition of Median?

The median is not equal to median in math.

Median is the number that in the middle of a sorted array. If there are `n` numbers in a sorted array `A`, the median is `A[(n - 1) / 2]`.

For example, if `A=[1,2,3]`, median is `2`. If `A=[1,19]`, median is `1`.

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
把比 median 小的放在 maxheap 里, 把比 median 大的放在 minheap 里。median 单独放在一个变量里。
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

用到两个堆, 但是可以有两种方式解决

- 跟中位数去比较大小, 决定放在哪一侧, 然后去平衡两个堆得大小
- 直接按照堆的大小去添加元素, 然后去平衡两个堆得大小

**第一种**

针对每一个 num, 拿它去和 已知的 median 去做比较, 根据大小关系, 把他放在对应的 heap 里面

```python
from heapq import heappush, heappop

class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return []

        # 用两个堆
        # max_heap 存放小于 median 的数
        # min_heap 存放大于 median 的数

        # 不跟 median 比较
        min_heap, max_heap = [], []
        medians = []
        for num in nums:

            if len(max_heap) == 0 or num < - max_heap[0]:
                heappush(max_heap, - num)
            else:
                heappush(min_heap, num)

            # balance
            # len(max_heap) == len(min_heap) or len(max_heap) == len(min_heap) + 1
            if len(max_heap) < len(min_heap):
                heappush(max_heap, - heappop(min_heap))
            elif len(max_heap) > len(min_heap) + 1:
                heappush(min_heap, - heappop(max_heap))

            # median is stored on top of max_heap
            medians.append(- max_heap[0])

        return medians
```

**第二种**

不去做比较 根据两个 heap 的大小来决定 放在哪里, 然后 balance 两个 heap

```python
from heapq import heappush, heappop

class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        # write your code here
        if not nums or len(nums) == 0:
            return []

        # 用两个堆
        # max_heap 存放小于 median 的数
        # min_heap 存放大于 median 的数

        # 不跟 median 比较
        min_heap, max_heap = [], []
        medians = []
        for num in nums:

            if len(max_heap) == 0 or len(max_heap) <= len(min_heap):
                heappush(max_heap, - num)
            else:
                heappush(min_heap, num)

            if len(max_heap) != 0 and len(min_heap) != 0:
                self.balance(min_heap, max_heap)

            medians.append(- max_heap[0])

        return medians

    def balance(self, min_heap, max_heap):
        if - max_heap[0] > min_heap[0]:
            heappush(min_heap, - heappop(max_heap))
            heappush(max_heap, - heappop(min_heap))
```
