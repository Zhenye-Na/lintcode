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
        if len(lists) < 1:
            return None
        heap = []
        dummy = tail = ListNode(-1)
        
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))
        
        while len(heap) > 0:
            curr = heapq.heappop(heap)[1]
            tail.next = curr
            tail = tail.next
            if curr.next:
                heapq.heappush(heap, (curr.next.val, curr.next))
        
        return dummy.next