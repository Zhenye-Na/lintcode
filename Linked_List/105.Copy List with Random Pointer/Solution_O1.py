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
        node = head
        while node:
            copy = RandomListNode(node.label)
            nextNode = node.next
            node.next = copy
            copy.next = nextNode
            node = nextNode

        node = head
        head2 = node.next
        while node:
            copy = node.next
            nextNode = copy.next
            if nextNode:
                copy.next = nextNode.next
            if node.random:
                copy.random = node.random.next
            node = nextNode

        return head2
