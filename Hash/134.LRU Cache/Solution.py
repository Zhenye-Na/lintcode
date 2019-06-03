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
