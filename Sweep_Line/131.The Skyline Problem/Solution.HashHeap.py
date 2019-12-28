# 本参考程序来自九章算法，由 @令狐冲 提供。版权所有，转发请注明出处。
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
            parent = (index - 1) // 2
            if self._smaller(self.heap[parent], self.heap[index]):
                break
            self._swap(parent, index)
            index = parent

    def _sift_down(self, index):
        if index is None:
            return
        while index * 2 + 1 < self.size:
            smallest = index
            left = index * 2 + 1
            right = index * 2 + 2

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
    @param buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """

    def buildingOutline(self, buildings):
        points = []
        for index, (start, end, height) in enumerate(buildings):
            points.append((start, height, index, True))
            points.append((end, height, index, False))
        points = sorted(points)

        maxheap = HashHeap(desc=True)
        intervals = []
        last_position = None
        for position, height, index, is_start in points:
            max_height = maxheap.top()[0] if maxheap.size else 0
            self.merge_to(intervals, last_position, position, max_height)
            if is_start:
                maxheap.push((height, index))
            else:
                maxheap.remove((height, index))
            last_position = position

        return intervals

    def merge_to(self, intervals, start, end, height):
        if start is None or height == 0 or start == end:
            return

        if not intervals:
            intervals.append([start, end, height])
            return

        _, prev_end, prev_height = intervals[-1]
        if prev_height == height and prev_end == start:
            intervals[-1][1] = end
            return

        intervals.append([start, end, height])
