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
