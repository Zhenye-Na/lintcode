# 134. LRU Cache

**Description**

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: `get` and `set`.

- `get(key)` - Get the `value` (will always be positive) of the `key` if the `key` exists in the cache, otherwise return `-1`.
- `set(key, value)` - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item. Finally, you need to return the data from each `get`

**Example**

Example 1:

```
Input:
LRUCache(2)
set(2, 1)
set(1, 1)
get(2)
set(4, 1)
get(1)
get(2)
Output: [1,-1,1]
Explanation:
cache cap is 2，set(2,1)，set(1, 1)，get(2) and return 1，set(4,1) and delete (1,1)，because （1,1）is the least use，get(1) and return -1，get(2) and return 1.
```


Example 2:

```
Input:
LRUCache(1)
set(2, 1)
get(2)
set(3, 2)
get(2)
get(3)
Output: [1,-1,2]
Explanation:
cache cap is 1，set(2,1)，get(2) and return 1，set(3,2) and delete (2,1)，get(2) and return -1，get(3) and return 2.
```

**HashMap + Linked List**

LinkedHashMap <- 不能用

```python
class LinkedNode:
    
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.key_to_prev = {}
        self.dummy = LinkedNode()
        self.tail = self.dummy
        self.capacity = capacity


    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.key_to_prev:
            return -1
        self.kick(self.key_to_prev[key])
        return self.key_to_prev[key].next.value

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.key_to_prev:	   
            self.kick(self.key_to_prev[key])
            self.key_to_prev[key].next.value = value
        else:
            # 如果key不存在，则存入新节点
            self.push_back(LinkedNode(key, value))
            if len(self.key_to_prev) > self.capacity:
                # 如果缓存超出上限
                self.pop_front()

    def push_back(self, node):
        self.key_to_prev[node.key] = self.tail
        self.tail.next = node
        self.tail = node
    
    def pop_front(self):
        # 删除头部
        head = self.dummy.next
        self.key_to_prev.pop(head.key, None)
        self.dummy.next = head.next
        self.key_to_prev[head.next.key] = self.dummy

    # change "prev->node->next...->tail"
    # to "prev->next->...->tail->node"
    def kick(self, prev):
        # 将数据移动至尾部
        node = prev.next
        if node == self.tail:
            return
        prev.next = node.next
        if node.next is not None:
            self.key_to_prev[node.next.key] = prev
            node.next = None
        self.push_back(node)
```