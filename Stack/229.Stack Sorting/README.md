# 229. Stack Sorting

**Description**

Sort a stack in ascending order (with biggest terms on top).

You may use at most one additional stack to hold items, but you may not copy the elements into any other data structure (e.g. array).

You don't need to return a new stack, just sort elements in the given parameter stack.

> `O(n^2)` time is acceptable.

Example

```
Given stack =

| |
|3|
|1|
|2|
|4|
 -

After sort, the stack should become:

| |
|4|
|3|
|2|
|1|
 -

The data will be serialized to [4,2,1,3]. The last element is the element on the top of the stack.
```


[YouTube - Interview Question: Sort Stacks](https://www.youtube.com/watch?v=nll-b4GeiX4)


```python
"""
In python, you can use list as stack
stack = [1,2,3,4]
Get top element: stack[-1]  -> 4
Pop element: stack.pop()   -> 4
Push element: stack.append(5)
check the size of stack: len(stack)
"""


class Solution:
    """
    @param: stk: an integer stack
    @return: void
    """
    def stackSorting(self, stk):
        # write your code here
        if not stk or len(stk) == 0:
            return stk

        stack = []
        stack.append(stk.pop())

        while stk:
            temp = stk.pop()
            while stack and temp > stack[-1]:
                stk.append(stack.pop())
            stack.append(temp)

        while stack:
            stk.append(stack.pop())
```