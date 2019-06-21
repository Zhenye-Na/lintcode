# 1065. My Calendar I

**Description**

Implement a `MyCalendar` class to store your events. A new `event` can be added if adding the event will not cause a double booking.

Your class will have the method, `book(int start, int end)`. Formally, this represents a booking on the half open interval [`start, end)`, the range of real numbers x such that `start <= x < end`.

A double booking happens when two events have some `non-empty` intersection (ie., there is some time that is common to both events.)

For each call to the method `MyCalendar.book`, return true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: `MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)`

- The number of calls to `MyCalendar.book` per test case will be at most `1000`.
- In calls to `MyCalendar.book(start, end)`, start and end are integers in the range `[0, 10^9]`.

**Example**

```
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(15, 25); // returns false
MyCalendar.book(20, 30); // returns true
Explanation: 
The first event can be booked.  The second can't because time 15 is already booked by another event.
The third event can be booked, as the first event takes every time less than 20, but not including 20.
```


**Sweep Line**

扫描线

可以用扫描线来解决的问题的特点有:

1. 首先是一个 "区间", 在这道题目里就是 `event` 的开始时间以及结束时间
2. 要将这个 `event` 的 `start` 和 `end` 打散进行排序, 是扫描线问题的一个 trick

这道题目要求不可以有任何一个 event 跟已经 create 好的 event 有时间上的交集, 也就是说明, 扫描线扫上一遍, 最多只能是 1, 因为如果出现了 2, 那么就相当于前一个 event 还没结束, 下一个 event 就已经开始了, 这时候, 我们把它从 list 里面 remove 掉

时间复杂度

- 排序 $O(N logN)$
- `remove()` $O(N)$

空间复杂度

- O(N)

```python
class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        start_interval, end_interval = (start, 1), (end, -1)
        self.events.append(start_interval)
        self.events.append(end_interval)
        self.events.sort()

        # sweep line
        num_of_event, max_concurrent_events = 0, -1
        for _, delta in self.events:
            num_of_event += delta
            max_concurrent_events = max(max_concurrent_events, num_of_event)
            if max_concurrent_events > 1:
                self.events.remove(start_interval)
                self.events.remove(end_interval)
                return False

        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
```


**方法二**

构造特殊的二叉搜索树 (https://baike.baidu.com/item/%E4%BA%8C%E5%8F%89%E6%90%9C%E7%B4%A2%E6%A0%91/7077855?fr=aladdin)

```
1. 类似在常见的二叉搜索树中查找某个数一样，如果我们能够实现出一种特殊的二叉搜索树，使得：
2. 树中每个节点是已加的一个时间段。
3. 能方便地查找新时间段与树中节点是否重叠。
4. 这样就能大幅提高效率。庆幸的是，这种想法是可行的。
5. 具体地，从树根开始搜索，当前搜索节点指向树根。新的时间段与当前节点有三种可能：
6. 完全在当前节点左侧，则当前节点指向左孩子；
7. 完全在当前节点右侧，则当前节点指向右孩子；
8. 有重叠，直接返回false。
9. 循环该过程，直到当前节点指空。指空说明新的时间段与整棵树无重叠，则把新的时间段添加在当前位置，并返回true。
10. 至此，整个算法已经结束。下文给出两点补充：
11. 有的同学可能会问，为什么这种做法是正确的？为什么当前节点指空一定说明无重叠？要注意，二叉搜索树的作用可看作是提供了一个排好序的列表，在二叉搜索树中搜索就像是在这个有序列表搜索某个元素一样，如果当前节点指空，说明指向了有序列表的两个相邻元素中间位置，这也就意味着搜索不到该元素。在这里，即是新时间段与所有时间段无重叠。
12. 如果使用的是Java，那么可以使用TreeMap (https://docs.oracle.com/javase/7/docs/api/java/util/TreeMap.html)这种数据结构。TreeMap 是一个有序的key-value集合，它通过红黑树 (http://www.cnblogs.com/skywang12345/p/3245399.html)实现，继承于AbstractMap，所以它是一个Map，即一个key-value集合。TreeMap可以查询小于等于某个值的最大的key，也可查询大于等于某个值的最小的key。所以，在该题中，对于每个以start开始、end结束的新时间段，若用start做key，end做value，只需查询TreeMap中start值相邻两侧的key，保证左侧end <= start <= end <= 右侧start即可。这种方法与前述方法二类似，都是使用了二叉搜索树（TreeMap所使用的红黑树也是一种二叉搜索树），只不过这里的节点有一种以start做key，end做value的特殊结构，但原理相同，所以仍可看作是方法二。
13. 复杂度分析：
14. 时间复杂度：O(N * logN)，N是添加成功的时间段数量，对于每一个时间段的搜索需要O(logN)，添加需要O(1)。（*注意：*这里的O(N * logN)只能看作是平均时间复杂度，因为搜索最坏需要O(N)。 如果在手动构造二叉搜索树时实现了平衡处理或者使用了TreeMap等标准库，可保证O(N * logN)仍为最坏时间复杂度）
15. 空间复杂度O(N)，用于构造二叉树。
```

```python
class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None

    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False

class MyCalendar(object):
    def __init__(self):
        self.root = None

    def book(self, start, end):
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
```


**Traverse**

从头到尾扫描比较一次

```python
class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        if len(self.events) == 0:
            self.events.append([start, end])
            return True

        else:
            for event in self.events:
                if not (event[1] <= start or event[0] >= end):
                    return False

            self.events.append([start, end])
            self.events.sort()
            return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
```