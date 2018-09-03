"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @param: n: An integer
    @return: Nth to last node of a singly linked list.
    """
    def nthToLast(self, head, n):
        # write your code here
        if not head or n <= 0:
            return None

        # Test if n is out of bounds, if so return None
        first = head
        num = 1
        while first.next:
            first = first.next
            num += 1

        if n > num:
            return None

        # If not out of bounds, then use two pointers
        # Right pointer indicates how many elements away from the head
        right = head
        while n > 1:
            right = right.next
            n -= 1

        # Left pointer indicates result
        # When Right pointer reach the end of LinedList, then Left pointer points
        # to the element which is n slots before end
        left = head
        while right and right.next:
            left = left.next
            right = right.next

        return left
