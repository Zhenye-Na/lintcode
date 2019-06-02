# 494. Implement Stack by Two Queues

**Description**

Implement a stack by two queues. The queue is first in first out (FIFO). That means you can not directly pop the last element in a queue.

**Example**

Example 1:

```
Input:
push(1)
pop()
push(2)
isEmpty() // return false
top() // return 2
pop()
isEmpty() // return true
```

Example 2:

```
Input:
isEmpty()
```

在pop之后, 要交换 stack1 和 stack2

```python
from collections import deque


class Stack:
    """
    Initialization
    """
    def __init__(self):
        self.q1 = deque([])
        self.q2 = deque([])

    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        self.q1.append(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        while self.q1 and len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        ele = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return ele


    """
    @return: An integer
    """
    def top(self):
        # write your code here
        while self.q1 and len(self.q1) > 1:
            self.q2.append(self.q1.popleft())

        ele = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        self.q1.append(ele)
        return ele

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return len(self.q1) == 0
```
