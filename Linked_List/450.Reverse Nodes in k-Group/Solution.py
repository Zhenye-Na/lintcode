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
    @param k: An integer
    @return: a ListNode
    """
    def reverseKGroup(self, head, k):
        # write your code here
        if not head:
            return head

        dummy = ListNode(0, head)
        head = dummy

        while head:
            head = self._reverseK(head, k)

        return dummy.next

    def _reverseK(self, node, k):
        n1, nk = node.next, node
        for _ in range(k):
            nk = nk.next
            if nk is None:
                return nk

        nk_next = nk.next

        # reverse
        prev, curt = None, n1
        while curt != nk_next:
            tmp = curt.next
            curt.next = prev
            prev = curt
            curt = tmp

        # connect
        node.next = nk
        n1.next = nk_next

        return n1
