# 40. Implement Queue by Two Stacks

**Description**

As the title described, you should only use two stacks to implement a queue's actions.

The queue should support `push(element)`, `pop()` and `top()` where `pop` is pop the first (a.k.a front) element in the queue.

```
Both pop and top methods should return the value of first element.
Suppose the queue is not empty when the pop() function is called.
```
 
**Example**

Example 1:

```
Input:
    push(1)
    pop()    
    push(2)
    push(3)
    top()    
    pop()     
Output:
    1
    2
    2
```

Example 2:

```
Input:
    push(1)
    push(2)
    push(2)
    push(3)
    push(4)
    push(5)
    push(6)
    push(7)
    push(1)
Output:
[]
```

**Challenge**

implement it by two stacks, do not use any other data structure and `push`, `pop` and `top` should be `O(1)` by *AVERAGE*.


```python
class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self.s1 = []
        self.s2 = []

    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self.s1.append(element)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        while self.s1:
            self.s2.append(self.s1.pop())
        ele =  self.s2.pop()
        while self.s2:
            self.s1.append(self.s2.pop())

        return ele
    """
    @return: An integer
    """
    def top(self):
        # write your code here
        while self.s1:
            self.s2.append(self.s1.pop())
        ele = self.s2[-1]
        while self.s2:
            self.s1.append(self.s2.pop())
        return ele
```