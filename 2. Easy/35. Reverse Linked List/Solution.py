"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        prev = None
        while head:
            # mark next list node
            tmp = head.next

            # swap order
            head.next = prev

            # update pointers
            prev = head
            head = tmp

        return prev
