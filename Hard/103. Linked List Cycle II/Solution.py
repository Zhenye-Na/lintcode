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
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):
        # write your code here
        if not head or not head.next:
            return None

        # Two Pointers -> test whether there is cycle in the LinkedList
        slow, fast = head, head.next
        while slow != fast:
            if fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            else:
                return None

        # Find the first node in the circle
        pointer = head
        while pointer != slow.next:
            slow = slow.next
            pointer = pointer.next

        return pointer
