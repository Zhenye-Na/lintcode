"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the List
    @param k: rotate to the right k places
    @return: the list after rotation
    """
    def rotateRight(self, head, k):
        # write your code here
        if not head or k < 0:
            return head

        dummy = ListNode(0)
        dummy.next = head

        # Get length of Linked List and last node of Linked List
        last = dummy
        length = 0
        while last.next:
            last = last.next
            length += 1

        k = k % length

        if k == 0:
            return head

        keep, i = length - k, 0
        curr = dummy
        while i < keep:
            curr = curr.next
            i += 1

        newHead = curr.next
        last.next = dummy.next
        curr.next = None

        return newHead
