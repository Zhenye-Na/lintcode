"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # write your code here
        if not headA or not headB:
            return None

        # Find last ListNode
        a = headA
        while a.next:
            a = a.next

        a.next = headB

        # Fast - Slow pointers
        haveIntersection = False
        slow, fast = headA, headA
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                haveIntersection = True
                break

        if haveIntersection:
            third = headA
            while third != slow:
                third = third.next
                slow = slow.next
            return slow

        return None
