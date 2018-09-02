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
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        if not head:
            return False

        slow, fast = head, head.next

        while slow != fast:
            # fast pointer is None -> no cycle
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        # If slow and fast pointers point to the same element after loop -> cycle exists
        return True
