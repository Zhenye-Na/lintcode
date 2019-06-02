"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list
    @param x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        # write your code here
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        newHead = ListNode(0)
        res = newHead

        curr = head
        prev = dummy

        while curr:
            if curr.val < x:
                newHead.next = curr
                newHead = newHead.next

                tmp = curr.next
                prev.next = tmp
                curr = tmp
            else:
                prev = curr
                curr = curr.next


        newHead.next = dummy.next
        return res.next
