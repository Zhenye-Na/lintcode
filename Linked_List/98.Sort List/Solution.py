"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """

    def sortList(self, head):
        # write your code here
        return self.quick_sort(head)

    def quick_sort(self, head):
        if head is None:
            return head
        if head.next is None:
            return head

        mid = self.find_mid(head)
        dummy_l = ListNode(-1)
        dummy_r = ListNode(-1)
        dummy_m = ListNode(-1)

        tail_l = dummy_l
        tail_r = dummy_r
        tail_m = dummy_m

        while (head is not None):
            if (head.val < mid.val):
                tail_l.next = head
                tail_l = head
            elif (head.val > mid.val):
                tail_r.next = head
                tail_r = head
            else:
                tail_m.next = head
                tail_m = head
            head = head.next

        tail_l.next = None
        tail_m.next = None
        tail_r.next = None

        left = self.quick_sort(dummy_l.next)
        right = self.quick_sort(dummy_r.next)
        return self.connect(left, dummy_m.next, right)

    def find_mid(self, node):
        if node is None:
            return node
        if node.next is None:
            return node

        slow = node
        fast = node
        while (fast.next is not None and fast.next.next is not None):
            slow = slow.next
            fast = fast.next.next

        res = slow.next
        return res

    def connect(self, left, mid, right):
        head = ListNode(-1, None)
        cur = head
        cur.next = left

        while (cur.next is not None):
            cur = cur.next
        cur.next = mid

        while (cur.next is not None):
            cur = cur.next
        cur.next = right

        return head.next
