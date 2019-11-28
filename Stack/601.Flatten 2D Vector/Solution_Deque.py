from collections import deque

class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.queue = deque(vec2d)
        self.next_elem = None

    # @return {int} a next element
    def next(self):
        # Write your code here
        if self.next_elem is None:
            self.hasNext()

        res, self.next_elem = self.next_elem, None
        return res


    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        if self.next_elem is not None:
            return True

        while self.queue:
            item = self.queue.popleft()
            if isinstance(item, list):
                for l in reversed(item):
                    self.queue.appendleft(l)
            else:
                self.next_elem = item
                return True

        return False



# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())