# 224. Implement Three Stacks by Single Array

**Description**

Implement three stacks by single array.

```
You can assume the three stacks has the same size and big enough, you don't need to care about how to extend it if one of the stack is full.
```
  
**Example**

```
ThreeStacks(5)  // create 3 stacks with size 5 in single array. stack index from 0 to 2
push(0, 10)     // push 10 in the 1st stack.
push(0, 11)
push(1, 20)     // push 20 in the 2nd stack.
push(1, 21)
pop(0)          // return 11
pop(1)          // return 21
peek(1)         // return 20
push(2, 30)     // push 30 in the 3rd stack.
pop(2)          // return 30
isEmpty(2)      // return true
isEmpty(0)      // return false
```

```python
class ThreeStacks:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.array = [[], [], []]

    """
    @param: stackNum: An integer
    @param: value: An integer
    @return: nothing
    """
    def push(self, stackNum, value):
        # Push value into stackNum stack
        self.array[stackNum].append(value)

    """
    @param: stackNum: An integer
    @return: the top element
    """
    def pop(self, stackNum):
        # Pop and return the top element from stackNum stack
        return self.array[stackNum].pop()

    """
    @param: stackNum: An integer
    @return: the top element
    """
    def peek(self, stackNum):
        # Return the top element
        return self.array[stackNum][-1]

    """
    @param: stackNum: An integer
    @return: true if the stack is empty else false
    """
    def isEmpty(self, stackNum):
        # write your code here
        return len(self.array[stackNum]) == 0
```
