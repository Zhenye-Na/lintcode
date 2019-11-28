class Vector2D(object):

    # @param vec2d {List[List[int]]}
    def __init__(self, vec2d):
        # Initialize your data structure here
        self.next_ele = None
        self.stack = []
        for vec in reversed(vec2d):
            self.stack.append(vec)

    # @return {int} a next element
    def next(self):
        # Write your code here
        if self.next_ele is None:
            self.hasNext()
        element, self.next_ele = self.next_ele, None
        return element

    # @return {boolean} true if it has next element
    # or false
    def hasNext(self):
        # Write your code here
        if self.next_ele:
            return True

        while self.stack:
            top = self.stack.pop()
            if isinstance(top, int):
                self.next_ele = top
                return True

            for elem in reversed(top):
                self.stack.append(elem)

        return False


# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())
