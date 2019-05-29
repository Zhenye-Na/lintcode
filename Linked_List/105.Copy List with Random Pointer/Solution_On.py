"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        # write your code here
        if not head:
            return head

        # copy nodes
        p = head
        mapping = {}
        while p:
            mapping[p] = RandomListNode(p.label)
            p = p.next

        # copy edges
        p = head
        while p:
            if p.next:
                mapping[p].next = mapping[p.next]
            if p.random:
                mapping[p].random = mapping[p.random]
            p = p.next

        return mapping[head]
