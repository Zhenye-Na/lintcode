"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a ListNode
    @param v1: An integer
    @param v2: An integer
    @return: a new head of singly-linked list
    """
    def swapNodes(self, head, v1, v2):
        # write your code here
        if not head:
            return head

        dummy = ListNode(0, head)

        n1, n2 = None, None
        n1_prev, n2_prev = None, None
        prev = dummy
        node = dummy.next

        while node:
            if node.val == v1:
                n1 = node
                n1_prev= prev
            if node.val == v2:
                n2 = node
                n2_prev = prev
            prev = node
            node = node.next

        if n1 is None or n2 is None:
            return dummy.next

        n1_next = n1.next
        n2_next = n2.next

        # swap
        if n1.next == n2:
            n1_prev.next = n2
            n2.next = n1
            n1.next = n2_next
        
        elif n2.next == n1:
            n2_prev.next = n1
            n1.next = n2
            n2.next = n1_next

        else:
            n1_prev.next = n2
            n2.next = n1_next
            n2_prev.next = n1
            n1.next = n2_next

        return dummy.next
