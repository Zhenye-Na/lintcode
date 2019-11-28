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
