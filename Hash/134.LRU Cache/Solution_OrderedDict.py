from collections import OrderedDict


class LRUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        self.cache = OrderedDict()

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        # write your code here
        if key not in self.cache:
            return -1
        # pop value and insert to the bottom of queue
        value = self.cache.pop(key)
        self.cache[key] = value
        return value

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def set(self, key, value):
        # write your code here
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) == self.capacity:
            # last = True 时 pop规则为 FILO, last = False 时 pop 规则为 FIFO
            self.cache.popitem(last=False)
        self.cache[key] = value
