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

        # Get list of nodes
        nodes = self.getNodes(head)

        # mapping from original nodes to new nodes
        mapping = {}

        # create mapping relation
        for node in nodes:
            mapping[node]        = RandomListNode(node.label)

        # update cloning nodes
        for node in nodes:
            mapping[node].next   = mapping[node.next] if node.next else None
            mapping[node].random = mapping[node.random] if node.random else None

        return mapping[head]


    def getNodes(self, head):
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        return nodes
