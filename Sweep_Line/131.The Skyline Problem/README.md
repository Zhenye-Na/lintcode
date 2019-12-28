# 131. The Skyline Problem

**Description**

Given `N` buildings in a x-axis，each building is a rectangle and can be represented by a triple `(start, end, height)`, where start is the start position on x-axis, end is the end position on x-axis and height is the height of the building. Buildings may overlap if you see them from far away，find the outline of them.

An outline can be represented by a triple, `(start, end, height)`, where `start` is the start position on x-axis of the outline, `end` is the end position on x-axis and `height` is the height of the outline.

![Building Outline](https://lintcode-media.s3.amazonaws.com/problem/jiuzhang3.jpg)

```
Please merge the adjacent outlines if they have the same height and make sure different outlines cant overlap on x-axis.
```

**Example**

Example 1

```
Input:
[
    [1, 3, 3],
    [2, 4, 4],
    [5, 6, 1]
]
Output:
[
    [1, 2, 3],
    [2, 4, 4],
    [5, 6, 1]
]
Explanation:
The buildings are look like this in the picture. The yellow part is buildings.
```

![](https://media-cdn.jiuzhang.com/markdown/images/6/20/18bd686e-934d-11e9-a170-0242ac110002.jpg)

Example 2

```
Input:
[
    [1, 4, 3],
    [6, 9, 5]
]
Output:
[
    [1, 4, 3],
    [6, 9, 5]
]
Explanation:
The buildings are look like this in the picture. The yellow part is buildings.
```

![](https://media-cdn.jiuzhang.com/markdown/images/6/20/58c5f08e-934d-11e9-a170-0242ac110002.jpg)


**只用 Python 里的 heapq**

- `list.remove()` 是 `O(n)` 的

```python
from heapq import heappush, heapify

class Solution:
    """
    @param buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """
    def buildingOutline(self, buildings):
        # write your code here
        building_outlines = []
        for idx, building in enumerate(buildings):
            start, end, height = building
            # start position, height, is_start, building index
            building_outlines.append([start, height, True, idx])
            building_outlines.append([end, height, False, idx])
        building_outlines.sort()

        answer = []
        building_heap = []
        prev_position = None

        for position, height, is_start, building_index in building_outlines:
            top_height = -building_heap[0][0] if building_heap else 0
            self.merge(answer, prev_position, position, top_height)
            if is_start:
                heappush(building_heap, (- height, building_index))
            else:
                # after remove, we need re-heapify
                building_heap.remove((- height, building_index))
                heapify(building_heap)

            prev_position = position

        return answer

    def merge(self, answer, start, end, height):
        if start is None or start == end or height == 0:
            return

        if len(answer) == 0:
            answer.append([start, end, height])
            return

        else:
            prev_start, prev_end, prev_height = answer[-1]
            if prev_height == height and prev_end == start:
                answer[-1][1] = end
            else:
                answer.append([start, end, height])
```

**用 Python 中的 heapq, set**

```python
from heapq import heappush, heappop

class Solution:
    """
    @param buildings: A list of lists of integers
    @return: Find the outline of those buildings
    """
    def buildingOutline(self, buildings):
        # write your code here
        building_outlines = []
        for idx, building in enumerate(buildings):
            start, end, height = building
            # start position, height, is_start, building index
            building_outlines.append([start, height, True, idx])
            building_outlines.append([end, height, False, idx])
        building_outlines.sort()

        answer = []
        building_heap = []
        prev_position = None
        history = set([])

        for position, height, is_start, building_index in building_outlines:
            top_height = -building_heap[0][0] if building_heap else 0
            self.merge(answer, prev_position, position, top_height)

            if is_start:
                heappush(building_heap, (- height, building_index))
            else:
                # record which building should be removed
                history.add(building_index)

            # removed
            while building_heap and building_heap[0][1] in history:
                heappop(building_heap)

            prev_position = position

        return answer

    def merge(self, answer, start, end, height):
        if start is None or start == end or height == 0:
            return

        if len(answer) == 0:
            answer.append([start, end, height])
            return

        else:
            prev_start, prev_end, prev_height = answer[-1]
            if prev_height == height and prev_end == start:
                answer[-1][1] = end
            else:
                answer.append([start, end, height])
```

**在 Python 中自己创建一个新的数据结构 - Hash Heap**

因为如果不用 set 删除操作是 `O(n)` Hash Heap 可以做到 `O(1)`

```python
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
```

**Java 语言可以使用 TreeSet**

当然我不用 Java -.-!

```java
/**
 * 本参考程序来自九章算法，由 @杨同学 提供。版权所有，转发请注明出处。 -
 * 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。 -
 * 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班， - Big Data
 * 项目实战班，算法面试高频题班, 动态规划专题班 - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code
 */

public class Solution {
    /**
     * @param buildings: A list of lists of integers
     * @return: Find the outline of those buildings
     */
    public class Point {
        int bldg;
        int x;
        int height;
        int status;

        public Point(int bldg, int x, int height, int status) {
            this.bldg = bldg;
            this.x = x;
            this.height = height;
            this.status = status;
        }
    }

    public class Height {
        int height;
        int bldg;

        public Height(int height, int bldg) {
            this.height = height;
            this.bldg = bldg;
        }
    }

    public List<List<Integer>> buildingOutline(int[][] buildings) {
        List<List<Integer>> result = new ArrayList<>();
        if (buildings.length == 0) {
            return result;
        }

        // 拆解每个建筑物为两个点，起点和终点，并存储到points中
        List<Point> points = new ArrayList<>();
        for (int i = 0; i < buildings.length; i++) {
            int[] b = buildings[i];
            points.add(new Point(i, b[0], b[2], 1));
            points.add(new Point(i, b[1], b[2], -1));
        }

        // 对points进行排序，排序优先级为，横坐标>进入or离开>高度
        Collections.sort(points, new Comparator<Point>() {
            public int compare(Point a, Point b) {
                if (a.x != b.x) {
                    return a.x - b.x;
                }
                if (a.status != b.status) {
                    return a.status - b.status;
                }
                return a.height - b.height;
            }
        });

        // 使用TreeSet存储当前位置的建筑物高度，最高者即为当前区间的高度
        TreeSet<Height> ts = new TreeSet<>(new Comparator<Height>() {
            public int compare(Height a, Height b) {
                if (a.height == b.height) {
                    return a.bldg - b.bldg;
                }
                return a.height - b.height;
            }
        });

        // 先向TreeSet中添加第一个点
        int curtX = points.get(0).x;
        int curtH = points.get(0).height;
        int curtB = points.get(0).bldg;
        ts.add(new Height(curtH, curtB));

        // 循环所有之前拆解的点，找到区间并合并
        for (int i = 1; i < points.size(); i++) {
            Point p = points.get(i);
            int height = ts.isEmpty() ? 0 : ts.last().height;
            List<Integer> interval = new ArrayList<>();
            interval.add(curtX);
            interval.add(p.x);
            interval.add(height);
            mergeTo(result, interval);

            if (p.status == 1) {
                ts.add(new Height(p.height, p.bldg));
            }
            if (p.status == -1) {
                ts.remove(new Height(p.height, p.bldg));
            }

            curtX = p.x;
        }

        return result;
    }

    private void mergeTo(List<List<Integer>> result, List<Integer> interval) {
        if ((int) interval.get(0) == (int) interval.get(1) || interval.get(2) == 0) {
            return;
        }
        if (result.size() == 0) {
            result.add(interval);
            return;
        }

        List<Integer> prev = result.get(result.size() - 1);
        if ((int) prev.get(2) == (int) interval.get(2) && (int) prev.get(1) == (int) interval.get(0)) {
            prev.set(1, interval.get(1));
        } else {
            result.add(interval);
        }
    }
}
```
