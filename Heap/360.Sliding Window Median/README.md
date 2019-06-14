# 360. Sliding Window Median

**Description**

Given an array of `n` integer, and a moving window (size `k`), move the window at each iteration from the start of the array, find the `median` of the element inside the window at each moving. (If there are even numbers in the array, return the `N/2-th` number after sorting the element in the window.)

**Example**

Example 1:

```
Input:
[1,2,7,8,5]
3
Output:
[2,7,7]

Explanation:
At first the window is at the start of the array like this `[ | 1,2,7 | ,8,5]` , return the median `2`;
then the window move one step forward.`[1, | 2,7,8 | ,5]`, return the median `7`;
then the window move one step forward again.`[1,2, | 7,8,5 | ]`, return the median `7`;
```

Example 2:

```
Input:
[1,2,3,4,5,6,7]
4
Output:
[2,3,4,5]

Explanation:
At first the window is at the start of the array like this `[ | 1,2,3,4, | 5,6,7]` , return the median `2`;
then the window move one step forward.`[1,| 2,3,4,5 | 6,7]`, return the median `3`;
then the window move one step forward again.`[1,2, | 3,4,5,6 | 7 ]`, return the median `4`;
then the window move one step forward again.`[1,2,3,| 4,5,6,7 ]`, return the median `5`;
```

**Challenge**

`O(nlog(n))` time


**HashMap + Heap**

```
使用九章算法强化班中讲到的 HashHeap。即一个 Hash + Heap。
Hash 的 key 是 Heap 里的每个元素，值是这个元素在 Heap 中的下标。

要做这个题首先需要先做一下 Data Stream Median。这个题是只在一个集合中增加数，不删除数，然后不断的求中点。
Sliding Window Median，就是不断的增加数，删除数，然后求中点。比 Data Stream Median 难的地方就在于如何支持删除数。

因为 Data Stream Median 的方法是用 两个 Heap，一个 max heap，一个min heap。所以删除的话，就需要让 heap 也支持删除操作。
由于 Python 的 heapq 并不支持 logn 时间内的删除操作，因此只能自己实现一个 hash + heap 的方法。
```

总体时间复杂度 `O(nlogk)`，`n` 是元素个数，`k` 是 window 的大小。



```python
# 本参考程序来自九章算法，由 @九章算法 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class HashHeap:
    
    def __init__(self, desc=False):
        self.hash = dict()
        self.heap = []
        self.desc = desc
        
    @property
    def size(self):
        return len(self.heap)
        
    def push(self, item):
        self.heap.append(item)
        self.hash[item] = self.size - 1
        self._sift_up(self.size - 1)
        
    def pop(self):
        item = self.heap[0]
        self.remove(item)
        return item
    
    def top(self):
        return self.heap[0]
        
    def remove(self, item):
        if item not in self.hash:
            return
            
        index = self.hash[item]
        self._swap(index, self.size - 1)
        
        del self.hash[item]
        self.heap.pop()
        
        # in case of the removed item is the last item
        if index < self.size:
            self._sift_up(index)
            self._sift_down(index)

    def _smaller(self, left, right):
        return right < left if self.desc else left < right

    def _sift_up(self, index):
        while index != 0:
            parent = index // 2
            if self._smaller(self.heap[parent], self.heap[index]):
                break
            self._swap(parent, index)
            index = parent
    
    def _sift_down(self, index):
        if index is None:
            return
        while index * 2 < self.size:
            smallest = index
            left = index * 2
            right = index * 2 + 1
            
            if self._smaller(self.heap[left], self.heap[smallest]):
                smallest = left
                
            if right < self.size and self._smaller(self.heap[right], self.heap[smallest]):
                smallest = right
                
            if smallest == index:
                break
            
            self._swap(index, smallest)
            index = smallest
        
    def _swap(self, i, j):
        elem1 = self.heap[i]
        elem2 = self.heap[j]
        self.heap[i] = elem2
        self.heap[j] = elem1
        self.hash[elem1] = j
        self.hash[elem2] = i
    
class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        if not nums or len(nums) < k:
            return []
            
        self.maxheap = HashHeap(desc=True)
        self.minheap = HashHeap()
        
        for i in range(0, k - 1):
            self.add((nums[i], i))
            
        medians = []
        for i in range(k - 1, len(nums)):
            self.add((nums[i], i))
            # print(self.maxheap.heap, self.median, self.minheap.heap)
            medians.append(self.median)
            self.remove((nums[i - k + 1], i - k + 1))
            # print(self.maxheap.heap, self.median, self.minheap.heap)
            
        return medians
            
    def add(self, item):
        if self.maxheap.size > self.minheap.size:
            self.minheap.push(item)
        else:
            self.maxheap.push(item)
            
        if self.maxheap.size == 0 or self.minheap.size == 0:
            return
            
        if self.maxheap.top() > self.minheap.top():
            self.maxheap.push(self.minheap.pop())
            self.minheap.push(self.maxheap.pop())
        
    def remove(self, item):
        self.maxheap.remove(item)
        self.minheap.remove(item)
        if self.maxheap.size < self.minheap.size:
            self.maxheap.push(self.minheap.pop())
        
    @property
    def median(self):
        return self.maxheap.top()[0]
```



**heapq**

heapq 支持 pop, 但是 pop 出来的是当前的最小值, 所以用了 list.remove() 但是这个是 O(n) 的时间, 会比较慢

```python
import heapq

class Solution:
    """
    @param nums: A list of integers
    @param k: An integer
    @return: The median of the element inside the window at each moving
    """
    def medianSlidingWindow(self, nums, k):
        # write your code here
        if not nums or len(nums) == 0:
            return []

        if k > len(nums):
            return []

        if k == 1:
            return nums

        medians = []

        # elemements greater than median
        minHeap = []

        # elements smaller than median
        maxHeap = []

        # initialize
        heapq.heappush(maxHeap, - nums[0])
        for i in range(1, k - 1):
            if nums[i] > - maxHeap[0]:
                heapq.heappush(minHeap, nums[i])
            else:
                heapq.heappush(maxHeap, - nums[i])

        for i in range(k - 1, len(nums)):
            # add new element
            if nums[i] > - maxHeap[0]:
                heapq.heappush(minHeap, nums[i])
            else:
                heapq.heappush(maxHeap, - nums[i])
            self._balance(minHeap, maxHeap)

            # append result
            medians.append(- maxHeap[0])

            # remove left-wise element
            if nums[i + 1 - k] > - maxHeap[0]:
                minHeap.remove(nums[i + 1 - k])
                heapq.heapify(minHeap)
            else:
                maxHeap.remove(- nums[i + 1 - k])
                heapq.heapify(maxHeap)
            self._balance(minHeap, maxHeap)

        return medians

    def _balance(self, minHeap, maxHeap):
        while len(maxHeap) > len(minHeap) + 1:
            heapq.heappush(minHeap, - heapq.heappop(maxHeap))

        while len(maxHeap) < len(minHeap):
            heapq.heappush(maxHeap, - heapq.heappop(minHeap))
```