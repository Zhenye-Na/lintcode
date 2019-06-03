import heapq


"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if not lists or len(lists) == 0:
            return None

        pq = []
        for l in lists:
            while l:
                heapq.heappush(pq, l.val)
                l = l.next

        dummy = ListNode(0)
        p = dummy
        while len(pq) > 0:
            p.next = ListNode(heapq.heappop(pq))
            p = p.next

        return dummy.next
