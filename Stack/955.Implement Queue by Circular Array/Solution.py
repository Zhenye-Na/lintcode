from collections import deque

class CircularQueue:
    def __init__(self, n):
        # do intialization if necessary
        self.array = deque([])
        self.size = n

    """
    @return:  return true if the array is full
    """
    def isFull(self):
        # write your code here
        return len(self.array) == self.size

    """
    @return: return true if there is no element in the array
    """
    def isEmpty(self):
        # write your code here
        return len(self.array) == 0

    """
    @param element: the element given to be added
    @return: nothing
    """
    def enqueue(self, element):
        # write your code here
        self.array.append(element)

    """
    @return: pop an element from the queue
    """
    def dequeue(self):
        # write your code here
        return self.array.popleft()
