"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        keep = length - n
        curr = head
        i = 1
        while i <= keep and curr:
            prev = curr
            curr = curr.next
            i += 1

        prev.next = curr.next
        return dummy.next
