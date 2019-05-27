"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: ListNode head is the head of the linked list
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        if not head or n < m or m < 1:
            return head

        dummy = ListNode(0)
        dummy.next = head
        head = dummy

        count = 1
        prev, first = head, head.next
        while head.next and count < m:
            prev  = first
            first = first.next

            count += 1

        # first -> the m_th node in the LinkedList
        newLast  = first
        newFirst = prev

        switch = 0
        while switch <= n - m:
            tmp = first.next
            first.next = prev
            prev  = first
            first = tmp

            switch += 1

        newLast.next  = first
        newFirst.next = prev

        return dummy.next
