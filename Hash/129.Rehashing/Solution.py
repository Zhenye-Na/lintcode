"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # write your code here
        if not hashTable:
            return

        capacity = len(hashTable) * 2
        heads = [None for _ in range(capacity)]
        tails = [None for _ in range(capacity)]

        curr = None
        _node = None
        for node in hashTable:
            curr = node

            while curr:
                i = curr.val % capacity
                _node = ListNode(curr.val)

                if heads[i]:
                    tails[i].next = _node
                else:
                    heads[i] = _node

                tails[i] = _node

                curr = curr.next

        return heads