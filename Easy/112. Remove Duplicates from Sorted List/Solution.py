"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        if not head:
            return head
        prev = head
        curr = head
        result = head
        while curr:
            if curr.val != prev.val:
                prev.next.val = curr.val
                prev = prev.next
            curr = curr.next

        prev.next = None
        return result
