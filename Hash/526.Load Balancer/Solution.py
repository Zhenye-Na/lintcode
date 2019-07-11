import random


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LoadBalancer:
    def __init__(self):
        # do intialization if necessary
        self.mapping = {}
        self.linkedlist = ListNode(-1)
        self.tail = self.linkedlist
        self.servers = []

    def add(self, server_id):
        """
        @param: server_id: add a new server to the cluster
        @return: nothing
        """
        # write your code here
        self.mapping[server_id] = self.tail
        self.tail.next = ListNode(server_id)
        self.tail = self.tail.next

        self.servers.append(server_id)

    def remove(self, server_id):
        """
        @param: server_id: server_id remove a bad server from the cluster
        @return: nothing
        """
        # write your code here
        prev_node = self.mapping[server_id]
        next_node = prev_node.next.next
        prev_node.next = next_node
        del self.mapping[server_id]

        self.servers.remove(server_id)

    def pick(self):
        """
        @return: pick a server in the cluster randomly with equal probability
        """
        # write your code here
        return self.servers[random.randint(0, len(self.servers) - 1)]
