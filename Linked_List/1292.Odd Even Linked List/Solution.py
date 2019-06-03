"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a singly linked list
    @return: Modified linked list
    """
    def oddEvenList(self, head):
        # write your code here
        if not head:
            return head

        odd = head
        even = head.next

        o, e = odd, even
        while e and e.next:
            o.next = e.next
            o = o.next
            e.next = o.next
            e = e.next

        o.next = even
        return head
