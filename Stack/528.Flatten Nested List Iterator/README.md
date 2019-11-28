# 528. Flatten Nested List Iterator

**Description**

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

```
You don't need to implement the `remove()` method.
```

**Example**

Example 1

```
Input: list = [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
```

Example 2

```
Input: list = [1,[4,[6]]]
Output: [1,4,6]
```


**分析**

Iterator 相关问题有 `next()` 和 `hasNext()` 两个函数需要实现, 虽然 OJ 里面会说明每次调用是按照如下语句进行

```python
i, v = NestedIterator(nestedList), []
while i.hasNext():
    v.append(i.next())
```

但是面试的时候, 面试官可以 followup

- 1.多次调用 `hasNext()` 你的答案还对吗?
- 2.多次调用 `next()` 你的答案还对吗?

所以, 需要用到一个变量去记录下 下一个元素是什么, `hasNext()` 函数中的 `pointer` 不要乱移动, 否则问题一就是不对的了

具体实现的话

- stack
- deque

都能做

**Stack**

```python
"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""

from collections import deque


class NestedIterator(object):

    def __init__(self, nestedList):
        # Initialize your data structure here.
        # :type nestedList: List[NestedInteger]
        self.next_elem = None
        self.stack = []
        for elem in reversed(nestedList):
            self.stack.append(elem)

    # @return {int} the next element in the iteration
    def next(self):
        # Write your code here
        if self.next_elem is None:
            self.hasNext()
        temp, self.next_elem = self.next_elem, None
        return temp

    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        if self.next_elem:
            return True

        while self.stack:
            top = self.stack.pop()
            if top.isInteger():
                self.next_elem = top.getInteger()
                return True
            for elem in reversed(top.getList()):
                self.stack.append(elem)
        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
```


**Deque**

```python
"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""

from collections import deque

class NestedIterator(object):

    def __init__(self, nestedList):
        # Initialize your data structure here.
        self.queue = deque(nestedList)
        self.next_elem = None

    # @return {int} the next element in the iteration
    def next(self):
        # Write your code here
        if self.next_elem is None:
            self.hasNext()

        self.next_elem, res = None, self.next_elem
        return res

    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        if self.next_elem is not None:
            # do not move pointer
            # what if we call hasNext() several times ?
            return True

        while self.queue:
            element = self.queue.popleft()
            
            if element.isInteger():
                self.next_elem = element.getInteger()
                return True
            else:
                for elem in reversed(element.getList()):
                    self.queue.appendleft(elem)

        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
```