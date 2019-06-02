# 955. Implement Queue by Circular Array

**Description**

Implement queue by circulant array. You need to support the following methods:

- `CircularQueue(n)`: initialize a circular array with size `n` to store elements
- `boolean isFull()`: return `true` if the array is full
- `boolean isEmpty()`: return `true` if there is no element in the array
- `void enqueue(element)`: add an element to the queue
- `int dequeue()`: pop an element from the queue

```
it's guaranteed in the test cases we won't call enqueue if it's full and we also won't call dequeue if it's empty. So it's ok to raise exception in scenarios described above.
```

**Example**

Example 1:

```
Input:
CircularQueue(5)
isFull()
isEmpty()
enqueue(1)
enqueue(2)
dequeue()
Output:
["false","true","1"]
```

Example 2:

```
Input:
CircularQueue(5)
isFull()
isEmpty()
enqueue(1)
enqueue(2)
dequeue()
dequeue()
enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
enqueue(5)
isFull()
dequeue()
dequeue()
dequeue()
dequeue()
dequeue()
Output:
["false","true","1","2","true","1","2","3","4","5"]
```


```python
# 本参考程序来自九章算法，由 @九章算法助教团队 提供。版权所有，转发请注明出处。
# - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
# - 现有的面试培训课程包括：九章算法班，系统设计班，算法强化班，Java入门与基础算法班，Android 项目实战班，
# - Big Data 项目实战班，算法面试高频题班, 动态规划专题班
# - 更多详情请见官方网站：http://www.jiuzhang.com/?source=code


class CircularQueue:
    def __init__(self, n):
        # do intialization if necessary
        self.arr = [None]*n
        self.head, self.tail = 0, -1
        self.size = n
    """
    @return:  return true if the array is full
    """
    def isFull(self):
        return self.head == (self.tail + 1) % self.size and not self.arr[self.tail] is None
        
    """
    @return: return true if there is no element in the array
    """
    def isEmpty(self):
        return self.arr[self.tail] is None
        
    """
    @param element: the element given to be added
    @return: nothing
    """
    def enqueue(self, element):
        self.tail = (self.tail + 1) % self.size
        self.arr[self.tail] = element

    """
    @return: pop an element from the queue
    """
    def dequeue(self):
        ele = self.arr[self.head]
        self.arr[self.head] = None
        self.head = (self.head + 1) % self.size
        return ele
```