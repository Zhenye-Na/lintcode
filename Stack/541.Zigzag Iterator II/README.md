# 541. Zigzag Iterator II

**Description**

Follow up Zigzag Iterator: What if you are given `k` 1d vectors? How well can your code be extended to such cases? The "Zigzag" order is not clearly defined and is ambiguous for `k > 2` cases. If "Zigzag" does not look right to you, replace "Zigzag" with "Cyclic".


**Example**

Example 1

```
Input: k = 3
vecs = [
    [1,2,3],
    [4,5,6,7],
    [8,9],
]
Output: [1,4,8,2,5,9,3,6,7]
```

Example 2

```
Input: k = 3
vecs = [
    [1,1,1]
    [2,2,2]
    [3,3,3]
]
Output: [1,2,3,1,2,3,1,2,3]
```

**Deque**

```python
from collections import deque


class ZigzagIterator2:
    """
    @param: vecs: a list of 1d vectors
    """
    def __init__(self, vecs):
        # do intialization if necessary
        self.queue = [deque(vector) for vector in vecs]

    """
    @return: An integer
    """
    def next(self):
        # write your code here
        for i in range(len(self.queue)):
            if self.queue[i]:
                ele = self.queue[i].popleft()
                self.queue.append(self.queue.pop(i))
                break
        return ele

    """
    @return: True if has next
    """
    def hasNext(self):
        # write your code here
        for q in self.queue:
            if q:
                return True
        return False

# Your ZigzagIterator2 object will be instantiated and called as such:
# solution, result = ZigzagIterator2(vecs), []
# while solution.hasNext(): result.append(solution.next())
# Output result
```