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
    @return: head of the linked list
    """
    def deleteDuplicates(self, head):
        # write your code here
        if not head:
            return head

        dummy = ListNode(0)
        newHead = dummy
        left  = head
        right = head.next

        while True:

            if not left:
                break

            # right points to None or left.val != right.val
            if not right or left.val != right.val:
                dummy.next = ListNode(left.val)
                dummy = dummy.next
                left  = left.next
                if right:
                    right = right.next
            else:
                # left.val == right.val
                val = right.val
                while right and val == right.val:
                    tmp = right
                    right = right.next

                left = tmp

                if left:
                    left   = left.next
                if right:
                    right  = right.next


        return newHead.next
