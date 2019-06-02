# 495. Implement Stack

**Description**

Implement a stack. You can use any data structure inside a stack except stack itself to implement it.

**Example**

Example 1:

```
Input:
push(1)
pop()
push(2)
top()  // return 2
pop()
isEmpty() // return true
push(3)
isEmpty() // return false
```

Example 2:

```
Input:
isEmpty()
```

用 python list 直接实现 stack

```python
class Stack:
    s = []

    """
    @param: x: An integer
    @return: nothing
    """
    def push(self, x):
        # write your code here
        self.s.append(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        self.s.pop()

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        return self.s[-1]

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        return len(self.s) == 0
```