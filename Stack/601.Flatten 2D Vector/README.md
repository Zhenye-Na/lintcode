# 601. Flatten 2D Vector

**Description**

Implement an iterator to flatten a 2d vector.

**Example**

Example 1:

```
Input:[[1,2],[3],[4,5,6]]
Output:[1,2,3,4,5,6]
```

Example 2:

```
Input:[[7,9],[5]]
Output:[7,9,5]
```

**Stack**

```python
from collections import deque


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
```